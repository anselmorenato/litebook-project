﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-

u"""LiteView is a read-only optimized wxpython text control, which provides
following features:
- 3 show modes: paper/book/vertical-book
- configurable: background(picture)/font/underline/margin
- render speed is independent of file size

Author: Hu Jun
Updated: 29/05/2010

"""

import wx
import sys
import re
import time





#---------------------------------------------------------------------------

class LiteView(wx.ScrolledWindow):
    u"""LiteView，一个看书的wxpython文本控件，具备如下特性：
        -只读
        -支持 背景（图片）/行间距/下划线/页边距/字体 等可设置
        -支持三种不同的显示模式（纸张/书本/竖排书本）

    """
    def __init__(self, parent, id = -1, bg_img=None):
        u"""
        bg_img: background image, can be bitmap obj or a string of filepath
        """
        sdc=wx.ScreenDC()
        wx.ScrolledWindow.__init__(self, parent, id, (0, 0), size=sdc.GetSize(), style=wx.SUNKEN_BORDER|wx.CLIP_CHILDREN)

        #初始化一些设置
        self.TextBackground='white'
        self.SetBackgroundColour(self.TextBackground)
        self.pagemargin=50
        self.bookmargin=50
        self.vbookmargin=50
        self.centralmargin=20
        self.linespace=5
        self.vlinespace=15
        self.Value=None
        self.under_line=True
        self.under_line_color="LIGHTGREEN"
        self.under_line_style=wx.DOT
        self.curPageTextList=[]
        self.bg_buff=None
        self.newbmp=None
        self.SetImgBackgroup(bg_img)
        self.bg_style='tile'
        self.show_mode='paper'
        self.buffer_bak=None
        self.TextForeground='black'
        #setup the default font
        self.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, ""))
        self.current_pos=0
        self.start_pos=0
        self.SelectedRange=[0,0]
        # Initialize the buffer bitmap.  No real DC is needed at this point.
        self.buffer=None

        #绑定事件处理
##        self.Bind(wx.EVT_SCROLLWIN,self.OnScroll)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_CHAR,self.OnChar)
        self.Bind(wx.EVT_SIZE,self.OnResize)
        self.Bind(wx.EVT_LEFT_DOWN,self.OnMouseDrag)
        self.Bind(wx.EVT_LEFT_UP,self.OnMouseDrag)
        self.Bind(wx.EVT_MOTION,self.OnMouseDrag)
        self.Bind(wx.EVT_RIGHT_UP,self.OnMouseDrag)


    def GetHitPos(self,pos):
        #返回坐标所在字在self.Value中的[index,字的坐标]
        r={}
        dc=wx.MemoryDC()
        dc.SetFont(self.GetFont())
        ch_h=dc.GetCharHeight()
        ch_w=dc.GetTextExtent(u'我')[0]
        if self.show_mode=='paper':
            line=pos[1]/(self.linespace+ch_h)
            pos_list=dc.GetPartialTextExtents(self.curPageTextList[line][0])
            i=0
            tlen=pos[0]-self.pagemargin
            while i<len(pos_list):
                if pos_list[i]>tlen:break
                else:
                    i+=1
            if i>=len(self.curPageTextList[line][0]):
                i=len(self.curPageTextList[line][0])
            m=0
            delta=0
            while m<line:
                delta+=len(self.curPageTextList[m][0])+self.curPageTextList[m][1]
                m+=1
            delta+=i
            if len(self.curPageTextList[line][0])==0:
                x=self.pagemargin
            else:
                x=self.pagemargin+dc.GetTextExtent(self.curPageTextList[line][0][:i])[0]
            y=(ch_h+self.linespace)*line
            r['index']=self.start_pos+delta
            r['pos']=(x,y)
            r['line']=line
            r['row']=i
##            return [(self.start_pos+delta),(x,y)]
            return r

    def GenSelectColor(self):
        """返回选择文字时候被选择文字的颜色"""
        cf=wx.NamedColour(self.TextForeground)
        oldr=cf.Red()
        oldg=cf.Green()
        oldb=cf.Blue()
        if self.bg_img==None:
            cb=wx.NamedColour(self.TextBackground)
            bgr=cb.Red()
            bgg=cb.Green()
            bgb=cb.Blue()
            newr=(510-oldr-bgr)/2
            newg=(510-oldg-bgg)/2
            newb=(510-oldb-bgb)/2
