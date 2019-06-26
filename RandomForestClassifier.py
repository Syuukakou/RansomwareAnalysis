'''
1. 用OneVsRestClassifier和RandomForestClassifier对数据进行分类
2. 数据用train_test_split进行分割，7：3
3. 分类后输出结果和混淆矩阵，并输出feature_importances_
'''


import numpy as np
import csv
from numpy import *
import pandas as pd
import seaborn as sn
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import train_test_split
from yellowbrick.classifier import ClassificationReport
import matplotlib.pyplot as plt

from sklearn.metrics import log_loss

all_data = pd.read_csv(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature_importance.csv",header=None)
	# 将csv转为矩阵
allData_matrix = all_data.as_matrix()
feature_names = allData_matrix[0]
allData_matrix = np.delete(allData_matrix, 0, axis=0)
feature_names = feature_names[:-1]
# 生成标签矩阵
allDataLabel_matrix = allData_matrix[:, 55]

# 从原始矩阵中剔除标签，保留数据
allData_matrix = np.delete(allData_matrix, 55, axis=1)
data_train, data_test, label_train, label_test = train_test_split(allData_matrix,allDataLabel_matrix,test_size=0.3, random_state=0)
tree_number = 10
classifier = OneVsRestClassifier(RandomForestClassifier(random_state=0,n_estimators=tree_number))
classifier.fit(data_train,label_train)
feim_list = []
for tree in range(tree_number):
	'''
	此处采用OneVsRestClassifier来对每个家族来说重要的API进行打分。
	思路：
	①首先第一次分类，标签为Benign，那么对于Benign的分类来说，哪个API对分类来说比较重要，并输出分数列表
	②同时输出分类标签
	'''
	print(classifier.estimators_[tree].feature_importances_)
	print(classifier.classes_[tree])
	feim_list = (classifier.estimators_[tree].feature_importances_)
	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature importances for each label-split.csv", "a+", newline="") as f:
			writer = csv.writer(f, dialect="excel")
			writer.writerow(feim_list)
print(feim_list)
result_pred = classifier.predict(data_test)
print(classifier.score(data_test,label_test))
print(classification_report(label_test,result_pred))
print("-------------------------")
confusion_array = confusion_matrix(label_test,result_pred)
print(confusion_array)
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


classes = ["Benign","Cerber","CryptoWall","CryptoLocker","Genasom","Jigsaw","Locky","Petya","Reveton","TeslaCrypt"]

visualizer = ClassificationReport(classifier, classes = classes, support=True)
visualizer.fit(data_train,label_train)
visualizer.score(data_test,label_test)
g = visualizer.poof()
# log_loss(label_test,clf_probs)