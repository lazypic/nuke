#coding:utf8
import nuke
import os
from PySide2.QtWidgets import *

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass
	customApp = QWidget()
	layout = QVBoxLayout()
	envs = ["USER","OCIO","NUKE_PATH","NUKE_FONT_PATH"]
	for e in envs:
		layout.addWidget(QLabel("$%s : %s" % (e, os.environ[e])))
	customApp.setLayout(layout)
	try:
		customApp.show()
	except:
		pass