##            print 'old color is ',oldr,oldg,oldb
##            print 'bg color is ',bgr,bgg,bgb
##            print 'new color is ',newr,newg,newb
            if oldr==0: oldr=1
            if oldg==0: oldg=1
            if oldb==0: oldb=1
            if bgr==0:bgr=1
            if bgg==0:bgg=1
            if bgb==0:bgb=1
            if (float(oldg)/float(oldr)<0.5 and float(oldb)/float(oldr)<0.5) or (float(bgg)/float(bgr)<0.5 and float(bgb)/float(bgr)<0.5):
                return (wx.Color(newr,newg,newb,0))
            else:
                return (wx.NamedColor('red'))
        else:
            dc = wx.MemoryDC( )
            dc.SelectObject( self.bg_buff)
            x=dc.GetSize()[0]/2
            y=dc.GetSize()[1]/2
            n=50
            xt=x+n
            b=0
            g=0
            r=0
            while x<xt:
                y+=1
                tc=dc.GetPixel(x,y)
                b+=tc.Blue()
                g+=tc.Green()
                r+=tc.Red()
                x+=1
            b/=n
            g/=n
            r/=n
            newr=(510-oldr-r)/2
            newg=(510-oldg-g)/2
            newb=(510-oldb-b)/2
            if oldr==0: oldr=1
            if oldg==0: oldg=1
            if oldb==0: oldb=1
            if r==0: r=1
            if g==0: g=1
            if b==0: b=1
            if (float(oldg)/float(oldr)<0.5 and float(oldb)/float(oldr)<0.5) or (float(g)/float(r)<0.5 and float(b)/float(r)<0.5):
                return (wx.Color(newr,newg,newb,0))
            else:
                return (wx.NamedColor('red'))



    def DrawSelection(self,dc,r1,r2):
        dc.SetFont(self.GetFont())
        ch_h=dc.GetCharHeight()
        newc=self.GenSelectColor()
        dc.SetTextForeground(newc)
        dc.BeginDrawing()
        if r1['pos'][1]==r2['pos'][1]:
            #如果在同一行
            dc.SetTextForeground(newc)
            y=r1['pos'][1]
            if r1['pos'][0]>r2['pos'][0]:
                x1=r2['pos'][0]
                x2=r1['pos'][0]
                i1=r2['index']
                i2=r1['index']
            else:
                x2=r2['pos'][0]
                x1=r1['pos'][0]
                i2=r2['index']
                i1=r1['index']
            dc.DrawText(self.Value[i1:i2],x1,y)
        else:
            if r1['pos'][1]>r2['pos'][1]:
                y2=r1['pos'][1]
                x2=r1['pos'][0]
                l2=r1['line']
                w2=r1['row']
                y1=r2['pos'][1]
                x1=r2['pos'][0]
                l1=r2['line']
                w1=r2['row']
            elif r1['pos'][1]<r2['pos'][1]:
                y1=r1['pos'][1]
                x1=r1['pos'][0]
                l1=r1['line']
                w1=r1['row']
                y2=r2['pos'][1]
                x2=r2['pos'][0]
                l2=r2['line']
                w2=r2['row']
            line=l1
            pos1=w1
            x=x1
            y=y1
            while line<l2:
                dc.DrawText(self.curPageTextList[line][0][pos1:],x,y)
                x=self.pagemargin
                y+=self.linespace+ch_h
                pos1=0
                line+=1
            dc.DrawText(self.curPageTextList[line][0][:w2],self.pagemargin,y)
        dc.EndDrawing()


    def OnMouseDrag(self,evt):
        if evt.ButtonDown(wx.MOUSE_BTN_LEFT):
            self.LastMousePos=evt.GetPositionTuple()
            self.FirstMousePos=evt.GetPositionTuple()
            if self.buffer_bak<>None:
                self.buffer=self.buffer_bak.GetSubBitmap(wx.Rect(0, 0, self.buffer_bak.GetWidth(), self.buffer_bak.GetHeight()))
                dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
                dc.BeginDrawing()
                dc.EndDrawing()
            return
        if evt.Dragging():
            current_mouse_pos=evt.GetPositionTuple()
            if current_mouse_pos==self.LastMousePos:return
            else:
                r1=self.GetHitPos(self.FirstMousePos)
                r2=self.GetHitPos(current_mouse_pos)
                self.buffer=self.buffer_bak.GetSubBitmap(wx.Rect(0, 0, self.buffer_bak.GetWidth(), self.buffer_bak.GetHeight()))
                dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
                self.DrawSelection(dc,r1,r2)
            self.LastMousePos=current_mouse_pos
        elif evt.ButtonUp(wx.MOUSE_BTN_LEFT) and not evt.LeftDClick():
            current_mouse_pos=evt.GetPositionTuple()
            r1=self.GetHitPos(self.FirstMousePos)
            r2=self.GetHitPos(current_mouse_pos)
            if r1['index']>r2['index']:
                self.SelectedRange[0]=r2['index']
                self.SelectedRange[1]=r1['index']
##                self.SelectedRange=[r2['index'],r1['index']]
            else:
                self.SelectedRange[1]=r2['index']
                self.SelectedRange[0]=r1['index']
