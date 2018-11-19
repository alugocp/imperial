from ImperialWidget import ImperialWidget
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

if __name__=="__main__":
    # Load stylesheet
    style=QFile("src/style.css")
    style.open(QFile.ReadOnly)

    app=QApplication(sys.argv)
    app.setStyleSheet(QString.fromAscii(style.readAll().data()))
    style.close()
    widget=ImperialWidget()
    sys.exit(app.exec_())
