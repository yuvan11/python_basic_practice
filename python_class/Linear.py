import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

data=pd.read_csv("student-mat.csv", sep=';')
print(data.head())
data=data[["G1","G2","G3","studytime","failures","absences"]]
# # print(data.head())
predict="G3"
# # print(predict)
X=np.array(data.drop([predict],1))
Y=np.array(data[predict])
X_train,X_test,Y_train,Y_test= sklearn.model_selection.train_test_split(X,Y,test_size=0.1)
best=0

for _ in range(30):

    X_train,X_test,Y_train,Y_test= sklearn.model_selection.train_test_split(X,Y,test_size=0.1)

    linear=linear_model.LinearRegression()

    linear.fit(X_train,Y_train)
    acc=linear.score(X_test,Y_test)

    print(acc)
    if acc>best:
        best=acc
        with open("studentmodel.pickle", "wb") as f:
            pickle.dump(linear, f)

pickle_in = open("studentmodel.pickle","rb")
linear=pickle.load(pickle_in)

print("co_eff:",linear.coef_)
print("intercept:",linear.intercept_)

predictions = linear.predict(X_test)

for x in range(len(predictions)):
    print(predictions[x],X_test[x],Y_test[x])

p="G1"
style.use("ggplot")
plt.scatter(data[p],data["G3"])
plt.xlabel(p)
plt.ylabel("Final grade")
plt.show()