##                self.SelectedRange=[r1['index'],r2['index']]


        if evt.RightUp():
            clipdata = wx.TextDataObject()
            clipdata.SetText(self.Value[self.SelectedRange[0]:self.SelectedRange[1]])
            if not wx.TheClipboard.IsOpened():
                wx.TheClipboard.Open()
                wx.TheClipboard.SetData(clipdata)
                wx.TheClipboard.Close()
            if self.buffer_bak<>None:
                self.buffer=self.buffer_bak.GetSubBitmap(wx.Rect(0, 0, self.buffer_bak.GetWidth(), self.buffer_bak.GetHeight()))
                dc = wx.BufferedDC(wx.ClientDC(self), self.buffer)
                dc.BeginDrawing()
                dc.EndDrawing()


    def OnChar(self,event):
        """键盘输入控制函数"""
        key=event.GetKeyCode()
        if key == wx.WXK_PAGEDOWN or key==wx.WXK_SPACE or key==wx.WXK_RIGHT:
            self.ScrollP(1)
            return
        if key == wx.WXK_PAGEUP or key==wx.WXK_LEFT :
            self.ScrollP(-1)
            return
##        if key == wx.WXK_DOWN:
##            pass
##            return
##        if key == wx.WXK_UP :
##            self.ScrollL(-1)
##            return
        if key == wx.WXK_HOME :
            self.ScrollTop()
            return
        if key == wx.WXK_END :
            self.ScrollBottom()
            return
        event.Skip()

    def DrawBackground(self,dc):
        """Draw background according to show_mode and bg_img"""
        sz = dc.GetSize()
        w = self.bg_img.GetWidth()
        h = self.bg_img.GetHeight()
        if self.bg_style=='tile':
            x = 0
            while x <= sz.width:
                y = 0

                while y <= sz.height:
                    dc.DrawBitmap(self.bg_img, x, y)
                    y = y + h
                x = x + w
        else:
            startx=(sz.width-w)/2
            if startx<0:startx=0
            starty=(sz.height-h)/2
            if starty<0:starty=0
            dc.DrawBitmap(self.bg_img,startx,starty)

##        if self.show_mode=='vertical_book':
##            oldpen=dc.GetPen()
##            oldbrush=dc.GetBrush()
##            dc.SetPen(wx.Pen('grey',width=5))
##            dc.SetBrush(wx.Brush('white',style=wx.TRANSPARENT))
##            dc.DrawLine(self.vbookmargin,self.vbookmargin,self.maxWidth-self.vbookmargin,self.vbookmargin)
##            dc.DrawLine(self.vbookmargin,self.maxHeight-2*self.vbookmargin,self.maxWidth-self.vbookmargin,self.maxHeight-2*self.vbookmargin)
##            dc.SetPen(oldpen)
##            dc.SetBrush(oldbrush)

        if self.show_mode=='book' or self.show_mode=='vertical_book':
            dc.DrawLine(3,0,3,sz.height)
            dc.DrawLine(4,0,4,sz.height)
            dc.DrawLine(6,0,6,sz.height)
            dc.DrawLine(8,0,8,sz.height)
            dc.DrawLine(10,0,10,sz.height)

            dc.DrawLine(sz.width-3,0,sz.width-3,sz.height)
            dc.DrawLine(sz.width-4,0,sz.width-4,sz.height)
            dc.DrawLine(sz.width-6,0,sz.width-6,sz.height)
            dc.DrawLine(sz.width-8,0,sz.width-8,sz.height)
            dc.DrawLine(sz.width-10,0,sz.width-10,sz.height)
            x=sz.width/2-20
            y=self.pagemargin+10
            n=self.pagemargin+10
            xt=x+n
            b=0
            g=0
            r=0
            while x<xt:
                tc=dc.GetPixel(x,y)
                b+=tc.Blue()
                g+=tc.Green()
                r+=tc.Red()
                x+=1
            b/=n
            g/=n
            r/=n

            dc.GradientFillLinear((sz.width/2-self.centralmargin,0, self.centralmargin,sz.height),wx.Color(r,g,b,0),'grey')
            dc.GradientFillLinear((sz.width/2,0, self.centralmargin,sz.height),'grey',wx.Color(r,g,b,0))


    def ReDraw(self):
        """ReDraw self"""
        delta=(self.GetSize()[1]-self.GetClientSize()[1])+1
        self.maxHeight=self.GetClientSize()[1]
        self.maxWidth=self.GetClientSize()[0]-delta
        self.SetVirtualSize((self.maxWidth, self.maxHeight))
        self.current_pos=self.start_pos
        self.bg_buff=None
        self.buffer=None
        self.ShowPos(1)
##        self.current_pos=0
        self.current_pos=self.start_pos
        self.ShowPos(1)

        self.Refresh(False)



    def SetShowMode(self,m):
        """设置显示模式，支持的有'book/paper/vertical_book'"""
        self.show_mode=m

    def GetPos(self):
        """返回当前页面显示最后一个字在self.ValueList中的index"""
        return self.current_pos

    def ScrollTop(self):
        """显示第一页"""
        self.current_pos=0
        self.start_pos=0
        self.ShowPos(1)
        self.Refresh()

    def ScrollBottom(self):
        """显示最后一页"""
        self.start_pos=self.ValueCharCount
        self.ShowPos(-1)
        self.Refresh()

    def ScrollP(self,direction):
        """向上或是向下翻页"""
##        t1=time.time()
        self.ShowPos(direction)
        self.Refresh(False) #Use False to avoid background flicker
