# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 20:17:45 2020

@author: Mohamed Hany
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
from sklearn.metrics import accuracy_score
newdata = pd.read_excel("tester.xls")
data = pd.read_excel("Dataset.xls")
ndata = newdata.drop('Name',axis=1)
noname = data.drop('Name',axis=1)
namecol =data['Name']
X_train, X_test, y_train, y_test = train_test_split(noname, namecol, test_size = 0.20)
svclassifier = SVC(kernel='rbf')#,degree=8
svclassifier.fit(X_train, y_train)

def make_decision(arr):
    fperc=0
    sperc=0
    fch=arr[0]
    for i in range(len(arr)):
        if(arr[i]==fch):
            fperc+=1
        else:
            sch=arr[i]
            sperc+=1
    if fperc>sperc:
        return fch
    else:
        return sch
class svmselector:
    def selecting():        
        try:
            identity=[]
            for i in range(10):
                y_pred = svclassifier.predict(ndata)
                print(y_pred)
    #            print(classification_report(y_test,y_pred))
                finaldec= make_decision(y_pred)
                identity.append(finaldec)
            
            return finaldec
        except:
            print("empty data")
            return 'Not Recognized'
print(svmselector.selecting())