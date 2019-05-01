import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
diabetes = pd.read_csv('diabetes.csv')
print(diabetes.columns) 

diabetes_mod = diabetes[(diabetes.BloodPressure != 0) & (diabetes.BMI != 0) & (diabetes.Glucose != 0)]

feature_names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
X = diabetes_mod[feature_names]
y = diabetes_mod.Outcome

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify = diabetes_mod.Outcome, random_state=66)

#import modules
import os
os.system('color 3f')

from sklearn.ensemble import GradientBoostingClassifier

#this module use for speaking
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

#select algo
model = GradientBoostingClassifier()

#fit into the model
model.fit(X_train,y_train)

#oututs
print('WelCome to Diabetes Prediction Software') #greeting
speak.Speak('WelCome to Diabetes Prediction Software')

#input format: 2,148,72,35,0,33.6,0.627,50
print("Enter Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age 'with comma'")
# speak.Speak("Enter Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age 'with comma'")
val = list(input().split(","))
pred = model.predict([val])
print(pred)

if pred == [1]:
    print('You Have Diabetes')
    speak.Speak('You Have Diabetes')
    print('You need to take this medicine')
    speak.Speak('You need to take this medicine')
    print('Alpha-glucosidase inhibitors, Biguanides, Dopamine agonist, DPP-4 inhibitors, Meglitinides')
    speak.Speak('Alpha-glucosidase inhibitors, Biguanides, Dopamine agonist, DPP-4 inhibitors, Meglitinides')
    print('And immediate contact to your doctor')
    speak.Speak('and immediate contact to your doctor')

else:
    print('You have not Diabetes')
    speak.Speak('You have not Diabetes')