##        print time.time()-t1

##    def getPreviousLine(self,txt):
##        llist=txt.splitlines()
##        dc=wx.MemoryDC()
##        dc.SetFont(self.GetFont())
##        delta=2*dc.GetCharHeight()
##        lline=llist[len(llist)-1]
##        newwidth=self.maxWidth-2*self.pagemargin
##        if dc.GetTextExtent(lline)[0]<=newwidth:
##            if txt[len(txt)-1]=='\n':
##                return lline+'\n'
##            else:
##                return lline
##        else:
##            high=len(lline)-1
##            low=0
##
##            while low<high:
##                mid=(low+high)/2
##                if dc.GetTextExtent(lline[mid:])[0]>newwidth:  low=mid+1
##                else:
##                    if dc.GetTextExtent(lline[mid:])[0]<newwidth: high=mid-1
##                    else:
##                        break
##            if dc.GetTextExtent(lline[mid:])[0]>newwidth: mid-=1
##            if txt[len(txt)-1]=='\n': return lline[mid:]+'\n'
##            else:
##                return lline[mid:]


##    def ScrollL(self,direction):
##        """向上或是向下翻行"""
##        if direction==1:
##            self.current_pos=self.start_pos+len(self.curPageTextList[0][0])+self.curPageTextList[0][1]
##            self.ShowPos(1)
##        else:
##            n=len(self.curPageTextList)
##            self.start_pos=self.start_pos+len()
##
##            self.ShowPos(-1)
##
##        self.Refresh()


##    def OnScroll(self,evt):
##        if self.GetScrollPos(wx.VERTICAL)==0:
##            self.ScollP(-1)
####            pass
##        else:
##            if self.GetScrollPos(wx.VERTICAL)+self.GetScrollThumb(wx.VERTICAL)==self.GetScrollRange(wx.VERTICAL):
##                self.ScollP(1)
##        evt.Skip()
    def OnResize(self,evt):
        self.isdirty=True
        self.ReDraw()




    def OnPaint(self, event):
        delta=(self.GetSize()[1]-self.GetClientSize()[1])+1
        self.maxHeight=self.GetClientSize()[1]
        self.maxWidth=self.GetClientSize()[0]-delta
        self.SetVirtualSize((self.maxWidth, self.maxHeight))
            # Create a buffered paint DC.  It will create the real
            # wx.PaintDC and then blit the bitmap to it when dc is
            # deleted.  Since we don't need to draw anything else
            # here that's all there is to it.
        if self.buffer<>None and not self.isdirty:
##            print "if yes"
            if self.bg_img==None or self.bg_buff==None or self.newbmp==None:
                dc = wx.BufferedPaintDC(self, self.buffer, wx.BUFFER_VIRTUAL_AREA)
            else:
                dc = wx.BufferedPaintDC(self, self.newbmp, wx.BUFFER_VIRTUAL_AREA)
        else:
##            print "if no"
            self.ShowPos(1)


    def SetValue(self,txt):
        self.Value=txt
        self.ValueCharCount=len(self.Value)
        self.current_pos=0
        self.start_pos=0
        self.Refresh()


    def SetImgBackgroup(self,img,style='tile'):
        self.bg_style=style
        if isinstance(img,wx.Bitmap):
            self.bg_img=img
        else:
            if isinstance(img,str) or isinstance(img,unicode):
                self.bg_img=wx.Bitmap(img, wx.BITMAP_TYPE_ANY)
            else:
                self.bg_img=None
