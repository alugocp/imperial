from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MimeBarWidget(QFrame):
    def __init__(self,parent):
        super(MimeBarWidget,self).__init__()
        self.parent=parent
        self.widget=QFrame()
        self.scrolling=QScrollArea(self)
        self.scrolling.setWidget(self.widget)
        layout=QVBoxLayout()
        layout.setSpacing(0)
        layout.setMargin(0)
        for k in sorted(parent.os.mimes.hash):
            list=MimeList(self,parent.os.mimes,k)
            list.setVisible(False)
            header=MimeHeader(self,k,list)
            layout.addWidget(header)
            layout.addWidget(list)
        self.widget.setMinimumSize(self.width(),self.height())
        self.widget.setLayout(layout)
        self.widget.adjustSize()
    def paintEvent(self,event):
        self.scrolling.resize(self.width(),self.height())

class MimeHeader(QFrame):
    def __init__(self,parent,name,list):
        super(MimeHeader,self).__init__()
        layout=QHBoxLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel(name))
        self.parent=parent
        self.list=list
    def mouseReleaseEvent(self,event):
        self.list.setVisible(not self.list.isVisible())
        self.parent.widget.adjustSize()
class MimeList(QFrame):
    def __init__(self,parent,mimes,k):
        super(MimeList,self).__init__()
        layout=QVBoxLayout()
        self.setLayout(layout)
        self.parent=parent
        self.k=k
        for m in sorted(mimes[k]):
            layout.addWidget(QLabel(m))
    def mouseReleaseEvent(self,event):
        target=self.childAt(event.x(),event.y())
        self.parent.parent.desc.setDescription(self.k,target.text())
        self.parent.parent.icon.loadMime(self.k,target.text())
