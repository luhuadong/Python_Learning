import wx

# 创建应用程序对象
app = wx.App()

# 创建一个窗口
win = wx.Frame(None, title="老师的点名神器", size=(410, 335))

#startBtn = wx.Button(win, label="开始", pos=(100, 100), size=(200, 80))
loadBtn = wx.Button(win, label="Open", pos=(225, 5), size=(80, 25))
saveBtn = wx.Button(win, label="Save", pos=(315, 5), size=(80, 25))

filename = wx.TextCtrl(win, pos=(5, 5), size=(210, 25))

contents = wx.TextCtrl(win, pos=(5, 35), size=(390, 260), style=wx.TE_MULTILINE | wx.HSCROLL)

# 设置可见
win.Show()

# 进入应用程序事件主循环
app.MainLoop()