##        if self.bg_img<>None:
##            self.bg_img_buffer.BeginDrawing()
##            self.DrawBackground(self.bg_img_buffer)
##            self.bg_img_buffer.EndDrawing()


    def breakline(self,line,dc):
        rr=line
        rlist=[]

        if self.show_mode=='paper':
            newwidth=self.maxWidth-2*self.pagemargin
            delta=dc.GetCharHeight()
        elif self.show_mode=='book':
            newwidth=self.maxWidth/2-self.bookmargin-self.centralmargin
            delta=dc.GetCharHeight()
        elif self.show_mode=='vertical_book':
            ch_h=dc.GetCharHeight()
            ch_w=dc.GetCharWidth()
            newwidth=self.maxWidth-2*self.vbookmargin
            newheight=self.maxHeight-2*self.vbookmargin
        if self.show_mode=='book' or self.show_mode=='paper':
            llist=dc.GetPartialTextExtents(line)
            n=len(llist)-1
            mid=0
            mylen=llist[n]
            while mylen>newwidth:
                high=n
                low=mid
                base=mid
                while low<high:
                    mid=(low+high)/2
                    if llist[mid]-llist[base]>newwidth: high=mid-1
                    else:
                        if llist[mid]-llist[base]<newwidth-delta: low=mid+1
                        else:
                            break
    ##            if dc.GetTextExtent(rr[:mid])[0]>newwidth: mid-=1
                rlist.append([rr[base:mid],0])
                mylen=llist[n]-llist[mid-1]
            rlist.append([rr[mid:],1])
            return rlist
        elif self.show_mode=='vertical_book':
            n=newheight/(ch_h+2)
            i=0
            while i<len(line):
                rlist.append([line[i:i+n],0])
                i+=n
            i-=n
            rlist[len(rlist)-1][1]=1
            return rlist





    def mywrap(self,txt):
        dc=wx.MemoryDC()
        dc.SetFont(self.GetFont())
        ch_h=dc.GetCharHeight()
        ch_w=dc.GetCharWidth()
        if self.show_mode=='paper':
            newwidth=self.maxWidth-2*self.pagemargin
        elif self.show_mode=='book':
            newwidth=self.maxWidth/2-self.bookmargin-self.centralmargin
        elif self.show_mode=='vertical_book':
            newwidth=self.maxWidth-2*self.vbookmargin
            newheight=self.maxHeight-2*self.vbookmargin
        rlist=[]
        if self.show_mode=='paper':
            for line in txt.splitlines():
                if dc.GetTextExtent(line)[0]<= newwidth:
                    rlist.append([line,1])
                else:
                    trlist=self.breakline(line,dc)
                    rlist+=trlist
        elif self.show_mode=='book':
            for line in txt.splitlines():
                if dc.GetTextExtent(line)[0]<= newwidth:
                    rlist.append([line,1])
                else:
                    trlist=self.breakline(line,dc)
                    rlist+=trlist
        elif self.show_mode=='vertical_book':
            for line in txt.splitlines():
                if len(line)*(self.linespace+ch_h)<=newheight:
                    rlist.append([line,1])
                else:
                    trlist=self.breakline(line,dc)
                    rlist+=trlist
        return rlist



    def ShowPos(self,direction=1):
        """从指定位置开始，画出一页的文本"""

        self.isdirty=False
        if self.Value==None:
            return
        if direction==1:
            if self.current_pos>=self.ValueCharCount: return
        else:
            if self.start_pos==0:return
        if direction==1:
            if self.current_pos>=len(self.Value):return
        dc=wx.MemoryDC()
        dc.SetFont(self.GetFont())

        ch_h=dc.GetCharHeight()
        ch_w=dc.GetCharWidth()
        maxcount=(self.maxHeight/(ch_h+self.linespace))*((self.maxWidth-2*self.pagemargin)/ch_w)
        self.blockline=self.maxHeight/(ch_h+self.linespace)
        self.SetVirtualSize((self.maxWidth, self.maxHeight))
        self.buffer = wx.EmptyBitmap(self.maxWidth, self.maxHeight)
        if self.bg_buff==None:
            dc = wx.BufferedDC(None, self.buffer)
            dc.SetBackground(wx.Brush(self.GetBackgroundColour()))
            dc.Clear()
        else:
            self.newbmp=self.bg_buff.GetSubBitmap(wx.Rect(0, 0, self.bg_buff.GetWidth(), self.bg_buff.GetHeight()));
            dc = wx.BufferedDC(None, self.newbmp)
        dc.SetFont(self.GetFont())
        dc.SetTextForeground(self.TextForeground)
        dc.SetTextBackground('black')
        dc.BeginDrawing()

        #draw backgroup
        if self.bg_img<>None and self.bg_buff==None:
            self.DrawBackground(dc)
            if self.bg_buff==None:
                memory = wx.MemoryDC( )
                x,y = self.GetClientSizeTuple()
                self.bg_buff = wx.EmptyBitmap( x,y, -1 )
                memory.SelectObject( self.bg_buff )
                memory.Blit( 0,0,x,y, dc, 0,0)
                memory.SelectObject( wx.NullBitmap)


        if self.show_mode=='paper':
            #draw paper mode
            h=0
            cur_pos=self.current_pos
            cur_x=0
            self.curPageTextList=[]
            if direction==1:
                if cur_pos+maxcount<len(self.Value):
                    tmptxt=self.Value[cur_pos:cur_pos+maxcount]
                else:
                    tmptxt=self.Value[cur_pos:]
                ptxtlist=self.mywrap(tmptxt)
                if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                line=0
                delta=0
                while line<self.blockline:
                    dc.DrawText(ptxtlist[line][0],self.pagemargin,h)
                    self.curPageTextList.append(ptxtlist[line])
                    if self.under_line:
                        oldpen=dc.GetPen()
                        newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                        dc.SetPen(newpen)
                        dc.DrawLine(self.pagemargin,h+ch_h+2,self.maxWidth-self.pagemargin,h+ch_h+2)
                        dc.SetPen(oldpen)
                    delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                    if line==len(ptxtlist)-1:break
                    h+=ch_h+self.linespace
                    line+=1
                self.start_pos=self.current_pos
                self.current_pos+=delta

            else:
                pos1=self.start_pos-maxcount
                if pos1<0: pos1=0
                pos2=self.start_pos
                tmptxt=self.Value[pos1:pos2]
                ptxtlist=self.mywrap(tmptxt)
                if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                line=len(ptxtlist)-1
                if line<0:line=0
                delta=0
                h=self.maxHeight-ch_h
                tlen=len(ptxtlist)-1-self.blockline
                elist=[]
                if tlen<0:
                    tmptxt=self.Value[:maxcount]
                    ptxtlist=self.mywrap(tmptxt)
                    if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                    line=0
                    delta=0
                    h=0
                    while line<self.blockline:
                        dc.DrawText(ptxtlist[line][0],self.pagemargin,h)
                        self.curPageTextList.append(ptxtlist[line])
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(self.pagemargin,h+ch_h+2,self.maxWidth-self.pagemargin,h+ch_h+2)
                            dc.SetPen(oldpen)
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        if line==len(ptxtlist)-1:break
                        h+=ch_h+self.linespace
                        line+=1
                    self.start_pos=0
                    self.current_pos=delta
                    dc.EndDrawing()
                    return
                else:
                    while line>tlen :
                        dc.DrawText(ptxtlist[line][0],self.pagemargin,h)
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(self.pagemargin,h+ch_h+2,self.maxWidth-self.pagemargin,h+ch_h+2)
                            dc.SetPen(oldpen)
                        elist.append(ptxtlist[line])
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        h-=(ch_h+self.linespace)
                        line-=1

                self.current_pos=self.start_pos
                self.start_pos-=delta
                i=len(elist)-1
                while i>=0:
                    self.curPageTextList.append(elist[i])
                    i-=1
        elif self.show_mode=='book':
            #draw book mode
            h=0
            cur_pos=self.current_pos
            cur_x=0
            self.curPageTextList=[]
            if direction==1:
                if cur_pos+maxcount<len(self.Value):
                    tmptxt=self.Value[cur_pos:cur_pos+maxcount]
                else:
                    tmptxt=self.Value[cur_pos:]
                ptxtlist=self.mywrap(tmptxt)
                if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                line=0
                delta=0
                #draw left page
                while line<self.blockline:
                    dc.DrawText(ptxtlist[line][0],self.bookmargin,h)
                    self.curPageTextList.append(ptxtlist[line])
                    if self.under_line:
                        oldpen=dc.GetPen()
                        newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                        dc.SetPen(newpen)
                        dc.DrawLine(self.bookmargin,h+ch_h+2,self.maxWidth/2-self.centralmargin,h+ch_h+2)
                        dc.SetPen(oldpen)
                    delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                    if line==len(ptxtlist)-1:break
                    h+=ch_h+self.linespace
                    line+=1
                #draw right page
                h=0
                newx=self.maxWidth/2+self.centralmargin
                while line<2*self.blockline:

                    dc.DrawText(ptxtlist[line][0],newx,h)
                    self.curPageTextList.append(ptxtlist[line])
                    if self.under_line:
                        oldpen=dc.GetPen()
                        newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                        dc.SetPen(newpen)
                        dc.DrawLine(self.maxWidth/2+self.centralmargin,h+ch_h+2,self.maxWidth-self.bookmargin,h+ch_h+2)
                        dc.SetPen(oldpen)
                    delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                    if line==len(ptxtlist)-1:break
                    h+=ch_h+self.linespace
                    line+=1
                self.start_pos=self.current_pos
                self.current_pos+=delta

            else:
                pos1=self.start_pos-maxcount
                if pos1<0: pos1=0
                pos2=self.start_pos
                tmptxt=self.Value[pos1:pos2]
                ptxtlist=self.mywrap(tmptxt)
                if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                line=len(ptxtlist)-1
                if line<0:line=0
                delta=0
                h=self.maxHeight-ch_h
                tlen=len(ptxtlist)-1-2*self.blockline
                elist=[]
                if tlen<0:
                    tmptxt=self.Value[:maxcount]
                    ptxtlist=self.mywrap(tmptxt)
                    if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                    line=0
                    delta=0
                    h=0
                    #draw left page
                    while line<self.blockline:
                        dc.DrawText(ptxtlist[line][0],self.pagemargin,h)
                        self.curPageTextList.append(ptxtlist[line])
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(self.pagemargin,h+ch_h+2,self.maxWidth-self.pagemargin,h+ch_h+2)
                            dc.SetPen(oldpen)
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        if line==len(ptxtlist)-1:break
                        h+=ch_h+self.linespace
                        line+=1
                    #draw right page
                    h=0
                    newx=self.maxWidth/2+self.centralmargin
                    while line<2*self.blockline:
                        dc.DrawText(ptxtlist[line][0],newx,h)
                        self.curPageTextList.append(ptxtlist[line])
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(self.maxWidth/2+self.centralmargin,h+ch_h+2,self.maxWidth-self.bookmargin,h+ch_h+2)
                            dc.SetPen(oldpen)
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        if line==len(ptxtlist)-1:break
                        h+=ch_h+self.linespace
                        line+=1
                    self.start_pos=0
                    self.current_pos=delta
                    dc.EndDrawing()
                    return
                else:
                    line=tlen+self.blockline
                    #draw left page
                    while line>tlen:
                        dc.DrawText(ptxtlist[line][0],self.pagemargin,h)
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(self.pagemargin,h+ch_h+2,self.maxWidth-self.pagemargin,h+ch_h+2)
                            dc.SetPen(oldpen)
                        elist.append(ptxtlist[line])
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        h-=(ch_h+self.linespace)
                        line-=1
                    #draw right page
                    h=self.maxHeight-ch_h
                    newx=self.maxWidth/2+self.centralmargin
                    line=len(ptxtlist)-1
                    while line>tlen+self.blockline:
                        dc.DrawText(ptxtlist[line][0],newx,h)
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(self.pagemargin,h+ch_h+2,self.maxWidth-self.pagemargin,h+ch_h+2)
                            dc.SetPen(oldpen)
                        elist.append(ptxtlist[line])
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        h-=(ch_h+self.linespace)
                        line-=1

                self.current_pos=self.start_pos
                self.start_pos-=delta
                i=len(elist)-1
                while i>=0:
                    self.curPageTextList.append(elist[i])
                    i-=1
        elif self.show_mode=='vertical_book':
            #draw vertical book
            ch_w=dc.GetTextExtent(u'我')[0]
            h=0
            cur_pos=self.current_pos
            cur_x=0
            self.curPageTextList=[]
            newwidth=self.maxWidth/2-self.vbookmargin-self.centralmargin
            newheight=self.maxHeight-2*self.vbookmargin
            self.blockline=newwidth/(ch_w+self.vlinespace)
            if direction==1:
                if cur_pos+maxcount<len(self.Value):
                    tmptxt=self.Value[cur_pos:cur_pos+maxcount]
                else:
                    tmptxt=self.Value[cur_pos:]
                ptxtlist=self.mywrap(tmptxt)
                if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                line=0
                delta=0
                #draw right page

                x=self.maxWidth-self.vbookmargin
                while line<=self.blockline:
                    y=self.vbookmargin
                    for chh in ptxtlist[line][0]:
                        dc.DrawText(chh,x,y)
                        y+=(ch_h+2)
                    x-=(self.vlinespace/2)
                    self.curPageTextList.append(ptxtlist[line])
                    if self.under_line:
                        oldpen=dc.GetPen()
                        newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                        dc.SetPen(newpen)
                        dc.DrawLine(x,self.vbookmargin,x,self.maxHeight-self.vbookmargin)
                        dc.SetPen(oldpen)
                    x-=(ch_w+self.vlinespace/2)
                    delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                    if line==len(ptxtlist)-1:break
                    line+=1
                #draw left page
                x=self.maxWidth/2-self.centralmargin-2*ch_w
                while line<=2*self.blockline:
                    y=self.vbookmargin
                    for chh in ptxtlist[line][0]:
                        dc.DrawText(chh,x,y)
                        y+=(ch_h+2)
                    x-=(self.vlinespace/2)
                    self.curPageTextList.append(ptxtlist[line])
                    if self.under_line:
                        oldpen=dc.GetPen()
                        newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                        dc.SetPen(newpen)
                        dc.DrawLine(x,self.vbookmargin,x,self.maxHeight-self.vbookmargin)
                        dc.SetPen(oldpen)
                    x-=(ch_w+self.vlinespace/2)
                    delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                    if line==len(ptxtlist)-1:break
                    line+=1
                self.start_pos=self.current_pos
                self.current_pos+=delta

            else:

                pos1=self.start_pos-maxcount
                if pos1<0: pos1=0
                pos2=self.start_pos
                tmptxt=self.Value[pos1:pos2]
                ptxtlist=self.mywrap(tmptxt)
                if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                line=len(ptxtlist)-1
                if line<0:line=0
                delta=0
                h=self.maxHeight-ch_h
                tlen=len(ptxtlist)-1-2*self.blockline
                elist=[]
                if tlen<0:
                    tmptxt=self.Value[:maxcount]
                    ptxtlist=self.mywrap(tmptxt)
                    if tmptxt[len(tmptxt)-1]<>'\n':ptxtlist[len(ptxtlist)-1][1]=0
                    line=0
                    delta=0
                    h=0
                    #draw right page
                    x=self.maxWidth-self.vbookmargin
                    while line<=self.blockline:
                        y=self.vbookmargin
                        for chh in ptxtlist[line][0]:
                            dc.DrawText(chh,x,y)
                            y+=(ch_h+2)
                        x-=(self.vlinespace/2)
                        self.curPageTextList.append(ptxtlist[line])
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(x,self.vbookmargin,x,self.maxHeight-self.vbookmargin)
                            dc.SetPen(oldpen)
                        x-=(ch_w+self.vlinespace/2)
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        if line==len(ptxtlist)-1:break
                        line+=1
                    #draw left page
                    x=self.maxWidth/2-self.centralmargin-ch_w
                    while line<=2*self.blockline:
                        y=self.vbookmargin
                        for chh in ptxtlist[line][0]:
                            dc.DrawText(chh,x,y)
                            y+=(ch_h+2)
                        x-=(self.vlinespace/2)
                        self.curPageTextList.append(ptxtlist[line])
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(x,self.vbookmargin,x,self.maxHeight-self.vbookmargin)
                            dc.SetPen(oldpen)
                        x-=(ch_w+self.vlinespace/2)
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        if line==len(ptxtlist)-1:break
                        line+=1
                    self.start_pos=0
                    self.current_pos=delta
                    dc.EndDrawing()
                    return
                else:
                    line=tlen+self.blockline
                    #draw right page
                    x=self.maxWidth-self.vbookmargin
                    while line>tlen:
                        y=self.vbookmargin
                        for chh in ptxtlist[line][0]:
                            dc.DrawText(chh,x,y)
                            y+=(ch_h+2)
                        x-=(self.vlinespace/2)
                        self.curPageTextList.append(ptxtlist[line])
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(x,self.vbookmargin,x,self.maxHeight-self.vbookmargin)
                            dc.SetPen(oldpen)
                        x-=(ch_w+self.vlinespace/2)
                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        if line==len(ptxtlist)-1:break
                        line-=1
                    #draw right page
                    x=self.vbookmargin
                    line=len(ptxtlist)-1
                    while line>tlen+self.blockline:
                        y=self.vbookmargin
                        if self.under_line:
                            oldpen=dc.GetPen()
                            newpen=wx.Pen(self.under_line_color,style=self.under_line_style)
                            dc.SetPen(newpen)
                            dc.DrawLine(x,self.vbookmargin,x,self.maxHeight-self.vbookmargin)
                            dc.SetPen(oldpen)
                        x+=(self.vlinespace/2)
                        for chh in ptxtlist[line][0]:
                            dc.DrawText(chh,x,y)
                            y+=(ch_h+2)
                        x+=(ch_w+self.vlinespace/2)
                        self.curPageTextList.append(ptxtlist[line])


                        delta+=len(ptxtlist[line][0])+ptxtlist[line][1]
                        line-=1

                self.current_pos=self.start_pos
                self.start_pos-=delta
                i=len(elist)-1
                while i>=0:
                    self.curPageTextList.append(elist[i])
                    i-=1
        dc.EndDrawing()

        memory = wx.MemoryDC( )
        x,y = self.GetClientSizeTuple()
        self.buffer_bak = wx.EmptyBitmap( x,y, -1 )
        memory.SelectObject( self.buffer_bak )
        memory.Blit( 0,0,x,y, dc, 0,0)
        memory.SelectObject( wx.NullBitmap)


class MyFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.Maximize(True)


        # Tool Bar
        self.frame_1_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_1_toolbar)
        # Tool Bar end
        self.frame_1_statusbar = self.CreateStatusBar(1, 0)

        # Menu Bar
        self.frame_1_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(101, u"关于(&A)", u"关于本程序", wx.ITEM_NORMAL)
        self.frame_1_menubar.Append(wxglade_tmp_menu, "item")
        self.SetMenuBar(self.frame_1_menubar)
        # Menu Bar end
        self.Bind(wx.EVT_MENU, self.Menu101, id=101)
        self.__set_properties()
        self.panel_1 = LiteView(self)
        self.__do_layout()



    def Menu101(self,evt):
        self.ShowFullScreen(True,wx.FULLSCREEN_ALL)



        # end wxGlade

    def __set_properties(self):
        self.frame_1_toolbar.Realize()
        self.frame_1_statusbar.SetStatusWidths([-1])
        # statusbar fields
        frame_1_statusbar_fields = ["frame_1_statusbar"]
        for i in range(len(frame_1_statusbar_fields)):
            self.frame_1_statusbar.SetStatusText(frame_1_statusbar_fields[i], i)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MyFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class MyFrame




if __name__ == "__main__":
    import psyco
    psyco.full()
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MyFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    if len(sys.argv)<=1:
        fp=open("5.txt",'r')
    else:
        fp=open(sys.argv[1],'r')
    alltxt=fp.read()
    alltxt=alltxt.decode('gbk')
    if len(sys.argv)<=2:
        frame_1.panel_1.SetImgBackgroup('6.jpg')
        pass
    else:
        frame_1.panel_1.SetImgBackgroup(sys.argv[2])
    if len(sys.argv)<=3:
        frame_1.panel_1.SetShowMode('paper')
    else:
        frame_1.panel_1.SetShowMode(sys.argv[3])
    frame_1.panel_1.SetValue(alltxt)
##    frame_1.panel_1.SetValue(u'　　一个黑色的小触角，小到什么程度？比旁边贴着地面的茅草还要低矮一点，它扭动着钻出了土层，小心翼翼地点点四周，又努力地挺直自己那黑黝黝不起眼的身躯，探索似的直立在空中，小触角似乎没有发现什么危险，迅速缩了回去，接着，地面开始震动，不停的震动，在触角回缩后的土地上，泥石翻裂，阵风吹过，掀起片片黄烟，似乎预示着，这片荒凉广阔的黄土地上要发生一些令人惊讶的事情来。')
    app.MainLoop()

