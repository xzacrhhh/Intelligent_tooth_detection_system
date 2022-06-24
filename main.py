from re import I
import time
import os

from PIL import Image, ImageQt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
import cv2
import sys
import numpy as np
from PyQt5.QtWidgets import *

from yolo import YOLO
from PIL import Image
from classification import Classification

classfication = Classification()
from yolo import YOLO
if __name__ == "__main__":
    yolo = YOLO()

'''单张图片检测'''
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        self.str_name = '0'
        # self.my_model=my_lodelmodel()
        self.resize(1600, 900)
        self.setWindowIcon(QIcon(os.getcwd() + '\\data\\source_image\\Detective.ico'))
        self.setWindowTitle("智能检牙系统")



        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(
            QtGui.QPixmap(os.getcwd() + '\\img\\7.jpg')))
        self.setPalette(window_pale)

        self.label1 = QLabel(self)
        self.label1.setText("   待检测图片")
        self.label1.setFixedSize(700, 500)
        self.label1.move(110, 80)

        self.label1.setStyleSheet("QLabel{background:#ffffff;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                  )
        self.label2 = QLabel(self)
        self.label2.setText("   检测结果")
        self.label2.setFixedSize(700, 500)
        self.label2.move(850, 80)

        self.label2.setStyleSheet("QLabel{background:#ffffff;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}"
                                  )

        self.label3 = QLabel(self)
        self.label3.setText("")
        self.label3.move(1200, 620)
        self.label3.setStyleSheet("font-size:20px;")
        self.label3.adjustSize()



        btn = QPushButton(self)
        btn.setText("打开图片")
        btn.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn.move(10, 30)
        btn.clicked.connect(self.openimage)

        btn1 = QPushButton(self)
        btn1.setText("检测图片")
        btn1.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn1.move(10, 80)
        # print("QPushButton构建")
        btn1.clicked.connect(self.button1_test)

        btn2 = QPushButton(self)
        btn2.setText("识别图片")
        btn2.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn2.move(10, 120)
        # print("QPushButton构建")
        btn2.clicked.connect(self.button2_test)

        btn3 = QPushButton(self)
        btn3.setText("实时检测")
        btn3.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        btn3.move(10, 160)
        # print("QPushButton构建")
        btn3.clicked.connect(self.vedio)

    def openimage(self):

        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")

        if imgName!='':
            self.imgname1=imgName
            # print("imgName",imgName,type(imgName))
            im0=cv2.imread(imgName)

            width = im0.shape[1]
            height = im0.shape[0]

            # 设置新的图片分辨率框架
            width_new = 700
            height_new = 500

            # 判断图片的长宽比率
            if width / height >= width_new / height_new:

                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:

                show = cv2.resize(im0, (int(width * height_new / height), height_new))

            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))

            # jpg = QtGui.QPixmap(imgName).scaled(self.label1.width(), self.label1.height())
            # self.label1.setPixmap(jpg)


    def button1_test(self):
        QApplication.processEvents()

        img=Image.open(self.imgname1)
        img=yolo.detect_image(img)

        width = img.width

        height = img.height
            # 设置新的图片分辨率框架
        width_new = 700
        height_new = 500

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = img.resize((width_new, int(height * width_new / width)))
        else:

            show = img.resize((int(width * height_new / height), height_new))
        im0 = np.asarray(show)
        showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
        self.label2.setPixmap(QtGui.QPixmap.fromImage(showImage))


    def button2_test(self):
        QApplication.processEvents()

        img=Image.open(self.imgname1)
        img=classfication.detect_image(img)

        width = img.width

        height = img.height
            # 设置新的图片分辨率框架
        width_new = 700
        height_new = 500

        # 判断图片的长宽比率
        if width / height >= width_new / height_new:

            show = img.resize((width_new, int(height * width_new / width)))
        else:

            show = img.resize((int(width * height_new / height), height_new))
        im0 = np.asarray(show)
        showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
        self.label2.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def vedio(self):
        global mode
        global video_path
        global video_path
        global video_fps
        mode = "video"
        video_path      = 0
        video_save_path = ""
        video_fps       = 25.0
        if mode == "video":
            capture=cv2.VideoCapture(video_path)
            if video_save_path!="":
                fourcc = cv2.VideoWriter_fourcc(*'XVID')
                size = (int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
                out = cv2.VideoWriter(video_save_path, fourcc, video_fps, size)   
        fps = 0.0
        while(True):
            t1 = time.time()
            # 读取某一帧
            ref,frame=capture.read()
            # 格式转变，BGRtoRGB
            frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            # 转变成Image
            frame = Image.fromarray(np.uint8(frame))
            # 进行检测
            frame = np.array(yolo.detect_image(frame))
            # RGBtoBGR满足opencv显示格式
            frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            
            fps  = ( fps + (1./(time.time()-t1)) ) / 2
            print("fps= %.2f"%(fps))
            frame = cv2.putText(frame, "fps= %.2f"%(fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.imshow("video",frame)
            c= cv2.waitKey(1) & 0xff 
            if video_save_path!="":
                out.write(frame)
            if c==27:
                capture.release()
                break
        capture.release()
        out.release()
        cv2.destroyAllWindows()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap("D:\Dental_examination_treasure\pyqt\1.jpg"))
    # 设置画面中的文字的字体
    splash.setFont(QFont('Microsoft YaHei UI', 12))
    # 显示画面
    splash.show()
    # 显示信息
    splash.showMessage("程序初始化中... 0%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    time.sleep(0.3)


    splash.showMessage("正在加载模型配置文件...60%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    # cam_t=Ui_MainWindow()
    splash.showMessage("正在加载模型配置文件...100%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)


    ui_p = picture()
    ui_p.show()
    splash.close()


    sys.exit(app.exec_())