# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cn.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 771)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.btn_get_video = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_get_video.sizePolicy().hasHeightForWidth())
        self.btn_get_video.setSizePolicy(sizePolicy)
        self.btn_get_video.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_get_video.setStyleSheet("")
        self.btn_get_video.setObjectName("btn_get_video")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_get_video)
        self.source_mp4 = QtWidgets.QLineEdit(self.widget)
        self.source_mp4.setMinimumSize(QtCore.QSize(0, 35))
        self.source_mp4.setInputMask("")
        self.source_mp4.setText("")
        self.source_mp4.setObjectName("source_mp4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source_mp4)
        self.verticalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.btn_save_dir = QtWidgets.QPushButton(self.widget)
        self.btn_save_dir.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_save_dir.setStyleSheet("")
        self.btn_save_dir.setObjectName("btn_save_dir")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_save_dir)
        self.target_dir = QtWidgets.QLineEdit(self.widget)
        self.target_dir.setMinimumSize(QtCore.QSize(0, 35))
        self.target_dir.setInputMask("")
        self.target_dir.setText("")
        self.target_dir.setObjectName("target_dir")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.target_dir)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.proxy = QtWidgets.QLineEdit(self.widget)
        self.proxy.setMinimumSize(QtCore.QSize(0, 35))
        self.proxy.setObjectName("proxy")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.proxy)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.source_language = QtWidgets.QComboBox(self.widget)
        self.source_language.setMinimumSize(QtCore.QSize(0, 35))
        self.source_language.setObjectName("source_language")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source_language)
        self.horizontalLayout.addLayout(self.formLayout_4)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setObjectName("label_3")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.target_language = QtWidgets.QComboBox(self.widget)
        self.target_language.setMinimumSize(QtCore.QSize(0, 35))
        self.target_language.setObjectName("target_language")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.target_language)
        self.horizontalLayout.addLayout(self.formLayout_5)
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 35))
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.voice_role = QtWidgets.QComboBox(self.widget)
        self.voice_role.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_role.setObjectName("voice_role")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_role)
        self.horizontalLayout.addLayout(self.formLayout_6)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_7 = QtWidgets.QFormLayout()
        self.formLayout_7.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 35))
        self.label_5.setObjectName("label_5")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.whisper_model = QtWidgets.QComboBox(self.widget)
        self.whisper_model.setMinimumSize(QtCore.QSize(0, 35))
        self.whisper_model.setObjectName("whisper_model")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.whisper_model)
        self.horizontalLayout_2.addLayout(self.formLayout_7)
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_8.setObjectName("formLayout_8")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 35))
        self.label_6.setObjectName("label_6")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.voice_rate = QtWidgets.QLineEdit(self.widget)
        self.voice_rate.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_rate.setObjectName("voice_rate")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_rate)
        self.horizontalLayout_2.addLayout(self.formLayout_8)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_9.setObjectName("formLayout_9")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 35))
        self.label_7.setObjectName("label_7")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.voice_silence = QtWidgets.QLineEdit(self.widget)
        self.voice_silence.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_silence.setObjectName("voice_silence")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_silence)
        self.horizontalLayout_2.addLayout(self.formLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.voice_autorate = QtWidgets.QCheckBox(self.widget)
        self.voice_autorate.setMinimumSize(QtCore.QSize(0, 30))
        self.voice_autorate.setObjectName("voice_autorate")
        self.horizontalLayout_4.addWidget(self.voice_autorate)
        self.remove_background = QtWidgets.QCheckBox(self.widget)
        self.remove_background.setMinimumSize(QtCore.QSize(0, 30))
        self.remove_background.setObjectName("remove_background")
        self.horizontalLayout_4.addWidget(self.remove_background)
        self.subtitle_type = QtWidgets.QComboBox(self.widget)
        self.subtitle_type.setMinimumSize(QtCore.QSize(0, 30))
        self.subtitle_type.setCurrentText("")
        self.subtitle_type.setObjectName("subtitle_type")
        self.horizontalLayout_4.addWidget(self.subtitle_type)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startbtn = QtWidgets.QPushButton(self.widget)
        self.startbtn.setMinimumSize(QtCore.QSize(200, 50))
        self.startbtn.setObjectName("startbtn")
        self.horizontalLayout_3.addWidget(self.startbtn)
        self.label_8 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.process = QtWidgets.QTextEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process.sizePolicy().hasHeightForWidth())
        self.process.setSizePolicy(sizePolicy)
        self.process.setMinimumSize(QtCore.QSize(0, 100))
        self.process.setAutoFillBackground(False)
        self.process.setStyleSheet("border:0;\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.process.setReadOnly(True)
        self.process.setObjectName("process")
        self.verticalLayout.addWidget(self.process)
        self.subtitle_area = QtWidgets.QPlainTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitle_area.sizePolicy().hasHeightForWidth())
        self.subtitle_area.setSizePolicy(sizePolicy)
        self.subtitle_area.setMinimumSize(QtCore.QSize(100, 0))
        self.subtitle_area.setReadOnly(True)
        self.subtitle_area.setObjectName("subtitle_area")
        self.horizontalLayout_5.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "视频翻译和配音"))
        self.btn_get_video.setText(_translate("MainWindow", "待翻译视频"))
        self.source_mp4.setPlaceholderText(_translate("MainWindow", "选择待翻译的mp4视频"))
        self.btn_save_dir.setText(_translate("MainWindow", "保存目录"))
        self.target_dir.setPlaceholderText(_translate("MainWindow", "选择翻译后的视频保存到的位置，默认原目录下_video_out中"))
        self.label.setText(_translate("MainWindow", "代理地址"))
        self.proxy.setPlaceholderText(_translate("MainWindow", "比如 http://127.0.0.1:10809 大陆地区必须填写"))
        self.label_2.setText(_translate("MainWindow", "视频原语言"))
        self.source_language.setToolTip(_translate("MainWindow", "视频原始语音所用语言"))
        self.label_3.setText(_translate("MainWindow", "翻译目标语言"))
        self.target_language.setToolTip(_translate("MainWindow", "你希望翻译为哪种语言"))
        self.label_4.setText(_translate("MainWindow", "配音角色"))
        self.voice_role.setToolTip(_translate("MainWindow", "选No代表不进行配音"))
        self.label_5.setText(_translate("MainWindow", "语音识别模型"))
        self.whisper_model.setToolTip(_translate("MainWindow", "base到large，效果越来越好，但速度也越来越慢"))
        self.label_6.setText(_translate("MainWindow", "配音语速"))
        self.voice_rate.setToolTip(_translate("MainWindow", "是否加速或减速播放配音"))
        self.voice_rate.setPlaceholderText(_translate("MainWindow", "正数则加速，负数则减速，-90到+90"))
        self.label_7.setText(_translate("MainWindow", "静音片段"))
        self.voice_silence.setToolTip(_translate("MainWindow", "默认500ms，越小切分的片段越多"))
        self.voice_silence.setPlaceholderText(_translate("MainWindow", "分割语音的静音时长，单位ms"))
        self.voice_autorate.setToolTip(_translate("MainWindow", "如果配音后时长大于原时长，是否强制加速播放"))
        self.voice_autorate.setText(_translate("MainWindow", "自动加速?"))
        self.remove_background.setToolTip(_translate("MainWindow", "去除背景音乐噪声等"))
        self.remove_background.setText(_translate("MainWindow", "消除背景音?"))
        self.subtitle_type.setToolTip(_translate("MainWindow", "嵌入式字幕无论哪里播放始终显示字幕，不可隐藏。\n"
"软字幕如果播放器支持，可在播放器中控制显示或隐藏。\n"
"如果你想网页中播放时显示字幕，请选择嵌入式字幕。\n"
""))
        self.startbtn.setText(_translate("MainWindow", "开始"))
        self.subtitle_area.setPlaceholderText(_translate("MainWindow", "这里显示字幕信息"))
