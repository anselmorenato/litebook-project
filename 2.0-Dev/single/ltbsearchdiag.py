#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Mon Aug 13 11:10:41 2012
import sys
import wx
from wx.lib.mixins.listctrl import CheckListCtrlMixin
import thread
import wx.lib.newevent
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import xmlrpclib
import traceback
import cPickle
import base64
import platform
import os

(SearchReportEvent,EVT_SRE)=wx.lib.newevent.NewEvent()

# begin wxGlade: extracode
# end wxGlade

report_rpc_path='/REPORT'
report_port=50202

MYOS = platform.system()
def cur_file_dir():
    #获取脚本路径
    global MYOS
    if MYOS == 'Linux':
        path = sys.path[0]
    elif MYOS == 'Windows':
        return os.path.dirname(os.path.abspath(sys.argv[0]))
    else:
        if sys.argv[0].find('/') != -1:
            path = sys.argv[0]
        else:
            path = sys.path[0]
    if isinstance(path,str):
        path=path.decode('utf-8')

    #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是编译后的文件，则返回的是编译后的文件路径
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


class XMLRPCRequestHandler(SimpleXMLRPCRequestHandler):
    global report_rpc_path
    rpc_paths = (report_rpc_path,)


class ReportSVRThread():
    global report_port
    """
    A XML RPC svr for receiving LTBNET search result
    """

    def __init__(self,win):
        self.win=win
##        self.running=True
        self.port = report_port
        self.server = SimpleXMLRPCServer(("localhost", self.port),
                            logRequests=False,
                            requestHandler=XMLRPCRequestHandler)
        self.server.register_introspection_functions()
        self.server.register_function(self.report)
        thread.start_new_thread(self.run,())

##    def stop(self):
##        self.running=False

    def report(self,search_results):
        sr=cPickle.loads(base64.b16decode(search_results))
        evt=SearchReportEvent(result=sr)
        try:
            wx.PostEvent(self.win, evt)
        except Exception, inst:
            print "LTBSearchDiag: catched except:"
            print traceback.format_exc()
            print inst

        return 'ok'

    def run(self):
        self.server.serve_forever()

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, style=wx.LC_REPORT)
        CheckListCtrlMixin.__init__(self)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnItemActivated)
        self.InsertColumn(0, u"文件名",width=150)
        self.InsertColumn(1, u"书名",width=150)
        self.InsertColumn(2, u"作者")
        self.InsertColumn(3, u"URL",width=300)
        self.InsertColumn(4, u"大小")


    def addResult(self,r):
        index = self.InsertStringItem(sys.maxint, r['rdata'])
        self.SetStringItem(index, 3, r['rloc'])
        try:
            self.SetStringItem(index, 1, r['meta_list']['title'])
            self.SetStringItem(index, 2, r['meta_list']['creator'])
            self.SetStringItem(index, 4, r['meta_list']['size'])
        except:
            pass

    def OnItemActivated(self, evt):
        self.ToggleItem(evt.m_itemIndex)


    # this is called by the base class when an item is checked/unchecked
    def OnCheckItem(self, index, flag):
        data = self.GetItemData(index)


    def GetAllChecked(self):
        """
        Get all checked items
        """
        nextid = -1
        rlist=[]
        while True:
            nextid = self.GetNextItem(nextid)
            if nextid == -1: break
            if self.IsChecked(nextid)==True:
                r={'filename':self.GetItem(nextid,0).GetText(),
                    'novelname':self.GetItem(nextid,1).GetText(),
                    'author':self.GetItem(nextid,2).GetText(),
                    'url':self.GetItem(nextid,3).GetText(),
                    'size':self.GetItem(nextid,4).GetText(),
                   }
                rlist.append(r)
        return rlist




class LTBSearchDiag(wx.Frame):
    def __init__(self, parent,downloadFunc=None,kadp_url=None):
        """
        downloadFunc is a function to add download task
        kadp_url is a url of KADP XMLRPC control server
        """
        # begin wxGlade: LTBSearchDiag.__init__
        wx.Frame.__init__(self, parent,-1)
        self.sizer_3_staticbox = wx.StaticBox(self, -1, u"搜索结果")
        self.sizer_2_staticbox = wx.StaticBox(self, -1, u"输入")
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)
        self.label_1 = wx.StaticText(self, -1, u"搜索关键词：")
        self.text_ctrl_1 = wx.TextCtrl(self, -1, "",style=wx.TE_PROCESS_ENTER)
        self.list_ctrl_1 = CheckListCtrl(self)
        self.downloadFunc=downloadFunc
        self.ongoing_kw = 0

