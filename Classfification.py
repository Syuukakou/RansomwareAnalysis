import csv
import pandas as pd
import numpy as np
import seaborn as sn
from sklearn import linear_model
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split, RepeatedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn import svm
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import ExtraTreesClassifier

from yellowbrick.classifier import ClassificationReport


from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.svm import SVC
from pprint import pprint
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

np.set_printoptions(suppress = True)
#
# train_data = pd.read_csv("E:\PycharmWorkSpace\RansomwareAnalysis\Train_Data.csv",header=None)
# trainData_matrix = train_data.as_matrix()
# trainDataLabel_matrix = trainData_matrix[:,10]
# trainData_matrix = np.delete(trainData_matrix,10,axis=1)
# # print(trainData_matrix)
# # print(trainDataLabel_matrix)
# test_data = pd.read_csv("E:\PycharmWorkSpace\RansomwareAnalysis\Test_Data.csv",header=None)
# testData_matrix = test_data.as_matrix()
# testDataLabel_matrix = testData_matrix[:,10]
# testData_matrix = np.delete(testData_matrix,10,axis=1)

all_data = pd.read_csv("E:\PycharmWorkSpace\RansomwareAnalysis\All_Data.csv",header=None)
#将csv转为矩阵
allData_matrix = all_data.as_matrix()
#生成标签矩阵
allDataLabel_matrix = allData_matrix[:,10]
#从原始矩阵中剔除标签，保留数据
allData_matrix = np.delete(allData_matrix,10,axis=1)


#------------------------------------------------------------------------------------------
#
# # 数据分割，用作参数最优化
# data_train, data_test, label_train, label_test = train_test_split(allData_matrix,allDataLabel_matrix,test_size=0.1, random_state=0)
# # 设定参数优化范围
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
# clf.fit(data_train,label_train)
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
#
# # cross-validation
# clf = svm.SVC(kernel="linear",C=1000)
# cv = ShuffleSplit(n_splits=5,test_size=0.3,random_state=0)
# scores = cross_val_score(clf, allData_matrix,allDataLabel_matrix,cv=cv)
# print("Cross-Validation scores: {}".format(scores))
# print("Average score:".format(np.mean(scores)))
# #


#-----------------------------------------------------------------------------------------------------------------
#SVM
# 将数据随机分为 训练数据：测试数据 = 7 ：3
data_train, data_test, label_train, label_test = train_test_split(allData_matrix,allDataLabel_matrix,test_size=0.3, random_state=0)
classifier = svm.SVC(kernel="linear",C=1000, class_weight="balanced")
classifier.fit(data_train,label_train)
result_true, result_pred = label_test, classifier.predict(data_test)

classes = ["Benign","Cerber","CryptoWall","CryptoLocker","Genasom","Jigsaw","Locky","Petya","Reveton","TeslaCrypt"]

print("-->Dataset: ")
print("Cerber:\t\t247",end="\t")
print("CryptoLocker:\t20")
print("CrytoWall:\t47",end="\t")
print("Genasom:\t\t25")
print("Jigsaw:\t\t29",end="\t")
print("Locky:\t\t\t334")
print("Petya:\t\t6",end="\t")
print("Reveton:\t\t126")
print("TeslaCrypt:\t65",end="\t")
print("Benign:\t\t\t241")
print()
print("-->Classification Result:")
print(classification_report(result_true,result_pred))
print("-->F1 value: ",classifier.score(data_test,label_test))

#---------------------------------------------------------------------------
'''
print confusion metrix
'''
confusion_array = confusion_matrix(label_test,result_pred)
print(confusion_array)
print(confusion_matrix(label_test, result_pred).ravel())
df_cm = pd.DataFrame(confusion_array,
					 index = ["Benign","Cerber","CryptoWall","CryptoLocker","Genasom","Jigsaw","Locky","Petya","Reveton","TeslaCrypt"],
					 columns=["Benign","Cerber","CryptoWall","CryptoLocker","Genasom","Jigsaw","Locky","Petya","Reveton","TeslaCrypt"])
sn.set(font_scale=1.5)
plt.figure(figsize=(9,7))
sn.heatmap(df_cm, cmap="Blues",annot=True, fmt="g")#将fmt参数设为g，则可以取消科学计数法
plt.title("SVM Linear Kernel \nAccuracy: {0:.3f}".format(accuracy_score(label_test,result_pred)))
plt.ylabel("True label")
plt.xlabel("Predicted label")
plt.show()

#此处的classes的标签必须和classifier的标签一致
visualizer = ClassificationReport(classifier, classes = classes, support=True)
visualizer.fit(data_train,label_train)
visualizer.score(data_test,label_test)
g = visualizer.poof()
#------------------------------------------------------------------------------------
