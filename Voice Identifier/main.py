# -*- coding: utf-8 -*-
"""
Created on Fri May 22 01:33:46 2020

@author: aa
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from database import DataBase
import speech_recognition as sr
import threading as thread
import time
import queue

class MainWindow(Screen):
    def rec(self):
        pass
class newsound(Screen):
    nm = ObjectProperty(None)
    #pb = ProgressBar(max=100)
    def recording(self):
        try:
            try:
                print(self.nm.text)
                print("try recording")
                db.record(self.nm.text,180)
                print("done recording")
                pop = Popup(title='Recorded Successfully',
                  content=Label(text='Recorded Successfuly and analysing now.'),
                  size_hint=(None, None), size=(400, 400))
                pop.open()
                #pb.value=33
            except:
                pop = Popup(title='Loss of data',
                  content=Label(text='There has to be an error with the recorded clip please refer to the instruction above and try again later'),
                  size_hint=(None, None), size=(400, 400))
                pop.open()
                return 0 
            print("start splitting")
            db.sp(self.nm.text)
            #pb.value=70
            print("done splitting")
            try:
                print("start analysing")
                i = db.collectdata(self.nm.text)
                if i<=19:
                    pop = Popup(title='Data Stored Successfully',
                      content=Label(text='your data had been stored successfuly You can try to use the detection method now'),
                      size_hint=(None, None), size=(400, 400))
                    pop.open()
                    #pb.value=100
                else:
                    pop = Popup(title='lake of data',
                      content=Label(text='your silence during the recording concluded of a data loss and some corruption,\n so please record again to add more data for more accuracy of detection'),
                      size_hint=(None, None), size=(400, 400))
                    pop.open()
                    return 0 
                print("done analysing")
            except:
                pop = Popup(title='Loss of data',
                  content=Label(text='It appears that there is a missing data or a probable loss of data please record again,\n and do not stay silent for more than 10 seconds.'),
                  size_hint=(None, None), size=(400, 400))
                return 0 
        except:
            pop = Popup(title='Error While Recording',
                  content=Label(text='There was a wrong in recording your voice\nplease follow the above steps.'),
                  size_hint=(None, None), size=(400, 400))
        
class detect(Screen):
    def rec(self):
        db.record("NA",9)
    def detection(self,buffer):
        db.sp("NA")
        j = db.testdata()
        try:
            name = db.detect()
            pop = Popup(title='Detected',
                   content=Label(text=name),
                   size_hint=(None, None), size=(400, 400))
            pop.open()
            return name
        except:
            print("passed")
            pass
    def check(self):
        try:
            r= sr.Recognizer()
            with sr.Microphone() as source:
                print("say smth")
                audio =r.listen(source)
                query = r.recognize_google(audio)
                print(query)
            return query
        except:
            return 'n'
    
    def det(self):
#        pop = Popup(title='Detection',
#                       content=Label(text="Say Start to start the detecting method"),
#                       size_hint=(None, None), size=(400, 400))
#        pop.open()
#        try:
#            comm = self.check()
#        except:
#            pop = Popup(title='Detection',
#                       content=Label(text="Cannot Hear your voice check your microphone and restart the App please"),
#                       size_hint=(None, None), size=(400, 400))
#            pop.open()
#        if 'start' in comm.lower():
#            time.sleep(2)
#            newt = thread.Thread(target=self.updatepop("updated and say start again"))
#            exc = thread.Thread(target=self.updatepop("updated and say for the second time"))
#            
#            newt.start()
#                
#            time.sleep(60)
#            if newt.is_alive()==False:
#                exc.start()
#            s =0
#            identities=[]
#            while s<=60:    
                p1 = thread.Thread(target=self.rec)
                que = queue.Queue()
                p2 = thread.Thread(target=lambda q, arg1: q.put(self.detection(arg1)), args = (que,'test'))#p2 = thread.Thread(target=self.detection)
                p1.start()
                p1.join()
                p2.start()
                p2.join()
                result = que.get()
#                if result not in identities:
#                    identities.append(result)
#                else:
#                    pass
#                s+=10
#            print(len(identities))
#        else:
##            pop.content=Label(text="Please Say (Start) to start detecting.")
#            self.det()
    def updatepop(self,cont):
        print("hi")
        pop = Popup(title='Detection',
                       content=Label(text=cont),
                       size_hint=(None, None), size=(400, 400))
        pop.open
        self.add_widget(pop)
        
#        pop.content=Label(text=cont)   
            
#        else:
#            self.det()
class WindowManager(ScreenManager):
    pass

db = DataBase("Dataset.xls")
kv = Builder.load_file("mykv.kv")
class MyMainApp(App):
    def build(self):
        return kv
if __name__ == "__main__":
    MyMainApp().run()