##        index = self.list_ctrl_1.InsertStringItem(sys.maxint,u'小说1')
##        self.list_ctrl_1.SetStringItem(index, 3, 'http://10.10.10.10/1.txt')
##
##        index = self.list_ctrl_1.InsertStringItem(sys.maxint,u'小说2')
##        self.list_ctrl_1.SetStringItem(index, 3, 'http://20.20.20.20/2.txt')
##
##        index = self.list_ctrl_1.InsertStringItem(sys.maxint,u'小说3')
##        self.list_ctrl_1.SetStringItem(index, 3, 'http://30.30.30.30/3.txt')

        self.button_1 = wx.Button(self, -1, u"下载")
        self.button_2 = wx.Button(self, -1, u"关闭")
        self.button_3 = wx.Button(self, -1, u"搜索")
        self.Bind(wx.EVT_BUTTON, self.OnDownload, self.button_1)
        self.Bind(wx.EVT_BUTTON, self.OnCancell, self.button_2)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnSearch, self.text_ctrl_1)
        self.Bind(wx.EVT_BUTTON, self.OnSearch, self.button_3)
        self.Bind(EVT_SRE,self.OnReport)
        self.Bind(wx.EVT_CLOSE,self.OnClose)

        self.__set_properties()
        self.__do_layout()

        self.rs_thread = ReportSVRThread(self)
        if kadp_url != None:
            self.kadp_ctrl = xmlrpclib.Server(kadp_url)

        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: LTBSearchDiag.__set_properties
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap(cur_file_dir()+u"/icon/litebook-icon_32x32.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetTitle(u"LTBNET搜索")
        self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_WINDOW))
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["Ready."]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)

        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: LTBSearchDiag.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.StaticBoxSizer(self.sizer_3_staticbox, wx.HORIZONTAL)
        sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.HORIZONTAL)
        sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.text_ctrl_1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.button_3, 0, 0, 0)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)
        sizer_3.Add(self.list_ctrl_1, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_3, 1, wx.EXPAND, 0)
        sizer_4.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_1, 0, 0, 0)
        sizer_4.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_4.Add(self.button_2, 0, 0, 0)
        sizer_4.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_4, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.SetSize((800,380))
        # end wxGlade

    def OnSearch(self,evt):
        global report_port,report_rpc_path
        self.list_ctrl_1.DeleteAllItems() #can NOT use ClearAll here, because it will del all columns too
        kw_list = self.text_ctrl_1.GetValue().strip().split()
        for kw in kw_list:
            if len(kw)<=1:
                dlg = wx.MessageDialog(None, u'每个关键词长度都要大于1',u"错误！",wx.OK|wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                return
        if kw_list==[]: return
        utfklist=[]
        for k in kw_list:
            utfklist.append(k.encode('utf-8'))
        self.ongoing_kw = len(kw_list)
##        print "prepare start searching"
##        print kw_list
        try:
            self.kadp_ctrl.search(utfklist,'http://127.0.0.1:'+str(report_port)+report_rpc_path)
        except Exception, inst:
                dlg = wx.MessageDialog(None, u'无法连接到KADP协议进程！建议稍后重试或是重启程序。\n'+str(inst),u"错误！",wx.OK|wx.ICON_ERROR)
                dlg.ShowModal()
                dlg.Destroy()
                return
        self.button_3.Disable()
        self.text_ctrl_1.Disable()
        self.frame_1_statusbar.SetStatusText(u'搜索中...')

    def GetResults(self):
        return self.list_ctrl_1.GetAllChecked()

    def OnCancell(self,evt):
        self.Hide()

    def OnDownload(self,evt):
        rlist=self.list_ctrl_1.GetAllChecked()
        for r in rlist:
            self.downloadFunc(r['url'])
        self.Hide()

    def OnReport(self,evt):
        for r in evt.result:
            self.list_ctrl_1.addResult(r)
        self.ongoing_kw -= 1
        if self.ongoing_kw <=0:
            self.frame_1_statusbar.SetStatusText(u'搜索结束.')
            self.button_3.Enable()
            self.text_ctrl_1.Enable()

    def OnClose(self,evt):
        self.Hide()

# end of class LTBSearchDiag


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = LTBSearchDiag(None,None,'http://'+sys.argv[1]+':50201')
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
