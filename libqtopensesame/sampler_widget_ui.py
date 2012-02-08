# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/sampler_widget.ui'
#
# Created: Wed Feb  8 18:21:34 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(550, 436)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.frame_notification = QtGui.QFrame(Form)
        self.frame_notification.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_notification.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_notification.setObjectName(_fromUtf8("frame_notification"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.frame_notification)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.widget_2 = QtGui.QWidget(self.frame_notification)
        self.widget_2.setStyleSheet(_fromUtf8("background-color: #fcaf3e;\n"
"color: rgb(255, 255, 255);"))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(5)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_10 = QtGui.QLabel(self.widget_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/about_large.png")))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_2.addWidget(self.label_10)
        self.label_15 = QtGui.QLabel(self.widget_2)
        self.label_15.setText(QtGui.QApplication.translate("Form", "One of the controls is defined using variables and therefore the controls are disabled. Use the script editor to edit the sampler.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_2.addWidget(self.label_15)
        self.button_script = QtGui.QPushButton(self.widget_2)
        self.button_script.setToolTip(QtGui.QApplication.translate("Form", "Edit the script to see the definition", None, QtGui.QApplication.UnicodeUTF8))
        self.button_script.setText(QtGui.QApplication.translate("Form", "Edit script", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/script.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_script.setIcon(icon)
        self.button_script.setObjectName(_fromUtf8("button_script"))
        self.horizontalLayout_2.addWidget(self.button_script)
        self.horizontalLayout_4.addWidget(self.widget_2)
        self.gridLayout.addWidget(self.frame_notification, 0, 1, 1, 1)
        self.frame_controls = QtGui.QFrame(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_controls.sizePolicy().hasHeightForWidth())
        self.frame_controls.setSizePolicy(sizePolicy)
        self.frame_controls.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_controls.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_controls.setObjectName(_fromUtf8("frame_controls"))
        self.gridLayout_3 = QtGui.QGridLayout(self.frame_controls)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.frame_controls)
        self.label.setText(QtGui.QApplication.translate("Form", "Sound file", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.edit_sample = QtGui.QLineEdit(self.frame_controls)
        self.edit_sample.setToolTip(QtGui.QApplication.translate("Form", "The sound file. Expecting a .ogg or .wav file.", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_sample.setObjectName(_fromUtf8("edit_sample"))
        self.gridLayout_3.addWidget(self.edit_sample, 1, 1, 1, 1)
        self.button_browse_sample = QtGui.QPushButton(self.frame_controls)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_browse_sample.sizePolicy().hasHeightForWidth())
        self.button_browse_sample.setSizePolicy(sizePolicy)
        self.button_browse_sample.setToolTip(QtGui.QApplication.translate("Form", "Select a sound file from the file pool", None, QtGui.QApplication.UnicodeUTF8))
        self.button_browse_sample.setText(QtGui.QApplication.translate("Form", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/browse.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_browse_sample.setIcon(icon1)
        self.button_browse_sample.setObjectName(_fromUtf8("button_browse_sample"))
        self.gridLayout_3.addWidget(self.button_browse_sample, 1, 2, 1, 1)
        self.frame = QtGui.QFrame(self.frame_controls)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame)
        self.gridLayout_2.setMargin(4)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_7 = QtGui.QLabel(self.frame)
        self.label_7.setText(QtGui.QApplication.translate("Form", "Volume", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.dial_volume = QtGui.QDial(self.frame)
        self.dial_volume.setToolTip(QtGui.QApplication.translate("Form", "Set the volume of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.dial_volume.setMaximum(100)
        self.dial_volume.setProperty("value", 99)
        self.dial_volume.setNotchTarget(10.0)
        self.dial_volume.setNotchesVisible(True)
        self.dial_volume.setObjectName(_fromUtf8("dial_volume"))
        self.gridLayout_2.addWidget(self.dial_volume, 1, 0, 1, 1)
        self.spin_volume = QtGui.QDoubleSpinBox(self.frame)
        self.spin_volume.setToolTip(QtGui.QApplication.translate("Form", "Set the volume of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_volume.setSuffix(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_volume.setMaximum(100.0)
        self.spin_volume.setSingleStep(100.0)
        self.spin_volume.setObjectName(_fromUtf8("spin_volume"))
        self.gridLayout_2.addWidget(self.spin_volume, 2, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.frame)
        self.label_8.setText(QtGui.QApplication.translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pan</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setText(QtGui.QApplication.translate("Form", "Pitch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.dial_pan = QtGui.QDial(self.frame)
        self.dial_pan.setToolTip(QtGui.QApplication.translate("Form", "Set the panning (left-right) of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.dial_pan.setMinimum(-20)
        self.dial_pan.setMaximum(20)
        self.dial_pan.setNotchTarget(10.0)
        self.dial_pan.setNotchesVisible(True)
        self.dial_pan.setObjectName(_fromUtf8("dial_pan"))
        self.gridLayout_2.addWidget(self.dial_pan, 1, 1, 1, 1)
        self.dial_pitch = QtGui.QDial(self.frame)
        self.dial_pitch.setToolTip(QtGui.QApplication.translate("Form", "Set the relative pitch of the sound (100% = original)", None, QtGui.QApplication.UnicodeUTF8))
        self.dial_pitch.setMaximum(400)
        self.dial_pitch.setProperty("value", 100)
        self.dial_pitch.setNotchTarget(20.0)
        self.dial_pitch.setNotchesVisible(True)
        self.dial_pitch.setObjectName(_fromUtf8("dial_pitch"))
        self.gridLayout_2.addWidget(self.dial_pitch, 1, 2, 1, 1)
        self.spin_pan = QtGui.QDoubleSpinBox(self.frame)
        self.spin_pan.setToolTip(QtGui.QApplication.translate("Form", "Set the panning (left-right) of the sound", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_pan.setMinimum(-1000.0)
        self.spin_pan.setMaximum(1000.0)
        self.spin_pan.setProperty("value", 0.0)
        self.spin_pan.setObjectName(_fromUtf8("spin_pan"))
        self.gridLayout_2.addWidget(self.spin_pan, 2, 1, 1, 1)
        self.spin_pitch = QtGui.QDoubleSpinBox(self.frame)
        self.spin_pitch.setToolTip(QtGui.QApplication.translate("Form", "Set the relative pitch of the sound (100% = original)", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_pitch.setSuffix(QtGui.QApplication.translate("Form", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_pitch.setMaximum(10000.0)
        self.spin_pitch.setProperty("value", 99.99)
        self.spin_pitch.setObjectName(_fromUtf8("spin_pitch"))
        self.gridLayout_2.addWidget(self.spin_pitch, 2, 2, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 3)
        self.label_4 = QtGui.QLabel(self.frame_controls)
        self.label_4.setText(QtGui.QApplication.translate("Form", "Stop after", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        self.spin_stop_after = QtGui.QSpinBox(self.frame_controls)
        self.spin_stop_after.setToolTip(QtGui.QApplication.translate("Form", "Force playback to stop after a specified duration. 0ms corresponds to a full playback.", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_stop_after.setSuffix(QtGui.QApplication.translate("Form", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_stop_after.setMaximum(100000000)
        self.spin_stop_after.setObjectName(_fromUtf8("spin_stop_after"))
        self.gridLayout_3.addWidget(self.spin_stop_after, 3, 1, 1, 2)
        self.spin_fade_in = QtGui.QSpinBox(self.frame_controls)
        self.spin_fade_in.setToolTip(QtGui.QApplication.translate("Form", "The fade-in time of the sound.", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_fade_in.setSuffix(QtGui.QApplication.translate("Form", "ms", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_fade_in.setMaximum(10000000)
        self.spin_fade_in.setObjectName(_fromUtf8("spin_fade_in"))
        self.gridLayout_3.addWidget(self.spin_fade_in, 4, 1, 1, 2)
        self.edit_duration = QtGui.QLineEdit(self.frame_controls)
        self.edit_duration.setToolTip(QtGui.QApplication.translate("Form", "Set the duration of the sampler item. Expecting a duration in ms, \'sound\' (to wait until the sound is finished playing), \'keypress\', \'mouseclick\', or a variable (e.g., \'[sampler_dur]\').", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_duration.setText(QtGui.QApplication.translate("Form", "sound", None, QtGui.QApplication.UnicodeUTF8))
        self.edit_duration.setObjectName(_fromUtf8("edit_duration"))
        self.gridLayout_3.addWidget(self.edit_duration, 5, 1, 1, 2)
        self.label_5 = QtGui.QLabel(self.frame_controls)
        self.label_5.setText(QtGui.QApplication.translate("Form", "Fade in", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.frame_controls)
        self.label_6.setText(QtGui.QApplication.translate("Form", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 5, 0, 1, 1)
        self.widget = QtGui.QWidget(self.frame_controls)
        self.widget.setStyleSheet(_fromUtf8("background-color: #fcaf3e;\n"
"color: rgb(255, 255, 255);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(5)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/sampler.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_9 = QtGui.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setText(QtGui.QApplication.translate("Form", "Sampler controls", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout.addWidget(self.label_9)
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 3)
        self.gridLayout.addWidget(self.frame_controls, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass

import icons_rc
