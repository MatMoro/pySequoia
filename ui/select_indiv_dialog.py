# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_indiv_dialog.ui'
#
# Created: Sat Sep 21 17:05:53 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_select_indiv_dialog(object):
    def setupUi(self, select_indiv_dialog):
        select_indiv_dialog.setObjectName(_fromUtf8("select_indiv_dialog"))
        select_indiv_dialog.resize(423, 344)
        select_indiv_dialog.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(select_indiv_dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(select_indiv_dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.filter = QtGui.QLineEdit(select_indiv_dialog)
        self.filter.setObjectName(_fromUtf8("filter"))
        self.horizontalLayout.addWidget(self.filter)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.indiv_list = QtGui.QListWidget(select_indiv_dialog)
        self.indiv_list.setObjectName(_fromUtf8("indiv_list"))
        self.verticalLayout.addWidget(self.indiv_list)
        self.buttonBox = QtGui.QDialogButtonBox(select_indiv_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.label.setBuddy(self.filter)

        self.retranslateUi(select_indiv_dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), select_indiv_dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), select_indiv_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(select_indiv_dialog)

    def retranslateUi(self, select_indiv_dialog):
        select_indiv_dialog.setWindowTitle(QtGui.QApplication.translate("select_indiv_dialog", "Select base individual", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("select_indiv_dialog", "Filter:", None, QtGui.QApplication.UnicodeUTF8))

