

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QDialog
    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 252)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setObjectName("btn_start")
        self.gridLayout.addWidget(self.btn_start, 5, 0, 1, 1)

        self.ui_locate = QtWidgets.QPushButton(self.centralwidget)
        self.ui_locate.setAutoFillBackground(False)
        self.ui_locate.setAutoDefault(False)
        self.ui_locate.setDefault(False)
        self.ui_locate.setFlat(False)
        self.ui_locate.setObjectName("ui_locate")

        self.gridLayout.addWidget(self.ui_locate, 1, 0, 1, 2)
        self.ui_path = QtWidgets.QTextBrowser(self.centralwidget)
        self.ui_path.setObjectName("ui_path")
        self.gridLayout.addWidget(self.ui_path, 6, 0, 1, 1)
        self.py_path = QtWidgets.QTextBrowser(self.centralwidget)
        self.py_path.setObjectName("py_path")
        self.gridLayout.addWidget(self.py_path, 7, 0, 1, 1)
        self.py_locate = QtWidgets.QPushButton(self.centralwidget)
        self.py_locate.setObjectName("py_locate")

        self.py_locate.clicked.connect(self.py_location)
        self.ui_locate.clicked.connect(self.ui_location)
        self.btn_start.clicked.connect(self.convert)

        self.gridLayout.addWidget(self.py_locate, 4, 0, 1, 1)
        self.ui_path.raise_()
        self.ui_locate.raise_()
        self.py_path.raise_()
        self.btn_start.raise_()
        self.py_locate.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", ".ui To .py Conversion Tool"))
        self.btn_start.setText(_translate("MainWindow", "Convert"))
        self.ui_locate.setText(_translate("MainWindow", "Locate the .ui file"))
        self.ui_path.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.py_locate.setText(_translate("MainWindow", "Output Location .py"))

    def ui_location(self):
        self.ui_file = QFileDialog.getOpenFileName()[0]
        self.ui_path.setText(self.ui_file)

        
    def py_location(self):
        self.py_file = QFileDialog.getExistingDirectory()
        self.py_path.setText(self.py_file)


            
    def convert(self):
        self.filename = self.ui_file.split("/")[-1]
        self.file_wo_ext = self.filename.split(".")[0]
        self.generated_file = f"{self.py_file}/conv_{self.file_wo_ext}.py"

            


        with open(self.generated_file , "x") as file:
            print("Generated .py file.")
            self.py_path.setText("Success!")
            self.ui_path.setText("Success!")
                        
        os.system(f"cmd /c pyuic5.exe -x {self.ui_file} -o {self.generated_file}")


if __name__ == "__main__":
    import sys
    import os
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
