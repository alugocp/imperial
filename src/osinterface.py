from subprocess import Popen,PIPE
from os.path import expanduser
from shutil import copyfile
import os

class OsInterface:
    def __init__(self):
        self.theme=ThemeData()
        self.mimes=MimeSet()
        self.fromFile("/etc/mime.types")
        self.fromFile(expanduser("~/.local/share/mime/types"))
    def addIcon(self,path,k,file):
        copyfile(path,"%s/mimes/scalable/%s-%s.svg"%(self.theme.themepath,k,file))
        return Popen(["gtk-update-icon-cache","%s"%(self.theme.themepath)]).wait()==0
    def removeIcon(self,k,file):
        os.remove("%s/mimes/scalable/%s-%s.svg"%(self.theme.themepath,k,file))
        return Popen(["gtk-update-icon-cache","%s"%(self.theme.themepath)]).wait()==0
    def getIcon(self,type,file):
        path="%s/mimes/scalable/%s-%s.svg"%(self.theme.themepath,type,file)
        if(os.path.isfile(path)): return path
    def fromFile(self,filepath):
        file=open(filepath,"r")
        for l in file:
            l=l.strip()
            if(len(l)>0 and l[0]!="#"):
                l=l.split("\t")
                if(len(l)>1): self.mimes.add(l[0],l[-1].split(" "))
# Themes
class ThemeData:
    def __init__(self):
        self.theme=Popen(
            ["gsettings","get","org.gnome.desktop.interface","icon-theme"],stdout=PIPE
        ).stdout.read().strip().replace("'","")
        self.themepath="/usr/share/icons/%s"%(self.theme)

# MIMEs
class MimeSet:
    def __init__(self):
        self.hash={}
        self.__len__=self.hash.__len__
        self.__getitem__=self.hash.__getitem__
        self.__iter__=self.hash.__iter__
    def add(self,mime,filetypes):
        mime=mime.split("/")
        if(mime[0] in self.hash):
            if(not mime[1] in self.hash[mime[0]]):
                self.hash[mime[0]][mime[1]]=filetypes
        else:
            self.hash[mime[0]]={mime[1]:filetypes}
