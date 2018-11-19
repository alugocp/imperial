from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSvg import *

class IconSlot(QFrame):
    def __init__(self,parent):
        super(IconSlot,self).__init__()
        self.icon=SvgIcon(self)
        self.setAcceptDrops(True)
        self.painter=QPainter()
        self.parent=parent
    def dragEnterEvent(self,event):
        if(hasattr(self,"k")): event.acceptProposedAction()
        else: self.message("No icon selected")
    def paintEvent(self,event):
        self.icon.setGeometry(25,25,self.width()-50,self.height()-50)
    def dropEvent(self,event):
        path=event.mimeData().urls()[0].path()
        try:
            self.parent.os.addIcon(path,self.k,self.type)
            self.message("New icon set")
        except:
            self.message("Could not set icon")
        self.icon.renderer=QSvgRenderer(path)
        self.update()
    def loadMime(self,k,type):
        self.k=k
        self.type=type
        path=self.parent.os.getIcon(k,type)
        if(path==None): self.icon.renderer=None
        else: self.icon.renderer=QSvgRenderer(path)
        self.update()
    def message(self,msg):
        self.parent.desc.msg.setText(msg)
class SvgIcon(QSvgWidget):
    def __init__(self,parent):
        super(SvgIcon,self).__init__(parent=parent)
        self.painter=QPainter()
        self.renderer=None
    def paintEvent(self,event):
        if(self.renderer):
            self.painter.begin(self)
            self.renderer.render(self.painter)
            self.painter.end()
