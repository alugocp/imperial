from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DescWidget(QFrame):
    def __init__(self,parent):
        super(DescWidget,self).__init__()
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        self.remove=Remove(self)
        self.msg=QLabel()
        self.layout.addWidget(self.msg)
        self.parent=parent
    def row(self,title,text):
        frame=QFrame()
        layout=QHBoxLayout()
        frame.setLayout(layout)
        layout.addWidget(Title(title))
        layout.addWidget(QLabel(text))
        return frame
    def setDescription(self,k,type):
        while(True):
            child=self.layout.takeAt(0)
            if(child and child.widget()!=self.msg and child.widget()!=self.remove):
                child.widget().deleteLater()
            else: break
        self.layout.addWidget(self.row("MIME:","%s/%s"%(k,type)))
        self.layout.addWidget(self.row("File:",", ".join(self.parent.os.mimes[k][str(type)])))
        self.layout.addWidget(self.msg)
        self.layout.addWidget(self.remove)
        self.msg.setText("")
        self.type=type
        self.k=k
class Title(QLabel):
    def __init__(self,text):
        super(Title,self).__init__(text)
class Remove(QPushButton):
    def __init__(self,parent):
        super(Remove,self).__init__("Remove")
        self.parent=parent
    def mouseReleaseEvent(self,event):
        try:
            self.parent.parent.os.removeIcon(self.parent.k,self.parent.type)
            self.parent.msg.setText("Icon removed")
            self.parent.parent.icon.icon.renderer=None
            self.parent.parent.icon.update()
        except:
            self.parent.msg.setText("Could not remove icon")
