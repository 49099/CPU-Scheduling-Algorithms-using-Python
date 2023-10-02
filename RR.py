# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RR.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
import matplotlib.pyplot as plt
import numpy as np

burstTime = []
BTProcess = 0
TQuantam = 0



class Ui_RR(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(-10, 40, 791, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 201, 51))
        self.label_3.setObjectName("label_3")
        self.Process_inp = QtWidgets.QTextEdit(self.centralwidget)
        self.Process_inp.setGeometry(QtCore.QRect(330, 90, 341, 51))
        self.Process_inp.setObjectName("Process_inp")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 200, 201, 21))
        self.label_4.setObjectName("label_4")
        self.Calc_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Calc_Btn.setGeometry(QtCore.QRect(400, 290, 111, 41))
        self.Calc_Btn.setObjectName("Calc_Btn")
        self.Calc_Btn.clicked.connect(self.calc_RR)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 230, 221, 51))
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 360, 791, 51))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(14)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 320, 1031, 51))
        self.label_6.setObjectName("label_6")
        self.Process_TAT = QtWidgets.QTextEdit(self.centralwidget)
        self.Process_TAT.setGeometry(QtCore.QRect(330, 490, 341, 51))
        self.Process_TAT.setObjectName("Process_TAT")
        self.Process_TAT.setReadOnly(True)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 61))
        font = QtGui.QFont()
        font.setFamily("Umpush")
        font.setPointSize(12)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(90, 480, 201, 51))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(130, 410, 191, 51))
        self.label_8.setObjectName("label_8")
        self.Process_BT_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Process_BT_2.setGeometry(QtCore.QRect(330, 230, 341, 51))
        self.Process_BT_2.setObjectName("Process_BT_2")
        self.Process_BT = QtWidgets.QTextEdit(self.centralwidget)
        self.Process_BT.setGeometry(QtCore.QRect(330, 160, 341, 51))
        self.Process_BT.setObjectName("Process_BT")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(120, 270, 201, 21))
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 191, 51))
        self.label_2.setObjectName("label_2")
        self.Process_WT = QtWidgets.QTextEdit(self.centralwidget)
        self.Process_WT.setGeometry(QtCore.QRect(330, 410, 341, 51))
        self.Process_WT.setObjectName("Process_WT")
        self.Process_WT.setReadOnly(True)
        self.Calc_Btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Calc_Btn_2.setGeometry(QtCore.QRect(260, 290, 111, 41))
        self.Calc_Btn_2.setObjectName("Calc_Btn_2")
        #self.Calc_Btn_2.clicked.connect(self.open_main_info)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Round-Robin"))
        self.label_9.setText(_translate("MainWindow", "INPUT"))
        self.label_3.setText(_translate("MainWindow", "Burst Time For Each Process"))
        self.label_4.setText(_translate("MainWindow", "(Separated by Space)"))
        self.Calc_Btn.setText(_translate("MainWindow", "Calculate"))
        self.label_10.setText(_translate("MainWindow", "Time Quantam"))
        self.label_5.setText(_translate("MainWindow", "OUTPUT"))
        self.label_6.setText(_translate("MainWindow", "_____________________________________________________________________________________________________________"))
        self.label.setText(_translate("MainWindow", "Please Enter The Process Details Below to Calculate Average Waiting and Turn-Around Times"))
        self.label_7.setText(_translate("MainWindow", "Average Turn-Around Time"))
        self.label_8.setText(_translate("MainWindow", "Average Waiting Time"))
        self.label_2.setText(_translate("MainWindow", "Number of Processes"))
        self.Calc_Btn_2.setText(_translate("MainWindow", "Back"))
    


    def calc_RR(self):
        Twt = 0.0
        Wt = []
        TTat = 0.0
        Tat=[]
        aTat = []

        BTVal = self.Process_BT.toPlainText()
        self.TQuantam = int(self.Process_BT_2.toPlainText())
        self.BTProcess = self.Process_inp.toPlainText()

        ValSplit = BTVal.split()
    
        if(int(self.BTProcess)<len(ValSplit) or int(self.BTProcess)>len(ValSplit)):
            msg2 = QMessageBox()
            msg2.setIcon(2)
            msg2.setInformativeText("Enter Same Number of Process and BT Values.")
            msg2.setWindowTitle("Error")
            msg2.exec_()
        elif(self.BTProcess.isspace()):
            print("Remove Spaces from the Process Number. ")
        else:
            for i in ValSplit:
                burstTime.append(int(i))
            
            rem_bt = list(burstTime)
            t = 0 # Current time  
            while(1): 
                done = True
                for i in range(int(self.BTProcess) ): 
                    if (int(rem_bt[i]) > 0) : 
                        done = False # There is a pending process 
                        if (int(rem_bt[i]) > self.TQuantam) : 
                            t += self.TQuantam  
                            rem_bt[i] =int(rem_bt[i])- self.TQuantam  
                        else: 
                            t = t + int(rem_bt[i])  
                            Wt.append(t - int(burstTime[i]))  
                            rem_bt[i] = 0                
                if (done == True): 
                    break
            for i in range(int(self.BTProcess)):
                Twt = int(Twt) + int(Wt[i])
            for i in range(int(self.BTProcess)): 
                TTat = int(TTat) + int(Wt[i]) + int(burstTime[i])

            self.Process_WT.setPlainText("Total Waiting Time: "+str(Twt))
            self.Process_WT.append("Average Waiting Time: "+str(Twt/int(self.BTProcess)))
            self.Process_TAT.setPlainText("Total Turnaround Time: "+str(TTat))
            self.Process_TAT.append("Average Turnaround Time: "+str(TTat/int(self.BTProcess)))
            Tat = []
            Twt = []
            FTat = []
            msg = QMessageBox()
            msg.setIcon(2)
            msg.setInformativeText("Press OK to Show Gantt Chart")
            msg.setWindowTitle("Prompt")

            buttonoptionA = msg.addButton("Show", QMessageBox.YesRole)
            buttonoptionB = msg.addButton("Close", QMessageBox.NoRole)

            msg.setDefaultButton(buttonoptionA)   
            msg.exec_()

            if msg.clickedButton() == buttonoptionA:
                self.ganttChart()
                self.Process_BT.setText(" ")
                self.Process_inp.setText(" ")
                self.Process_BT_2.setText(" ")
                self.BTProcess = 0
                self.BurstTime = []
            elif msg.clickedButton() == buttonoptionB:
                self


    def ganttChart(self):
        #burstTime.list(self.data)
        fig,gnt = plt.subplots()
        gnt.set_ylim(0, 50)
        gnt.set_xlim(0, 40)
        gnt.set_xlabel("Process Time")
        gnt.set_title = "Shortest Job First Gantt Chart"
        j=0
        k=5
        x=0
        p=1
        pName = ""
        for i in range(int(self.BTProcess)):
            pName = ("P"+str(i))
            colors = np.random.rand(i+1,3)
            gnt.broken_barh([(x,int(burstTime[i]))], (j, k), facecolors = colors)
            x=x+int(burstTime[i])
            j=j+k
            gnt.annotate(pName, xy =(5, 0),xytext =(p,p),size=15)
            p+=5
        plt.savefig("ganttFCFS.png")
        plt.show()

    # def open_main_info(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Ui_MainWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
