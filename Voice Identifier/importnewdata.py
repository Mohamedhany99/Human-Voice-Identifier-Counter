# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 03:19:33 2020

@author: aa
"""

import os,glob
#from scipy.io.wavfile import read
from scipy.io import wavfile
from scipy.stats import skew
from scipy.stats import kurtosis
import xlwt
from xlwt import Workbook
import xlrd
from xlutils.copy import copy
import pandas as pd
import numpy as np
import re

#path = 'F:\BUE\Year 3 ( Senior)\Graduation Project\Projects\Audio Splitter\MH'

def clearing():
        wb = Workbook()
        sheet = wb.add_sheet("sheet 1")
        #Name	mean	variance	Minimum Value	Maximum Value	Median	Kurtosis	Skewness	Frequency
        sheet.write(0,0,"Name")
        sheet.write(0,1,"mean")
        sheet.write(0,2,"variance")
        sheet.write(0,3,"Minimum Value")
        sheet.write(0,4,"Maximum Value")
        sheet.write(0,5,"Median")
        sheet.write(0,6,"Kurtosis")
        sheet.write(0,7,"Skewness")
        sheet.write(0,8,"Frequency")
        wb.save("tester.xls")
#extracting frequency function
def frequency(frate,data):
    data = np.array(data)
    w = np.fft.fft(data)
    freqs =0
    freqs = np.fft.fftfreq(len(w))
    idx = np.argmax(np.abs(w))
    freq = freqs[idx]
    freq_in_hertz = abs(freq * frate)
    #print(freq_in_hertz)
    return freq_in_hertz

class d:    
    def collectsf():
        #setting excel paramaters
        clearing()
        print("cleared and moving on")
        wb = Workbook()
        sheet = wb.add_sheet("sheet 1")
        rb = xlrd.open_workbook("tester.xls",formatting_info=True)
        r_sheet=rb.sheet_by_index(0)
        r= r_sheet.nrows
        wb=copy(rb)
        i=0
#        setting path of recorded data folder
        print("setting path")
        oldpath = os.getcwd()
        try:
            os.chdir("wav")
            print("Directory Changed")
        except:
            print("could not change directory")
        path = os.getcwd()
        #iterating through files in wav
        for filename in glob.glob(os.path.join(path,'*.wav')):
#            reading the wav files stored at the database of sounds
#            reading the wav files stored at the database of sounds
            try:
                i+=1
                frate , data = wavfile.read(filename)
                    #fname = filename.replace(path , "")
                    #looping through the single wav file
                    #for i in range(len(data)):
                        #storing the data in a numpy array as a float datatype to extract sound features
                        #data = np.array(data[i],dtype=float)
                data = np.array(data)
                freq = frequency(frate,data)
                    #extracting sound features
                    #editing kurtosis output
                kurt=''
                kurt = str(kurtosis(data))
                kurt = kurt.replace('[',"")
                kurt=kurt[0:9]
                    #editing skewness output
                skk=''
                skk = str(skew(data))
                skk = skk.replace('[',"")
                skk=skk[0:9]
                    
                    #array of data = [ mean , variance , minimum , maximum , median , kurtosis , Skewness , Frequency ]
                arrofdata =0
                arrofdata=[np.mean(data) , np.var(data) , str(np.min(data)) , str(np.max(data)) , np.median(data), kurt, skk, freq]
                print("data stored in array")
                    #importing data into excel sheet
                sheet = wb.get_sheet(0)
                    
                sheet.write(r,0,"NA")
                sheet.write(r,1,arrofdata[0])
                sheet.write(r,2,arrofdata[1])
                sheet.write(r,3,arrofdata[2])
                sheet.write(r,4,arrofdata[3])
                sheet.write(r,5,arrofdata[4])
                sheet.write(r,6,arrofdata[5])
                sheet.write(r,7,arrofdata[6])
                sheet.write(r,8,arrofdata[7])
                r = r+1
            except:
                print("could not read so i passed it")
                pass
        try:
            os.chdir(oldpath)
            print("dir is here: "+os.getcwd())
            print("Directory Changed")
        except:
            print("coudl not change directory")
        print("saved")
        wb.save("tester.xls")
        return i
