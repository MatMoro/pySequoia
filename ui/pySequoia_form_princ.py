# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pySequoia.ui'
#
# Created: Sat Sep 21 12:17:44 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(661, 470)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/sequoia2.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.openButton = QtGui.QPushButton(self.centralwidget)
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.horizontalLayout.addWidget(self.openButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.typeArbre_ascendant = QtGui.QRadioButton(self.groupBox)
        self.typeArbre_ascendant.setGeometry(QtCore.QRect(20, 30, 97, 21))
        self.typeArbre_ascendant.setChecked(True)
        self.typeArbre_ascendant.setObjectName(_fromUtf8("typeArbre_ascendant"))
        self.typeArbre_descendant = QtGui.QRadioButton(self.groupBox)
        self.typeArbre_descendant.setGeometry(QtCore.QRect(20, 50, 97, 21))
        self.typeArbre_descendant.setObjectName(_fromUtf8("typeArbre_descendant"))
        self.horizontalLayout_6.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.orientation_portrait = QtGui.QRadioButton(self.groupBox_2)
        self.orientation_portrait.setChecked(True)
        self.orientation_portrait.setObjectName(_fromUtf8("orientation_portrait"))
        self.verticalLayout_3.addWidget(self.orientation_portrait)
        self.orientation_paysage = QtGui.QRadioButton(self.groupBox_2)
        self.orientation_paysage.setObjectName(_fromUtf8("orientation_paysage"))
        self.verticalLayout_3.addWidget(self.orientation_paysage)
        self.horizontalLayout_6.addWidget(self.groupBox_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.encodage = QtGui.QComboBox(self.centralwidget)
        self.encodage.setObjectName(_fromUtf8("encodage"))
        self.encodage.addItem(_fromUtf8(""))
        self.encodage.addItem(_fromUtf8(""))
        self.horizontalLayout_5.addWidget(self.encodage)
        self.button_reload_file = QtGui.QPushButton(self.centralwidget)
        self.button_reload_file.setEnabled(False)
        self.button_reload_file.setObjectName(_fromUtf8("button_reload_file"))
        self.horizontalLayout_5.addWidget(self.button_reload_file)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.inclure_images = QtGui.QCheckBox(self.centralwidget)
        self.inclure_images.setObjectName(_fromUtf8("inclure_images"))
        self.verticalLayout.addWidget(self.inclure_images)
        self.creer_index = QtGui.QCheckBox(self.centralwidget)
        self.creer_index.setEnabled(True)
        self.creer_index.setObjectName(_fromUtf8("creer_index"))
        self.verticalLayout.addWidget(self.creer_index)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.nb_generations = QtGui.QSpinBox(self.centralwidget)
        self.nb_generations.setMinimum(1)
        self.nb_generations.setMaximum(50)
        self.nb_generations.setProperty("value", 10)
        self.nb_generations.setObjectName(_fromUtf8("nb_generations"))
        self.horizontalLayout_2.addWidget(self.nb_generations)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_3.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(517, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.buttonBox = QtGui.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setEnabled(False)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout_2.addWidget(self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 661, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionA_propos_de_pySequoia = QtGui.QAction(MainWindow)
        self.actionA_propos_de_pySequoia.setObjectName(_fromUtf8("actionA_propos_de_pySequoia"))
        self.menuOptions.addAction(self.actionPreferences)
        self.menuOptions.addAction(self.actionA_propos_de_pySequoia)
        self.menubar.addAction(self.menuOptions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "pySequoia", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Fichier Gedcom", None, QtGui.QApplication.UnicodeUTF8))
        self.openButton.setText(QtGui.QApplication.translate("MainWindow", "Rechercher...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Type d\'arbre", None, QtGui.QApplication.UnicodeUTF8))
        self.typeArbre_ascendant.setText(QtGui.QApplication.translate("MainWindow", "Ascendant", None, QtGui.QApplication.UnicodeUTF8))
        self.typeArbre_descendant.setText(QtGui.QApplication.translate("MainWindow", "Descendant", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Orientation", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation_portrait.setText(QtGui.QApplication.translate("MainWindow", "Portrait", None, QtGui.QApplication.UnicodeUTF8))
        self.orientation_paysage.setText(QtGui.QApplication.translate("MainWindow", "Paysage", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Encodage", None, QtGui.QApplication.UnicodeUTF8))
        self.encodage.setItemText(0, QtGui.QApplication.translate("MainWindow", "UTF-8", None, QtGui.QApplication.UnicodeUTF8))
        self.encodage.setItemText(1, QtGui.QApplication.translate("MainWindow", "Latin1", None, QtGui.QApplication.UnicodeUTF8))
        self.button_reload_file.setText(QtGui.QApplication.translate("MainWindow", "Recharger le fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.inclure_images.setText(QtGui.QApplication.translate("MainWindow", "Inclure les images", None, QtGui.QApplication.UnicodeUTF8))
        self.creer_index.setText(QtGui.QApplication.translate("MainWindow", "Créer un index", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Nombre de générations", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Enregistrer le PDF sous", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("MainWindow", "Rechercher...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Personne à la base", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Sélectionner...", None, QtGui.QApplication.UnicodeUTF8))
        self.menuOptions.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreferences.setText(QtGui.QApplication.translate("MainWindow", "Préférences...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionA_propos_de_pySequoia.setText(QtGui.QApplication.translate("MainWindow", "A propos de pySequoia...", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
