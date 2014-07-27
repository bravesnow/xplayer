# -*- coding: cp936 -*-
import wx,os,mp3play
'''�Զ���˵�'''
class MyMenu():
    def __init__(self,parent):
        #-----------------------------
        menuBar=wx.MenuBar()#�����˵���
        #-----------------------------
        menu1=wx.Menu()#����һ���˵�      
        menuBar.Append(menu1,"�ļ�(&F)")#���˵������˵���
        self.open=menu1.Append(wx.NewId(),"��(&O)","��һ���ļ�")#�����˵���
        #-----------------------------
        menu2=wx.Menu()
        menuBar.Append(menu2,"�༭(&E)")
        menu2.Append(wx.NewId(),"����","")
        menu2.AppendSeparator()#�˵��ָ���
        #-----------------------------        
        menu3=wx.Menu()
        menuBar.Append(menu3,"����(&H)")
        #-----------------------------
        parent.SetMenuBar(menuBar)#���˵������ڴ��ڿ��   
'''�Զ�����'''
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        #��ʼ��һ�����
        wx.Frame.__init__(self,parent,id,"MyWindow",size=(600,600))
        #����һ���������
        panel=wx.Panel(self,-1)
        panel.SetBackgroundColour('white')
        #�ڻ����ϣ�����һ����ť����        
        self.button_play=wx.Button(panel,label='Play')
        self.button_stop=wx.Button(panel,label='Stop')
        self.button=wx.Button(panel,label='Read')
        self.button_save=wx.Button(panel,label='Save')
        #����״̬��
        statusBar=self.CreateStatusBar()
        #����������
        self.toolBar=self.CreateToolBar()
        self.toolBar_open=self.toolBar.AddSimpleTool(-1,wx.Bitmap('heart.ico'),
                              "open","OPen a new file")                              
        self.toolBar.Realize()
        #�ڻ����ϣ������ı���
        self.textfile=wx.TextCtrl(panel)
        #�ڻ����ϣ������б��        
        datafile=open('data.txt','r')#���ļ��е����ݴ����б����
        self.listBox=wx.ListBox(panel,-1,style=wx.LB_SINGLE)
        for each in datafile.readlines():
            if each!='':
                self.listBox.Append(each)
        datafile.close()
        #�ߴ繹����
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
        
'''�Զ���Ӧ�ó�����'''       
class MyApp(wx.App):
    #��ʼ��Ӧ�ó���
    def OnInit(self):
        #����ʵ����
        self.frame = MyFrame(parent=None,id=-1)#ʵ���������
        self.SetTopWindow(self.frame)#����һ�������
        self.menu=MyMenu(self.frame)#ʵ�����˵���������һ�����
        ##����Ӧ����
        self.Bind(wx.EVT_MENU,self.OpenFileDialog,self.menu.open)#�˵�����Ӧ
        #self.Bind(wx.EVT_BUTTON,self.Play,self.frame.button_play)#��ť��Ӧ
        self.Bind(wx.EVT_BUTTON,self.Stop,self.frame.button_stop)#��ť��Ӧ
        #self.Bind(wx.EVT_BUTTON,self.LoadTxt,self.frame.button)
        #self.Bind(wx.EVT_BUTTON,self.SaveTxt,self.frame.button_save)
        self.Bind(wx.EVT_TOOL,self.OpenFileDialog,self.frame.toolBar_open)
        self.Bind(wx.EVT_LISTBOX_DCLICK,self.Play,self.frame.listBox)
        #��ʾ��ܴ���
        self.frame.Show()    
        return True
    #�¼���Ӧ����
    def Play(self,event):
        #����WAV��Ƶ
        #winsound.PlaySound(self.frame.textfile.GetValue(),winsound.SND_FILENAME)
        #����mp3
        self.mp3file=self.frame.listBox.GetStringSelection()
        self.mp3file=self.mp3file.split("\n")[0]
        #print self.mp3file
        self.mp3=mp3play.load(self.mp3file)
        self.mp3.play()
    def Stop(self,event):
        self.mp3.stop()
    def OpenFileDialog(self,event):
        #���ļ��Ի���
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
        #����һ���Ի���
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
        wx.MessageBox("����ɹ���","��ʾ��",style=wx.OK)
        file.close()'''
    def OnCloseMe(self,event):
        #�ر�Ӧ�ó���
        self.Close(True)
           
if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
