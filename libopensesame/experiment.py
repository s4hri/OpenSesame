
#-*- coding:utf-8 -*-

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame import misc, item, exceptions, plugins, debug
import random
import os.path
import shutil
import sys
import time
import tarfile
import tempfile
import codecs

# Contains a list of all pool folders, which need to be removed on program exit
pool_folders = []

class experiment(item.item):

	"""The main experiment class, which is the first item to be called"""

	def __init__(self, name='experiment', string=None, pool_folder=None):

		"""<DOC>
		Constructor. The experiment is created automatically be OpenSesame and
		you will generally not need to create it yourself.

		Keyword arguments:
		name -- the name of the experiment (default='experiment')		
		string -- a string containing the experiment definition (default=None)
		pool_folder -- a specific folder to be used for the file pool
					   (default=None)
		</DOC>"""

		global pool_folders
		
		random.seed()		

		self.items = {}
		self.running = False
		self.auto_response = False
		self.plugin_folder = "plugins"
		self.start_response_interval = None
		self.cleanup_functions = []
		self.restart = False
		self.experiment_path = None
		self.title = 'My Experiment'

		# Set default variables
		self.coordinates = "relative"
		self.compensation = 0
		self.start = "experiment"
		
		# Sound parameters
		self.sound_freq = 48000
		self.sound_sample_size = -16 # Negative values means signed
		self.sound_channels = 2
		self.sound_buf_size = 512
		self.resources = {}

		# Backend parameters
		self.canvas_backend = "xpyriment"
		self.keyboard_backend = "legacy"
		self.mouse_backend = "legacy"
		self.sampler_backend = "legacy"
		self.synth_backend = "legacy"

		# Display parameters
		self.width = 1024
		self.height = 768
		self.background = "black"
		self.foreground = "white"		
		self.resolution = self.width, self.height
		self.fullscreen = False

		# Font parameters
		self.font_size = 18
		self.font_family = "mono"
		self.font_italic = "no"
		self.font_bold = "no"

		# Logfile parameters
		self._log = None
		self.logfile = None
		
		# This is a dummy variable for backwards compatibility. The logfile 
		# encoding is always utf-8, and this variable doesn't do anything.
		self.logfile_codec = "utf-8"	

		# Variables used for bookkeeping responses
		self.total_correct = 0
		self.total_response_time = 0
		self.total_responses = 0
		
		# Default subject info
		self.subject_nr = 0
		self.subject_parity = "even"

		# This is some duplication of the option parser in qtopensesame,
		# but nevertheless keep it so we don't need qtopensesame
		self.debug = "--debug" in sys.argv or "-d" in sys.argv
		self._stack = "--stack" in sys.argv or "-s" in sys.argv

		# Pool folder
		if pool_folder == None:
			self.pool_folder = tempfile.mkdtemp(".opensesame_pool")
			pool_folders.append(self.pool_folder)
			debug.msg("creating new pool folder")
		else:
			debug.msg("reusing existing pool folder")
			self.pool_folder = pool_folder
		debug.msg("pool folder is '%s'" % self.pool_folder)
		
		string = self.open(string)
		item.item.__init__(self, name, self, string)
		
	def module_container(self):

		"""Specify the module that contains the item modules"""

		return "libopensesame"

	def item_prefix(self):

		"""
		A prefix for the plug-in classes, so that [prefix][plugin] class is used
		instead of the [plugin] class
		"""

		return ""

	def set_subject(self, nr):

		"""<DOC>
		Set the subject number and parity (even/ odd)

		Arguments:
		nr -- the subject nr
		</DOC>"""

		# Set the subject nr and parity
		self.set("subject_nr", nr)
		if nr % 2 == 0:
			self.set("subject_parity", "even")
		else:
			self.set("subject_parity", "odd")

	def read_definition(self, s):

		"""
		Extract a the definition of a single item from the string

		Arguments:
		s -- the definition string

		Returns:
		A (str, str) tuple with the full string minus the definition string
		and the definition string
		"""

		# Read the string until the end of the definition
		def_str = u''
		line = next(s, None)
		if line == None:
			return None, u''
		get_next = False
		while True:
			if len(line) > 0:
				if line[0] != u'\t':
					break
				else:
					def_str += line + u'\n'
			line = next(s, None)
			if line == None:
				break
		return line, def_str

	def parse_definition(self, item_type, item_name, string):

		"""
		Initialize a single definition, using the string, and
		add it to the dictionary of items

		Arguments:
		item_type -- the type of the item
		item_name -- the name of the item
		string -- the string containing the definition
		"""

		if plugins.is_plugin(item_type):

			# Load a plug-in
			if debug.enabled:
				debug.msg(u"loading plugin '%s'" % item_type)
				item = plugins.load_plugin(item_type, item_name, self, string, \
					self.item_prefix())
			else:
				try:
					item = plugins.load_plugin(item_type, item_name, self, \
						string, self.item_prefix())
				except:
					raise exceptions.script_error(u"Failed load plugin '%s'" % \
						item_type)
			self.items[item_name] = item

		else:

			# Load the module from the regular items
			debug.msg(u"loading core plugin '%s'" % item_type)
			if debug.enabled:
				exec("from %s import %s" % (self.module_container(), item_type))
			try:
				if not self.debug:
					exec("from %s import %s" % (self.module_container(), \
						item_type))
			except:
				raise exceptions.script_error( \
					u"Failed to import item '%s' as '%s'. " \
					% (item_type, item_name)
					+ "Perhaps the experiment requires a plug-in that is not available on your system.", \
					full=False)

			cmd = '%(item_type)s.%(item_type)s("%(item_name)s", self, u"""%(string)s""")' \
				% {"item_type" : item_type, "item_name" : item_name, "string" \
				: string.replace(u'"', u'\\"')}

			if debug.enabled:
				bytecode = compile(cmd, "<string>", "eval")
				self.items[item_name] = eval(bytecode)
			else:
				try:
					bytecode = compile(cmd, "<string>", "eval")
					self.items[item_name] = eval(bytecode)
				except Exception as e:
					raise exceptions.script_error( \
						u"Failed to instantiate module '%s' as '%s': %s" % \
						(item_type, item_name, e))

	def from_string(self, string):

		"""
		Read the entire experiment from a string

		Arguments:
		string -- a definition string
		"""

		debug.msg(u"building experiment")
		s = iter(string.split("\n"));
		line = next(s, None)
		while line != None:

			get_next = True
			try:
				l = self.split(line)
			except ValueError as e:									
				raise exceptions.script_error( \
					u"Failed to parse script. Maybe it contains illegal characters or unclosed quotes?")

			if len(l) > 0:
				self.parse_variable(line)

				# Parse definitions
				if l[0] == u"define":
					if len(l) != 3:
						raise exceptions.script_error( \
							u"Failed to parse definition '%s'" \
							% line)
					item_type = l[1]
					item_name = self.sanitize(l[2])
					line, def_str = self.read_definition(s)
					get_next = False					
					self.parse_definition(item_type, item_name, def_str)					

			if get_next:
				line = next(s, None)

	def run(self):

		"""Run the experiment"""

		self.running = True
		self.init_sound()
		self.init_display()
		self.init_log()

		print "experiment.run(): experiment started at %s" % time.ctime()

		if self.start in self.items:
			self.items[self.start].prepare()
			self.items[self.start].run()
		else:
			raise exceptions.runtime_error( \
				"Could not find item '%s', which is the entry point of the experiment" \
				% self.start)

		print "experiment.run(): experiment finished at %s" % time.ctime()

		self.end()

	def cleanup(self):

		"""Call all the cleanup functions"""

		while len(self.cleanup_functions) > 0:
			func = self.cleanup_functions.pop()
			debug.msg("calling cleanup function")
			func()

	def end(self):

		"""Nicely end the experiment"""

		self.running = False
		openexp.experiment.experiment.end(self)
		self.cleanup()

	def to_string(self):

		"""
		Encode the experiment into a string

		Returns:
		A definition string for the experiment
		"""

		s = u'# Generated by OpenSesame %s (%s)\n' % (misc.version, \
			misc.codename) + \
			u'# %s (%s)\n' % (time.ctime(), os.name) + \
			u'# <http://www.cogsci.nl/opensesame>\n\n'
		for var in self.variables:
			s += self.variable_to_string(var)
		s += u'\n'
		for item in self.items:
			s += self.items[item].to_string() + u'\n'
		return s

	def resource(self, name):

		"""
		Retrieve a file from the resources folder

		Arguments:
		name -- the file name

		Returns:
		The full path to the file in the resources folder
		"""

		if self != None:
			if name in self.resources:
				return self.resources[name]
			if os.path.exists(self.get_file(name)):
				return self.get_file(name)
		path = misc.resource(name)
		if path == None:
			raise Exception( \
				"The resource '%s' could not be found in libopensesame.experiment.resource()" \
				% name)
		return path

	def get_file(self, path):

		"""<DOC>
		Returns the path to a file. First checks if the file is in the file pool
		and then the folder of the current experiment (if any)
		Otherwise, simply return the path.

		Arguments:
		path -- the filename

		Returns:
		The full path to the file
		</DOC>"""

		if type(path) not in(unicode, str):
			raise exceptions.runtime_error( \
				"A string should be passed to experiment.get_file(), not '%s'" \
				% path)
		if os.path.exists(os.path.join(self.pool_folder, path)):
			return os.path.join(self.pool_folder, path)
		elif self.experiment_path != None and os.path.exists(os.path.join( \
			self.experiment_path, path)):
			return os.path.join(self.experiment_path, path)
		else:
			return path

	def file_in_pool(self, path):

		"""<DOC>
		Checks if a file is in the file pool

		Returns:
		A boolean indicating if the file is in the pool
		</DOC>"""

		return os.path.exists(self.get_file(path))

	def save(self, path, overwrite=False):

		"""
		Save the experiment to file. If no extension is provided,
		.opensesame.tar.gz is chosen by default.

		Arguments:
		path -- the target file to save to

		Keyword arguments:
		overwrite -- a boolean indicating if existing files should be
					 overwritten (default=False)

		Returns:
		The path on successfull saving or False otherwise
		"""

		debug.msg("asked to save '%s'" % path)

		# Determine the extension
		ext = os.path.splitext(path)[1].lower()

		# If the extension is .opensesame, save the script as plain text
		if ext == ".opensesame":
			if os.path.exists(path) and not overwrite:
				return False
			debug.msg("saving as .opensesame file")
			f = open(path, "w")
			f.write(self.usanitize(self.to_string()))
			f.close()
			self.experiment_path = os.path.dirname(path)
			return path

		# Use the .opensesame.tar.gz extension by default
		if path[-len(".opensesame.tar.gz"):] != ".opensesame.tar.gz":
			path += ".opensesame.tar.gz"

		if os.path.exists(path) and not overwrite:
			return False

		debug.msg("saving as .opensesame.tar.gz file")

		# Write the script to a text file
		script = self.to_string()
		script_path = os.path.join(self.pool_folder, "script.opensesame")
		f = open(script_path, "w")
		f.write(self.usanitize(script))
		f.close()

		# Create the archive in a a temporary folder and move it
		# afterwards. This hack is needed, because tarfile fails
		# on a Unicode path.
		tmp_path = tempfile.mktemp(suffix = ".opensesame.tar.gz")
		tar = tarfile.open(tmp_path, "w:gz")
		tar.add(script_path, "script.opensesame")
		os.remove(script_path)
		tar.add(self.pool_folder, "pool", True)
		tar.close()

		# Move the file to the intended location
		shutil.move(tmp_path, path)

		self.experiment_path = os.path.dirname(path)
		return path

	def open(self, path):

		"""
		If the path exists, open the file, extract the pool and return the
		contents of the script.opensesame. Otherwise just return the input
		string, because it probably was a definition to begin with

		Arguments:
		path -- the file to be opened

		Returns:
		A unicode defition string
		"""

		# If the path is not a path at all, but a string containing
		# the script, return it
		
		if not os.path.exists(path):
			debug.msg("opening from unicode string")
			self.experiment_path = None
			return path

		# If the file is a regular text script,
		# read it and return it
		ext = ".opensesame.tar.gz"
		if path[-len(ext):] != ext:
			debug.msg("opening .opensesame file")
			self.experiment_path = os.path.dirname(path)
			return self.unsanitize(open(path, "rU").read())

		debug.msg("opening .opensesame.tar.gz file")

		# If the file is a .tar.gz archive, extract
		# the pool to the pool folder and return the
		# contents of opensesame.script
		tar = tarfile.open(path, "r:gz")
		for name in tar.getnames():
			folder, fname = os.path.split(name)
			if folder == "pool":
				debug.msg("extracting '%s'" % name)
				tar.extract(name, self.pool_folder)
				os.rename(os.path.join(self.pool_folder, name), os.path.join( \
					self.pool_folder, fname))
				os.rmdir(os.path.join(self.pool_folder, folder))

		script_path = os.path.join(self.pool_folder, "script.opensesame")
		tar.extract("script.opensesame", self.pool_folder)
		script = self.unsanitize(open(script_path, "rU").read())
		os.remove(script_path)
		self.experiment_path = os.path.dirname(path)
		return script

	def reset_feedback(self):

		"""Reset the feedback variables (acc, avg_rt, etc.)"""

		self.total_responses = 0
		self.total_correct = 0
		self.total_response_time = 0
		self.avg_rt = "undefined"
		self.average_response_time = "undefined"
		self.accuracy = "undefined"
		self.acc = "undefined"

	def var_info(self):

		"""
		Return a list of (name, value) tuples with variable descriptions
		for the main experiment

		Returns:
		A list of tuples
		"""

		l = []
		for var in self.variables:
			l.append( (var, self.variables[var]) )
		return l

	def var_list(self, filt=""):

		"""
		Return a list of (name, value, description) tuples with variable
		descriptions for all items

		Keyword arguments:
		filt -- a search string to filter by

		Returns:
		A list of tuples
		"""

		l = []
		i = 0
		for item in self.items:
			var_list = self.items[item].var_info()
			for var, val in var_list:
				if filt in var.lower() or filt in self.unistr(val).lower() or \
					filt in item.lower():
					l.append( (var, val, item) )

		# Global variables are defined in the experiment class itself
		var_list = self.var_info()
		for var, val in var_list:
			if filt in var.lower() or filt in self.unistr(val).lower() or filt in \
				"global":
				l.append( (var, val, "global") )

		return l
				
	def init_sound(self):

		"""Intialize the sound backend"""

		from openexp import sampler
		sampler.init_sound(self)

	def init_display(self):

		"""Initialize the canvas backend"""

		from openexp import canvas
		canvas.init_display(self)

	def init_log(self):

		"""Open the logile"""
		
		# Do not open the logfile if it's already open
		if self._log != None:
			return
		# Open the logfile
		if self.logfile == None:
			self.logfile = u'defaultlog.txt'
		self._log = codecs.open(self.logfile, 'w', encoding=self.encoding)
		print "experiment.init_log(): using '%s' as logfile (%s)" % \
			(self.logfile, self.logfile_codec)
						
	def _sleep_func(self, ms):

		"""
		Sleeps for a specific time. 
		
		* This is a stub that should be replaced by a proper function by the
		  canvas backend. See openexp._canvas.legacy.init_display()
		
		Arguments:
		ms -- the sleep period
		"""
		
		raise exceptions.runtime_error( \
			"experiment._sleep_func(): This function should be set by the canvas backend." \
			)			

	def _time_func(self):

		"""
		Get the time
		
		* This is a stub that should be replaced by a proper function by the
		  canvas backend. See openexp._canvas.legacy.init_display()
		  
		Returns:
		A timestamp in milliseconds. Depending on the backend, this may be an
		int or a float
		"""

		raise exceptions.runtime_error( \
			"experiment._time_func(): This function should be set by the canvas backend." \
			)

	def end(self):

		"""Gracefully end the experiment"""

		from openexp import sampler, canvas
		try:
			self._log.flush()
			os.fsync(self._log)
			self._log.close()
		except:
			pass					
		sampler.close_sound(self)
		canvas.close_display(self)		

def clean_up(verbose=False):

	"""
	Clean up the temporary pool folders

	Keyword arguments:
	verbose -- a boolean indicating if debugging output should be given
			   (default=False)
	"""

	from openexp import canvas
	global pool_folders
	if verbose:
		print "experiment.clean_up()"

	for path in pool_folders:
		if verbose:
			print "experiment.clean_up(): removing '%s'" % path
		try:
			shutil.rmtree(path)
		except:
			if verbose:
				print "experiment.clean_up(): failed to remove '%s'" % path
	canvas.clean_up(verbose)


