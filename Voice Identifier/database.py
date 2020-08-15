# -*- coding: utf-8 -*-
"""
Created on Fri May 22 02:09:55 2020

@author: Mohamed Hany
"""
from importing import dataset
from Splitter import splitter
from Recorder import recorder
from importnewdata import d
from detection import svmselector
#from importnewdata import d
import os,glob
class DataBase:
    def __init__(self,filename):
        self.dataset=filename
    def record(self,usname,time):
        recorder.recording(usname,time)
    def sp(self,usname):
        splitter.splitting(usname)
    def collectdata(self,usname):
        os.remove(usname+".wav")
        i = dataset.collectsf(usname)
        if os.path.exists("wav"):
            try:
                oldpath=os.getcwd()
                os.chdir("wav")
                path=os.getcwd()
            except:
                print("could not change directory")
            for filename in glob.glob(os.path.join(path,'*.wav')):
                os.remove(filename)
            try:
                os.chdir(oldpath)
                os.rmdir("wav")
                print("Directory Changed and delete the files")
                
            except:
                print("coudl not change directory")
        else:
            os.mkdir("wav")
        return i
    def testdata(self):
        try:
            os.remove("NA.wav")
        except:
            pass
        i = d.collectsf()
        if os.path.exists("wav"):
            try:
                oldpath=os.getcwd()
                os.chdir("wav")
                path=os.getcwd()
            except:
                print("could not change directory")
            for filename in glob.glob(os.path.join(path,'*.wav')):
                os.remove(filename)
            try:
                os.chdir(oldpath)
                os.rmdir("wav")
                print("Directory Changed and delete the files")
                
            except:
                print("coudl not change directory")
        else:
            os.mkdir("wav")
        print("number of recognized rows = "+str(i))
        return i
    def detect(self):
        return svmselector.selecting()
        