# -*- coding: cp936 -*-
import sys
import mp3play
from PyQt4 import QtCore,QtGui

class MyWindow(QtGui.QWidget):
    def __init__(self,):
        QtGui.QMainWindow.__init__(self)
        self.setWindowTitle('pyqt')#设置窗口标题
        #=====================================================
        gridlayout=QtGui.QGridLayout()#全局布局       
        hboxlayout1=QtGui.QHBoxLayout()#横向布局
        #按钮定义，添加，响应
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
        #列表框定义，添加
        hboxlayout2=QtGui.QHBoxLayout()#横向布局
        #self.textedit=QtGui.QTextEdit()多行文本框
        #hboxlayout2.addWidget(self.textedit)添加多行文本框
        self.list=QtGui.QListWidget(self)
        hboxlayout2.addWidget(self.list)
        #布局组合       
        gridlayout.addLayout(hboxlayout1,0,0)
        gridlayout.addLayout(hboxlayout2,1,0)
        #布局添加
        self.setLayout(gridlayout)
    def onadd(self):
        filename=QtGui.QFileDialog.getOpenFileName(self,'open')#文件对话框
        self.list.addItem(filename)#文件名添加到列表框
    def onplay(self):      
        cur=self.list.currentItem()#取得列表框当前项
        if not cur:
            QtGui.QMessageBox.information(self,"Info",u"请选择一个文件名！")
        else:
            self.mp3file=cur.text()#列表框项转成字符串文本
            self.mp3=mp3play.load(self.mp3file)#载入mp3文件
            self.mp3.play()#mp3播放
            #QtGui.QMessageBox.information(self,"Info",string)
    def onstop(self):
        self.mp3.stop()#mp3暂停
if __name__ == '__main__':
    app=QtGui.QApplication(sys.argv)
    MyWindowob=MyWindow()
    MyWindowob.show()
    app.exec_()

