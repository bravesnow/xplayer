# -*- coding: cp936 -*-
import sys
import mp3play
from PyQt4 import QtCore,QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self,):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('pyqt')#���ô��ڱ���
        #=====================================================
        gridlayout=QtGui.QGridLayout()#ȫ�ֲ���       
        hboxlayout1=QtGui.QHBoxLayout()#���򲼾�
        #��ť���壬��ӣ���Ӧ
        self.button_add=QtGui.QPushButton('add')
        self.connect(self.button_add,QtCore.SIGNAL('clicked()'),self.onadd)
        self.button_play=QtGui.QPushButton('play')
        self.connect(self.button_play,QtCore.SIGNAL('clicked()'),self.onplay)
        self.button_stop=QtGui.QPushButton('stop')
        self.connect(self.button_stop,QtCore.SIGNAL('clicked()'),self.onstop)
        self.button_read=QtGui.QPushButton('read')
        self.button_save=QtGui.QPushButton('save')
        hboxlayout1.addWidget(self.button_add)
        hboxlayout1.addWidget(self.button_play)
        hboxlayout1.addWidget(self.button_stop)
        hboxlayout1.addWidget(self.button_read)
        hboxlayout1.addWidget(self.button_save)
        #�б���壬���
        hboxlayout2=QtGui.QHBoxLayout()#���򲼾�
        #self.textedit=QtGui.QTextEdit()�����ı���
        #hboxlayout2.addWidget(self.textedit)��Ӷ����ı���
        self.list=QtGui.QListWidget(self)
        hboxlayout2.addWidget(self.list)
        #�������       
        gridlayout.addLayout(hboxlayout1,0,0)
        gridlayout.addLayout(hboxlayout2,1,0)
        #�������
        self.setLayout(gridlayout)
    def onadd(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,'open')#�ļ��Ի���
        self.list.addItem(filename)#�ļ�����ӵ��б��
    def onplay(self):      
        cur=self.list.currentItem()#ȡ���б��ǰ��
        if not cur:
            QtGui.QMessageBox.information(self,"Info",u"��ѡ��һ���ļ�����")
        else:
            self.mp3file=cur.text()#�б����ת���ַ����ı�
            self.mp3=mp3play.load(self.mp3file)#����mp3�ļ�
            self.mp3.play()#mp3����
            #QtGui.QMessageBox.information(self,"Info",string)
    def onstop(self):
        self.mp3.stop()#mp3��ͣ
if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    MyWindowob=MyWindow()
    MyWindowob.show()
    app.exec_()

