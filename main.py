import RenameMoveFile
import GetPPAPIStatis
import random
import string
from pandas import DataFrame
import pandas as pd
from scipy.stats import pearsonr
import numpy as np
import csv
import TestCode
import json
from pprint import  pprint
import GetFileName
import seaborn as sn
import matplotlib.pyplot as plt

import GetJsonAPI

import ExtractCryptAPI
# print("---------------从解析报告中中提取report.json，并更名为当前样本的MD5值---------------")
# RenameMoveFile.rename_move(r"E:\PycharmWorkSpace\RansomwareAnalysis\Report\CryptoLocker",
# 							 r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\added Cryptolocker")
# with open("E:\PycharmWorkSpace\RansomwareAnalysis\Data_corrcoef.csv","a+",newline="") as f:
# 	writer = csv.writer(f,dialect="excel")
# 	writer.writerow(["file-crypt","file-register","file-socket","crypt-register","crypt-socket","register-socket","label"])
# print("--------------------提取json文件的API，并计算各类api之间的corrceof相关系数并输出至csv文件-------------------")
# GetJsonAPI.GetAPI(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Cryptolocker")

# GetFileName.getname(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\TeslaCrypt")

# ExtractCryptAPI.ExtractAPI(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Bengin Software")

'''
Training Data path
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Bengin Software
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Cerber
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\CryptoLocker
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\CryptoWall
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\GenVirus
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Jigsaw
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Locky
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Petya
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Reveton
E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\TeslaCrypt

E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\CryptoLocker
'''

'''
可视化feature_importances_
'''
# data = pd.read_csv(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature importances for each label for plot y.csv",header=None)
data = pd.read_csv(r"E:\PycharmWorkSpace\RansomwareAnalysis\feature importance\feature importances for each label-split.csv",header=None)

data_matrix = data.as_matrix()
print(np.shape(data_matrix))
new_data_matrix = np.rot90(data_matrix,1)
print(np.shape(new_data_matrix))
#10， 55
#55， 10

df_cm = pd.DataFrame(new_data_matrix,
			# 		 index = ["Benign","Cerber","CryptoWall","CryptoLocker","Genasom","Jigsaw","Locky","Petya","Reveton","TeslaCrypt"],
			# 		 columns= ["FindNextFile","FindFirstFile","FindFirstFileEx","SetFilePointer","SetFilePointerEx","GetFileSize","GetFileSizeEx",
			# "SetFileAttributes", "GetFileType","CopyFileEx","CopyFile","DeleteFile","EncryptFile","NtReadFile","NtWriteFile",
			#  "GetFileAttributes","GetFileAttributesEx",
			# "CryptDeriveKey", "CryptDecodeObject", "CryptGenKey", "CryptImportPublicKeyInfo", "CryptAcquireContext","CryptAcquireContextW",
			# "RegCloseKey","RegCreateKeyExW","RegDeleteKeyW","RegQueryValueExW","RegSetValueExW",
			# 	"RegEnumKeyExA","RegOpenKeyExW","NtQueryValueKey","NtOpenKey",
			# "socket", "InternetOpen","shutdown","sendto","connect","bind","listen","accept","recv","send",
			# 	"InternetOpenUrl","InternetReadFile","InternetWriteFile",
			# "CreateThread","CreateRemoteThread","NtResumeThread","NtGetContextThread","NtSetContextThread","CreateProcessInternalW",
			#  "NtOpenProcess","Process32NextW","Process32FirstW","NtTerminateProcess"]
			index = ["FindNextFile","FindFirstFile","FindFirstFileEx","SetFilePointer","SetFilePointerEx","GetFileSize","GetFileSizeEx",
			"SetFileAttributes", "GetFileType","CopyFileEx","CopyFile","DeleteFile","EncryptFile","NtReadFile","NtWriteFile",
			 "GetFileAttributes","GetFileAttributesEx",
			"CryptDeriveKey", "CryptDecodeObject", "CryptGenKey", "CryptImportPublicKeyInfo", "CryptAcquireContext","CryptAcquireContextW",
			"RegCloseKey","RegCreateKeyExW","RegDeleteKeyW","RegQueryValueExW","RegSetValueExW",
				"RegEnumKeyExA","RegOpenKeyExW","NtQueryValueKey","NtOpenKey",
			"socket", "InternetOpen","shutdown","sendto","connect","bind","listen","accept","recv","send",
				"InternetOpenUrl","InternetReadFile","InternetWriteFile",
			"CreateThread","CreateRemoteThread","NtResumeThread","NtGetContextThread","NtSetContextThread","CreateProcessInternalW",
			 "NtOpenProcess","Process32NextW","Process32FirstW","NtTerminateProcess"],
					 columns= ["Benign","Cerber","CryptoWall","CryptoLocker","Genasom","Jigsaw","Locky","Petya","Reveton","TeslaCrypt"]
					 )
plt.figure(figsize=(7,11))
sn.heatmap(df_cm, cmap="Blues",annot=False,linewidths=.5)#将fmt参数设为g，则可以取消科学计数法
plt.title("Feature Importances")
plt.ylabel("Families")
plt.xlabel("API")
plt.show()
