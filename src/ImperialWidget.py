from osinterface import OsInterface
from description import DescWidget
from mimebar import MimeBarWidget
from iconslot import IconSlot
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Startup
class ImperialWidget(QWidget):
    def __init__(self):
        super(ImperialWidget,self).__init__()
        self.setWindowTitle("Imperial")
        self.painter=QPainter()
        self.resize(900,600)
        self.layout=QVBoxLayout()
        self.setLayout(self.layout)
        self.layout.setMargin(0)
        self.load=LoadWidget()
        self.layout.addWidget(self.load)
        self.show()

        QTimer.singleShot(1000,self.finishLoading)
    def finishLoading(self):
        self.layout.removeWidget(self.load)
        self.layout.addLayout(MainLayout(OsInterface()))
        self.load.deleteLater()
class LoadWidget(QFrame):
    def __init__(self):
        super(LoadWidget,self).__init__()
        self.icon=QIcon("assets/imperial-icon.svg").pixmap(QSize(100,100))
        self.painter=QPainter()
        self.pen=QPen()
    def paintEvent(self,event):
        h=self.height()
        w=self.width()
        self.painter.begin(self)
        self.painter.setPen(self.pen)
        #self.painter.fillRect(0,0,w,h,LoadWidget.BG)
        self.painter.drawPixmap((w/2)-50,(h/2)-55,100,100,self.icon)
        self.painter.drawText((w/2)-50,(h/2)+60,100,25,Qt.AlignCenter,"Loading...")
        self.painter.end()

# Post-load
class MainLayout(QGridLayout):
    def __init__(self,os):
        super(MainLayout,self).__init__()
        self.os=os
        self.mime=MimeBarWidget(self)
        self.desc=DescWidget(self)
        self.icon=IconSlot(self)
        self.addWidget(self.mime,0,0,6,1)# MIME bar
        self.addWidget(self.desc,4,1,2,3)# Description
        self.addWidget(self.icon,1,2,2,1)# Icon
        self.setSpacing(0)
        self.setMargin(0)
