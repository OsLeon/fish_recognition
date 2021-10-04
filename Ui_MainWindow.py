# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/leon/Project/fish_demo_client/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import cv2
import os
import paddlex as pdx
import sys

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_yuce = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_yuce.setGeometry(QtCore.QRect(140, 400, 81, 26))
        self.pushButton_yuce.setObjectName("pushButton_yuce")
        self.pushButton_jiance = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_jiance.setGeometry(QtCore.QRect(140, 450, 81, 26))
        self.pushButton_jiance.setObjectName("pushButton_jiance")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(310, 20, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_yuantu = QtWidgets.QLabel(self.centralwidget)
        self.label_yuantu.setGeometry(QtCore.QRect(170, 110, 31, 16))
        self.label_yuantu.setObjectName("label_yuantu")
        self.label_yucetu = QtWidgets.QLabel(self.centralwidget)
        self.label_yucetu.setGeometry(QtCore.QRect(580, 100, 41, 16))
        self.label_yucetu.setObjectName("label_yucetu")
        self.label_jieguo = QtWidgets.QLabel(self.centralwidget)
        self.label_jieguo.setGeometry(QtCore.QRect(460, 420, 61, 16))
        self.label_jieguo.setObjectName("label_jieguo")
        self.textBrowser_jieguo = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_jieguo.setGeometry(QtCore.QRect(530, 410, 141, 41))
        self.textBrowser_jieguo.setObjectName("textBrowser_jieguo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(380, 90, 20, 451))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 370, 781, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(60, 140, 261, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(50, 150, 20, 191))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(60, 330, 261, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(310, 150, 20, 191))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(730, 150, 20, 191))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(480, 140, 261, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(470, 150, 20, 191))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(480, 330, 261, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_show1 = QtWidgets.QLabel(self.centralwidget)
        self.label_show1.setGeometry(QtCore.QRect(70, 150, 251, 181))
        self.label_show1.setText("")
        self.label_show1.setObjectName("label_show1")
        self.label_show2 = QtWidgets.QLabel(self.centralwidget)
        self.label_show2.setGeometry(QtCore.QRect(480, 150, 251, 181))
        self.label_show2.setText("")
        self.label_show2.setObjectName("label_show2")
#        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
#        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
#        MainWindow.setStatusBar(self.statusbar)


        self.pushButton_yuce.clicked.connect(self.prediction)
        self.pushButton_jiance.clicked.connect(self.prediction_seg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_yuce.setText(_translate("MainWindow", "目标预测"))
        self.pushButton_jiance.setText(_translate("MainWindow", "目标检测"))
        self.label_title.setText(_translate("MainWindow", "海洋鱼类识别系统"))
        self.label_yuantu.setText(_translate("MainWindow", "原图"))
        self.label_yucetu.setText(_translate("MainWindow", "预测图"))
        self.label_jieguo.setText(_translate("MainWindow", "预测结果"))


    def prediction(self):
        imgName,imgtype= QFileDialog.getOpenFileName(self,"打开图片","","*.png;;*.jpg;;All Files(*)")
        jpg = QtGui.QPixmap(imgName).scaled(self.label_show1.width(),self.label_show1.height())       
        self.label_show1.setPixmap(jpg)
        model = pdx.load_model('./inference_model')
        result = model.predict(imgName)
        result_categroy = result[0]["category"]
        self.textBrowser_jieguo.setText(result_categroy)

    def prediction_seg(self):
        
        imgName,imgtype= QFileDialog.getOpenFileName(self,"打开图片","","*.png;;*.jpg;;All Files(*)")
        file_name = os.path.split(imgName)[1].split('.')[0]
        model = pdx.deploy.Predictor('./inference_model_seg')
        label = model.predict(imgName)['label_map']
        label = label * 255
#        label = label.astype(np.int)
        cv2.imwrite(f'./tmp/mask/{file_name}.png', label,
                    (cv2.IMWRITE_PNG_COMPRESSION, 0))
        image = cv2.imread(f'./tmp/image/{file_name}.png')
        mask = cv2.imread(f'./tmp/mask/{file_name}.png', 0)
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 2)
        cv2.imwrite(f'./tmp/draw/{file_name}.png',image)

        img_path = f'./tmp/draw/{file_name}.png'
        jpg2 = QtGui.QPixmap(img_path).scaled(self.label_show2.width(),self.label_show2.height())       
        self.label_show2.setPixmap(jpg2)
  
if __name__ == '__main__':
    #创建应用程序和对象
    app = QApplication(sys.argv)
    Window = QtWidgets.QWidget()
    ex = Ui_MainWindow()
    ex.setupUi(Window)
    Window.show()
    sys.exit(app.exec_()) 