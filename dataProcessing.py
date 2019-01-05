# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# importing the library 
import  numpy as  np
import  matplotlib as plt
import pandas as  pd

# importing  data from  data file 

dataset=pd.read_csv('Data.csv')
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values

# handling the missing data ,missing  data  is replace by  mean  of coloumn

from sklearn.preprocessing import Imputer
imputer =Imputer(missing_values="NaN",strategy='mean',axis=0) 
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])


# categorical data ,encoding  into  LabelEncoder  and  OneHotEncoder



from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
labelencoder=LabelEncoder()
X[:,0]=labelencoder.fit_transform(X[:,0])
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()

labelencoder_y=LabelEncoder()
Y=labelencoder_y.fit_transform(Y)

#Splitting  the  data  set  into traing  set  and  test set

from  sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test =train_test_split(X,Y,test_size=0.2,random_state=0)


#feature scaling of  Data
from sklearn.preprocessing import StandardScaler

sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)









