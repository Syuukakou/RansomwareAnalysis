import numpy as np
import pandas as pd
import json
import os
import csv
from pprint import pprint
from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt

from sklearn.multiclass import OneVsRestClassifier



#提取API频率到同一个csv文件中
api_list = [{"FindNextFile":0,"FindFirstFile":0,"FindFirstFileEx":0,"SetFilePointer":0,"SetFilePointerEx":0,"GetFileSize":0,"GetFileSizeEx":0,
			"SetFileAttributes":0, "GetFileType":0,"CopyFileEx":0,"CopyFile":0,"DeleteFile":0,"EncryptFile":0,"NtReadFile":0,"NtWriteFile":0,
			 "GetFileAttributes":0,"GetFileAttributesEx":0},
			{"CryptDeriveKey":0, "CryptDecodeObject":0, "CryptGenKey":0, "CryptImportPublicKeyInfo":0, "CryptAcquireContext":0,"CryptAcquireContextW":0},
			{"RegCloseKey":0,"RegCreateKeyExW":0,"RegDeleteKeyW":0,"RegQueryValueExW":0,"RegSetValueExW":0,
				"RegEnumKeyExA":0,"RegOpenKeyExW":0,"NtQueryValueKey":0,"NtOpenKey":0},
			{"socket":0, "InternetOpen":0,"shutdown":0,"sendto":0,"connect":0,"bind":0,"listen":0,"accept":0,"recv":0,"send":0,
				"InternetOpenUrl":0,"InternetReadFile":0,"InternetWriteFile":0},
			{"CreateThread":0,"CreateRemoteThread":0,"NtResumeThread":0,"NtGetContextThread":0,"NtSetContextThread":0,"CreateProcessInternalW":0,
			 "NtOpenProcess":0,"Process32NextW":0,"Process32FirstW":0,"NtTerminateProcess":0}]
def GetAPI(filepath):
	list = os.listdir(filepath)
	for i in range(len(list)):
		print()
		path = os.path.join(filepath,list[i])
		if os.path.isfile(path):
			with open(path) as file:
				files_list = []
				crypt_list = []
				register_list = []
				socket_list = []
				importance_list = []
				process_list = []
				jf = json.load(file)
				apistats = jf["behavior"]["apistats"]
				for pro_id in apistats:
					for api_name in apistats[pro_id]:
						#匹配各组的API，匹配到了则将API的调用次数提取
						if api_name in api_list[0]:
							api_list[0][api_name] += int(apistats[pro_id][api_name])
						if api_name in api_list[1]:
							api_list[1][api_name] += int(apistats[pro_id][api_name])
						if api_name in api_list[2]:
							api_list[2][api_name] += int(apistats[pro_id][api_name])
						if api_name in api_list[3]:
							api_list[3][api_name] += int(apistats[pro_id][api_name])
						if api_name in api_list[4]:
							api_list[4][api_name] += int(apistats[pro_id][api_name])
				print("---------------------API executed succeed!!!!!!-------------------------------")
				# 获取api_list中最长元素的长度
				# print(api_list)
				# 将api的频率抽出，并存入各自的列表中
				for fileAPI in api_list[0]:
					files_list.append(api_list[0][fileAPI])
				for cryptAPI in api_list[1]:
					crypt_list.append(api_list[1][cryptAPI])
				for regAPI in api_list[2]:
					register_list.append(api_list[2][regAPI])
				for socketAPI in api_list[3]:
					socket_list.append(api_list[3][socketAPI])
				for processAPI in api_list[4]:
					process_list.append(api_list[4][processAPI])
				print(files_list, crypt_list, register_list, socket_list,process_list)
				print("-----------------Saved API's frequencies into list succeed!!!!!!-----------------")
				importance_list.extend(files_list)
				importance_list.extend(crypt_list)
				importance_list.extend(register_list)
				importance_list.extend(socket_list)
				importance_list.extend(process_list)
				'''
				Cerber	CryptoLocker CryptoWall Genasom Jigsaw Locky Petya Reveton Teslacrypt Benign
				'''
				importance_list.append("Benign")
				print("----------importanve_list")
				print(importance_list)
				print("Over")
				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature_importance.csv", "a+", newline="") as file:
					writer = csv.writer(file, dialect="excel")
					writer.writerow(importance_list)




if __name__ == "__main__":
	apiname_list = ["FindNextFile","FindFirstFile","FindFirstFileEx","SetFilePointer","SetFilePointerEx","GetFileSize","GetFileSizeEx",
			"SetFileAttributes", "GetFileType","CopyFileEx","CopyFile","DeleteFile","EncryptFile","NtReadFile","NtWriteFile",
			 "GetFileAttributes","GetFileAttributesEx",
			"CryptDeriveKey", "CryptDecodeObject", "CryptGenKey", "CryptImportPublicKeyInfo", "CryptAcquireContext","CryptAcquireContextW",
			"RegCloseKey","RegCreateKeyExW","RegDeleteKeyW","RegQueryValueExW","RegSetValueExW",
				"RegEnumKeyExA","RegOpenKeyExW","NtQueryValueKey","NtOpenKey",
			"socket", "InternetOpen","shutdown","sendto","connect","bind","listen","accept","recv","send",
				"InternetOpenUrl","InternetReadFile","InternetWriteFile",
			"CreateThread","CreateRemoteThread","NtResumeThread","NtGetContextThread","NtSetContextThread","CreateProcessInternalW",
			 "NtOpenProcess","Process32NextW","Process32FirstW","NtTerminateProcess"]
	# with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature_importance.csv", "a+", newline="") as f:
	# 	writer = csv.writer(f, dialect="excel")
	# 	writer.writerow(apiname_list)
	# GetAPI("E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Bengin Software")

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
	numbertree = 10
	classifier = OneVsRestClassifier(RandomForestClassifier(random_state=0, n_estimators=numbertree))

	# classifier = RandomForestClassifier(random_state=0, n_jobs=-1)
	classifier.fit(allData_matrix, allDataLabel_matrix)
	feim_list = []
	#写入文件
	# with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature importances for each label.csv", "a+",
	# 		  newline="") as f:
	# 	writer = csv.writer(f, dialect="excel")
	# 	writer.writerow(apiname_list)
	for tree in range(numbertree):
		'''
		此处采用OneVsRestClassifier来对每个家族来说重要的API进行打分。
		思路：
		①首先第一次分类，标签为Benign，那么对于Benign的分类来说，哪个API对分类来说比较重要，并输出分数列表
		②同时输出分类标签
		'''
		print(classifier.estimators_[tree].feature_importances_)
		print(classifier.classes_[tree])
		feim_list = (classifier.estimators_[tree].feature_importances_)
	# 	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature importances for each label.csv", "a+", newline="") as f:
	# 		writer = csv.writer(f, dialect="excel")
	# 		writer.writerow(feim_list)


