# -*- coding: utf-8 -*-
"""Major project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DZCtOaxS6sb-PkJWS-5bZcpS4A8lOBgJ

**B** **Kalyani** **Reddy**

**1**. **Decision Tree Classification**
"""

import pandas as pd
import numpy as np
import matplotlib as mtb

df = pd.read_excel("/Date_fruits_dataset.xlsx")
df.head()

df.shape

df.isnull().sum()

df.dtypes

from sklearn.preprocessing import LabelEncoder

df['Class'].value_counts()

lb = LabelEncoder()
df['Class'] = lb.fit_transform(df['Class'])
df['Class'].value_counts()

x = df.iloc[:,:-1]
y = df.iloc[:,-1]
x.head()

y.head()
print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split

x_tr,x_te,y_tr,y_te = train_test_split(x,y,test_size=0.2)
x_tr.head()

print(x_tr.shape)
print(x_te.shape)

from sklearn.tree import DecisionTreeClassifier

DTC = DecisionTreeClassifier()
DTC.fit(x_tr,y_tr)
print("training_score",DTC.score(x_tr,y_tr))
print("test_score",DTC.score(x_te,y_te))

y_pred = DTC.predict(x_te)
y_pred

x_te['yactual'] = y_te
x_te['ypred'] = y_pred
x_te.head()

from sklearn.metrics import classification_report,confusion_matrix

cr = classification_report(y_te,y_pred)
print(cr)

cm = confusion_matrix(y_te,y_pred)
print(cm)

"""**2. Random forest classification**"""

from sklearn.ensemble import RandomForestClassifier

RFC = RandomForestClassifier(n_estimators=250)

x_tr,x_te,y_tr,y_te = train_test_split(x,y,test_size=0.2)
x_tr.head()

RFC.fit(x_tr,y_tr)

RFC.score(x_te,y_te)

rfc_predict = RFC.predict(x_te)
rfc_predict

print(classification_report(y_te,rfc_predict))

print(confusion_matrix(y_te,rfc_predict))

"""**3. KNN classification**"""

from sklearn.neighbors import KNeighborsClassifier

knc = KNeighborsClassifier(n_neighbors=30)
knc.fit(x_tr,y_tr)
print(knc.score(x_te,y_te))

knc_predict = knc.predict(x_te)
print(knc_predict)

print(confusion_matrix(y_te,knc_predict))

print(classification_report(y_te,knc_predict))

"""**4. LogisticRegression**"""

from sklearn.linear_model import LogisticRegression
lg = LogisticRegression()

lg.fit(x_tr,y_tr)
print(lg.score(x_te,y_te))

lg_predict = lg.predict(x_te)

print(lg_predict)

print(confusion_matrix(y_te,lg_predict))

print(classification_report(y_te,lg_predict))

"""**CONCLUSION:** Random Forest Classification has more accuracy score than any other classification model. Hence Random Forest Classification can be used for predicting the type of date fruits."""

