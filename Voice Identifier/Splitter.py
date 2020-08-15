# -*- coding: utf-8 -*-
"""
Created on Sat May  2 01:04:00 2020

@author: aa
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:01:46 2020

@author: aa
"""
from pydub import AudioSegment
import wave
import os
class splitter:
    def splitting(filename):
        t1=0
        t2=3000
        wavfile = wave.open(filename+".wav")#HERE
        frames = wavfile.getnframes()
        rate = wavfile.getframerate()
        duration = frames/float(rate)
        newAudio = AudioSegment.from_wav(filename+".wav")
        oldpath = os.getcwd()
        try:
            os.mkdir("wav")
            os.chdir("wav")
            newAudio.export(filename+".wav", format="wav")
            print("Directory Changed")
            
        except:
            print("coudl not change directory")
        for i in range(int(duration)):
            newAudio = AudioSegment.from_wav(filename+".wav")
            newAudio = newAudio[t1:t2]
            newaudname= filename+str(i)+".wav"
            newAudio.export(newaudname, format="wav") #Exports to a wav file in the current path.
            t1 = t2     #Works in milliseconds
            t2 = t2 + 3000 #every 1k = 1 second
            print("t1 = "+str(t1))
            print("t2 = "+str(t2))
            seconds = t2/1000
            print(seconds)
            if seconds>duration:
                break;
            
        try:
            os.chdir(oldpath)
            print("Directory Changed")
        except:
            print("coudl not change directory")
        #newAudio.close()
        wavfile.close()
        
#os.rmdir('Christmas 2017')
#s = splitter()
#s.splitting("MZH3")
#os.remove("newMZH.wav")        
#os.mkdir("wav")