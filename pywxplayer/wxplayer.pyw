# -*- coding: cp936 -*-
import wx,os,mp3play
'''自定义菜单'''
class MyMenu():
    def __init__(self,parent):
        #-----------------------------
        menuBar=wx.MenuBar()#创建菜单栏
        #-----------------------------
        menu1=wx.Menu()#创建一个菜单      
        menuBar.Append(menu1,"文件(&F)")#将菜单附到菜单栏
        self.open=menu1.Append(wx.NewId(),"打开(&O)","打开一个文件")#创建菜单项
        #-----------------------------
        menu2=wx.Menu()
        menuBar.Append(menu2,"编辑(&E)")
        menu2.Append(wx.NewId(),"复制","")
        menu2.AppendSeparator()#菜单分隔符
        #-----------------------------        
        menu3=wx.Menu()
        menuBar.Append(menu3,"帮助(&H)")
        #-----------------------------
        parent.SetMenuBar(menuBar)#将菜单栏附于窗口框架   
'''自定义框架'''
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        #初始化一个框架
        wx.Frame.__init__(self,parent,id,"MyWindow",size=(600,600))
        #构造一个画板对象
        panel=wx.Panel(self,-1)
        panel.SetBackgroundColour('white')
        #在画板上，构造一个按钮对象        
        self.button_play=wx.Button(panel,label='Play')
        self.button_stop=wx.Button(panel,label='Stop')
        self.button=wx.Button(panel,label='Read')
        self.button_save=wx.Button(panel,label='Save')
        #创建状态栏
        statusBar=self.CreateStatusBar()
        #创建工具栏
        self.toolBar=self.CreateToolBar()
        self.toolBar_open=self.toolBar.AddSimpleTool(-1,wx.Bitmap('heart.ico'),
                              "open","OPen a new file")                              
        self.toolBar.Realize()
        #在画板上，构造文本框
        self.textfile=wx.TextCtrl(panel)
        #在画板上，构造列表框        
        datafile=open('data.txt','r')#将文件中的数据存入列表框中
        self.listBox=wx.ListBox(panel,-1,style=wx.LB_SINGLE)
        for each in datafile.readlines():
            if each!='':
                self.listBox.Append(each)
        datafile.close()
        #尺寸构造器
        hbox=wx.BoxSizer()
        hbox.Add(self.textfile,proportion=1,flag=wx.EXPAND)
        hbox.Add(self.button_play,proportion=0,flag=wx.LEFT,border=5)
        hbox.Add(self.button_stop,proportion=0,flag=wx.LEFT,border=5)
        hbox.Add(self.button,proportion=0,flag=wx.LEFT,border=5)
        hbox.Add(self.button_save,proportion=0,flag=wx.LEFT,border=5)
        vbox=wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
        vbox.Add(self.listBox,proportion=1,
                 flag=wx.EXPAND|wx.BOTTOM|wx.RIGHT,border=5)
        panel.SetSizer(vbox)
        
'''自定义应用程序类'''       
class MyApp(wx.App):
    #初始化应用程序
    def OnInit(self):
        #对象实例化
        self.frame = MyFrame(parent=None,id=-1)#实例化框架类
        self.SetTopWindow(self.frame)#设置一个主框架
        self.menu=MyMenu(self.frame)#实例化菜单栏，附于一个框架
        ##绑定响应函数
        self.Bind(wx.EVT_MENU,self.OpenFileDialog,self.menu.open)#菜单项响应
        #self.Bind(wx.EVT_BUTTON,self.Play,self.frame.button_play)#按钮响应
        self.Bind(wx.EVT_BUTTON,self.Stop,self.frame.button_stop)#按钮响应
        #self.Bind(wx.EVT_BUTTON,self.LoadTxt,self.frame.button)
        #self.Bind(wx.EVT_BUTTON,self.SaveTxt,self.frame.button_save)
        self.Bind(wx.EVT_TOOL,self.OpenFileDialog,self.frame.toolBar_open)
        self.Bind(wx.EVT_LISTBOX_DCLICK,self.Play,self.frame.listBox)
        #显示框架窗口
        self.frame.Show()    
        return True
    #事件响应函数
    def Play(self,event):
        #播放WAV音频
        #winsound.PlaySound(self.frame.textfile.GetValue(),winsound.SND_FILENAME)
        #播放mp3
        self.mp3file=self.frame.listBox.GetStringSelection()
        self.mp3file=self.mp3file.split("\n")[0]
        #print self.mp3file
        self.mp3=mp3play.load(self.mp3file)
        self.mp3.play()
    def Stop(self,event):
        self.mp3.stop()
    def OpenFileDialog(self,event):
        #打开文件对话框
        wildcard = "All files (*.*)|*.*"
        fileDialog=wx.FileDialog(None,"choose",os.getcwd(),"",wildcard,wx.OPEN)
        if fileDialog.ShowModal()==wx.ID_OK:            
            self.frame.textfile.SetValue(fileDialog.GetPath())
        filepath=fileDialog.GetPath()
        #filename=filepath.split("\\")[-1]
        self.frame.listBox.Append(filepath)
        datafile=open('data.txt','a+')
        datafile.write(filepath)
        datafile.write('\n')
        fileDialog.Destroy()
        datafile.close()
    def OpenDialog(self,event):
        #弹出一个对话框
        dlg=wx.MessageDialog(self,"Is this","test",wx.YES_NO)
        ret=dlg.ShowModal()
        dlg.Destroy()
    '''def LoadTxt(self,event):
        file=open(self.frame.textfile.GetValue())
        self.frame.textcontent.SetValue(file.read())
        file.close()'''
    '''def SaveTxt(self,event):
        file=open(self.frame.textfile.GetValue(),'w')
        file.write(self.frame.textcontent.GetValue())
        wx.MessageBox("保存成功！","提示：",style=wx.OK)
        file.close()'''
    def OnCloseMe(self,event):
        #关闭应用程序
        self.Close(True)
           
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
