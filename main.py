# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TX_Maker.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial


import maker
#from tools.tx_maker import maker
#reload(maker)


class Ui_TX_Maker(object):


    def setupUi(self, TX_Maker):
        TX_Maker.setObjectName("TX_Maker")
        TX_Maker.resize(900, 700)
        TX_Maker.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(TX_Maker)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.Out_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Out_pushButton.setObjectName("Out_pushButton")
        self.gridLayout.addWidget(self.Out_pushButton, 3, 3, 1, 1)
        self.Out_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Out_lineEdit.setObjectName("Out_lineEdit")
        self.gridLayout.addWidget(self.Out_lineEdit, 3, 2, 1, 1)
        self.Out_label = QtWidgets.QLabel(self.centralwidget)
        self.Out_label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Out_label.setOpenExternalLinks(True)
        self.Out_label.setObjectName("Out_label")
        self.gridLayout.addWidget(self.Out_label, 3, 1, 1, 1)
        self.Create_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Create_pushButton.setObjectName("Create_pushButton")
        self.gridLayout.addWidget(self.Create_pushButton, 4, 2, 1, 1)
        self.TX_Maker_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.TX_Maker_pushButton.setObjectName("TX_Maker_pushButton")
        self.gridLayout.addWidget(self.TX_Maker_pushButton, 0, 3, 1, 1)
        self.Source_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.Source_lineEdit.setObjectName("Source_lineEdit")
        self.gridLayout.addWidget(self.Source_lineEdit, 1, 2, 1, 1)
        self.Source_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.Source_pushButton.setObjectName("Source_pushButton")
        self.gridLayout.addWidget(self.Source_pushButton, 1, 3, 1, 1)
        self.TX_Maker_label = QtWidgets.QLabel(self.centralwidget)
        self.TX_Maker_label.setObjectName("TX_Maker_label")
        self.gridLayout.addWidget(self.TX_Maker_label, 0, 1, 1, 1)
        self.TX_Maker_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.TX_Maker_lineEdit.setObjectName("TX_Maker_lineEdit")
        self.gridLayout.addWidget(self.TX_Maker_lineEdit, 0, 2, 1, 1)
        self.Source_label = QtWidgets.QLabel(self.centralwidget)
        self.Source_label.setEnabled(True)
        self.Source_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Source_label.setObjectName("Source_label")
        self.gridLayout.addWidget(self.Source_label, 1, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 2, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        TX_Maker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TX_Maker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 924, 21))
        self.menubar.setObjectName("menubar")
        TX_Maker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TX_Maker)
        self.statusbar.setObjectName("statusbar")
        TX_Maker.setStatusBar(self.statusbar)


        self.TX_Maker_pushButton.clicked.connect(partial(self.set_dirname, self.TX_Maker_lineEdit, mode=False))
        self.Source_pushButton.clicked.connect(partial(self.set_dirname, self.Source_lineEdit, mode=False, load=True))
        self.Out_pushButton.clicked.connect(partial(self.set_dirname, self.Out_lineEdit, mode=False, load=True))
        self.Create_pushButton.clicked.connect(self.convert_to_tx)
        QtCore.QMetaObject.connectSlotsByName(TX_Maker)
                
        self.browse_directory = 'D:\Company\_01.Pratice\_python\JS_PIPE'

        self.retranslateUi(TX_Maker)
        self.set_default(TX_Maker)


    def retranslateUi(self, TX_Maker):
        _translate = QtCore.QCoreApplication.translate
        TX_Maker.setWindowTitle(_translate("TX_Maker", "TX_Maker"))
        self.Out_pushButton.setText(_translate("TX_Maker", "..."))
        self.Out_label.setText(_translate("TX_Maker", "<html><head/><body><p align=\"right\">Out</p></body></html>"))
        self.Create_pushButton.setText(_translate("TX_Maker", "Create"))
        self.TX_Maker_pushButton.setText(_translate("TX_Maker", "..."))
        self.Source_pushButton.setText(_translate("TX_Maker", "..."))
        self.TX_Maker_label.setText(_translate("TX_Maker", "<html><head/><body><p align=\"right\">TX_Maker</p></body></html>"))
        self.Source_label.setText(_translate("TX_Maker", "<html><head/><body><p align=\"right\">Source</p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("TX_Maker", "Index"))
        self.treeWidget.headerItem().setText(1, _translate("TX_Maker", "Path"))
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def set_default(self, TX_Maker):
        if 'RMANTREE' in os.environ:
            rmantree = os.environ['RMANTREE']
        else:
            rmantree = 'C:\Program Files\Pixar\RenderManProServer-24.1'
        txmake_path = os.path.join(rmantree, 'bin', 'txmake')
        set_txmake_path =  '\"\"' + txmake_path + '\"\"'
        self.TX_Maker_lineEdit.setText(set_txmake_path)

    def set_dirname(self, widget, mode=False, **kwargs):
        if mode:
            current_path, _ = QtWidgets.QFileDialog.getExistingDirectory(None, 'Browser', self.browse_directory)

        else:
            current_format = 'txmake (*txmake)'
            ###filter="All files (*)"
            current_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Browser', self.browse_directory)
            set_current_path =  '\"\"' + current_path + '\"\"'

        widget.setText(set_current_path)
        self.browse_directory = current_path
        
        if 'load' in kwargs:
            self.load_source_images(source_dirname=current_path)

    def load_source_images(self, source_dirname=None):
        if not source_dirname:
            source_dirname = self.Source_lineEdit.text()
        if not source_dirname:
            return
        if isinstance(source_dirname, QtCore.QStringListModel):
            source_dirname = str(source_dirname)
        if not os.path.isdir(source_dirname):
            return
        self.browse_directory = source_dirname
        self.treeWidget.clear()
        contents = os.listdir(source_dirname)
        index = 1
            
        for content in contents:
            name, format = os.path.splitext(content)
            if format.upper() not in maker.IMAGE_FORMATS:
                continue

            image_path = os.path.join(source_dirname, content)
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0, str(index))
            item.setText(1, image_path)
            item.setCheckState(1, QtCore.Qt.Checked)
            index+=1

    def convert_to_tx(self):
        txmake = str(self.TX_Maker_lineEdit.text())
        source_dirname = str(self.Source_lineEdit.text)
        output_diranme = str(self.Out_lineEdit.text())
        output_diranme_cv = (output_diranme.replace('"', ''))
        message = None
    #    if not os.path.isdir(source_dirname):
    #        message = 'not found source directory'
    #    if not os.path.isdir(output_diranme):
    #        message = 'not found out put directroy'

        widget_item = self.treeWidget.invisibleRootItem() 

        source_images = []
        for index in range(widget_item.childCount()):
            item = widget_item.child(index)
            if not item.checkState(1):
                continue
            source_images.append(str(item.text(1)))
        
        if not source_images:
            message = 'not found items'

        if message:
            QtWidgets.QMessageBox.warning(None, 'Warning', message, QtWidgets.QMessageBox.Ok)
            return
        

        maker.converts(txmake, source_images, output_diranme_cv)


        QtWidgets.QMessageBox.information(None, 'Sucess', 'done!...', QtWidgets.QMessageBox.Ok)
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    TX_Maker = QtWidgets.QMainWindow()
    ui = Ui_TX_Maker()
    ui.setupUi(TX_Maker)
    TX_Maker.show()
    sys.exit(app.exec_())



