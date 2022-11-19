import wx

class ToolsFrame(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(ToolsFrame, self).__init__(*args, **kwargs)

        self.init_ui()

    def init_ui(self):
        print('hi')


def main():
    app = wx.App()
    frame = ToolsFrame(None, title="A2L Tools", size=(800,600))
    frame.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()