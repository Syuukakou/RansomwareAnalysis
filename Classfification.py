import csv
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, RepeatedKFold
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.svm import SVC
from pprint import pprint
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

train_data = pd.read_csv("E:\PycharmWorkSpace\RansomwareAnalysis\Train_Data.csv",header=None)
trainData_matrix = train_data.as_matrix()
trainDataLabel_matrix = trainData_matrix[:,10]
trainData_matrix = np.delete(trainData_matrix,10,axis=1)
# print(trainData_matrix)
# print(trainDataLabel_matrix)
test_data = pd.read_csv("E:\PycharmWorkSpace\RansomwareAnalysis\Test_Data.csv",header=None)
testData_matrix = test_data.as_matrix()
testDataLabel_matrix = testData_matrix[:,10]
testData_matrix = np.delete(testData_matrix,10,axis=1)

all_data = pd.read_csv("E:\PycharmWorkSpace\RansomwareAnalysis\All_Data.csv",header=None)
#将csv转为矩阵
allData_matrix = all_data.as_matrix()
#生成标签矩阵
allDataLabel_matrix = allData_matrix[:,10]
#从原始矩阵中剔除标签，保留数据
allData_matrix = np.delete(allData_matrix,10,axis=1)


#------------------------------------------------------------------------------------------

#数据分割，用作参数最优化
data_train, data_test, label_train, label_test = train_test_split(allData_matrix,allDataLabel_matrix,test_size=0.3, random_state=0)
#设定参数优化范围
# tuned_parameters = [
# 	{"C":[1,10,100,1000], "kernel":["linear"]},
# 	{"C":[1,10,100,1000], "kernel":["rbf"], "gamma":[0.001,0.0001]},
# 	{"C":[1,10,100,1000], "kernel":["poly"], "degree":[2,3,4], "gamma":[0.001,0.0001]},
# 	{"C":[1,10,100,1000], "kernel":["sigmoid"], "gamma":[0.001,0.0001]}
# ]
# score = "f1"
# clf = GridSearchCV(
# 	SVC(),
# 	tuned_parameters,
# 	cv=5,
# 	scoring="%s_weighted" % score
# )
# clf.fit(trainData_matrix,trainDataLabel_matrix)
# # print(clf.grid_scores_)
# print(clf.best_params_)
#
#
# print("# Tuning hyper-parameters for %s" % score)
# print()
# print("Best parameters set found on development set: %s" % clf.best_params_)
# print()
#
# print("Grid scores on development set:")
# print()
# # for params, mean_score, scores in clf.grid_scores_:
# # 	print("%0.3f (+/-%0.03f) for %r" % (mean_score, scores.std() * 2, params))
# print()
#
# print("The scores are computed on the full evaluation set.")
# print()
# y_true, y_pred = label_test, clf.predict(data_test)
# print(classification_report(y_true, y_pred))

# cross-validation
clf = svm.SVC(kernel="linear",C=10)
cv = ShuffleSplit(n_splits=5,test_size=0.3,random_state=0)
scores = cross_val_score(clf, allData_matrix,allDataLabel_matrix,cv=cv)
print("Cross-Validation scores: {}".format(scores))
print("Average score:".format(np.mean(scores)))



#-----------------------------------------------------------------------------------------------------------------
# #SVM
#将数据随机分为 训练数据：测试数据 = 7 ：3
# data_train, data_test, label_train, label_test = train_test_split(allData_matrix,allDataLabel_matrix,test_size=0.3, random_state=0)
# classifier = svm.SVC(kernel="linear",C=10)
# classifier.fit(data_train,label_train)
# result_true, result_pred = label_test, classifier.predict(data_test)
# print("-->Dataset: ")
# print("Cerber:\t\t247",end="\t")
# print("CryptoLocker:\t12")
# print("CrytoWall:\t49",end="\t")
# print("Genasom:\t\t25")
# print("Jigsaw:\t\t16",end="\t")
# print("Locky:\t\t\t334")
# print("Petya:\t\t6",end="\t")
# print("Reveton:\t\t126")
# print("TeslaCrypt:\t65",end="\t")
# print("Benign:\t\t\t230")
# print()
# print("-->Classification Result:")
# print(classification_report(result_true,result_pred))
# print("-->F1 value: ",classifier.score(data_test,label_test))
