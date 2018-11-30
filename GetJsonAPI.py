import json
import pandas as pd
import os
import csv
import numpy as np
from numpy import *
from scipy.stats import pearsonr
from pprint import pprint

#初始化各个API的频率为0
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
# pearson_list = []

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
				corrcoef_list = []
				process_list = []
				jf = json.load(file)
				apistats = jf["behavior"]["apistats"]
				for pro_id in apistats:
					for api_name in apistats[pro_id]:
						#匹配各组的API，匹配到则 +1
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
				print(api_list)
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
				print(files_list, crypt_list, register_list, socket_list)
				print("-----------------Saved API's frequencies into list succeed!!!!!!-----------------")
				# 将list转换为数组
				files_arr = np.array(files_list)
				crypt_arr = np.array(crypt_list)
				register_arr = np.array(register_list)
				socket_arr = np.array(socket_list)
				process_arr = np.array(process_list)
				print("--------------------Converted list to array Succeed !!!!!!!!---------------------")
				arrary_size = max(len(x) for x in api_list)
				# 将所有数组大小统一，不足处补零
				files_arr = np.pad(files_arr, (0, arrary_size - len(files_list)), "constant")
				crypt_arr = np.pad(crypt_arr, (0, arrary_size - len(crypt_list)), "constant")
				register_arr = np.pad(register_arr, (0, arrary_size - len(register_list)), "constant")
				socket_arr = np.pad(socket_arr, (0, arrary_size - len(socket_list)), "constant")
				process_arr = np.pad(process_arr, (0, arrary_size - len(process_list)), "constant")

				print("----------Arranged array and add zeros to the end of array Succeed!!!!-----------")
				fc_corr = np.corrcoef(files_arr, crypt_arr)		#计算filesAPI和CryptAPI之间的相关系数
				fr_corr = np.corrcoef(files_arr, register_arr)	#计算filesAPI和RegisterAPI之间的相关系数
				fs_corr = np.corrcoef(files_arr, socket_arr)	#计算filesAPI和SocketAPI之间的相关系数
				fp_corr = np.corrcoef(files_arr,process_arr)	#计算filesAPI和ProcessAPI之间的相关系数
				cr_corr = np.corrcoef(crypt_arr, register_arr)	#计算CryptAPI和RegisterAPI之间的相关系数
				cs_corr = np.corrcoef(crypt_arr, socket_arr)	#计算CryptAPI和SocketAPI之间的相关系数
				cp_corr = np.corrcoef(crypt_arr,process_arr)	#计算CryptAPI和ProcessAPI之间的相关系数
				rs_corr = np.corrcoef(register_arr, socket_arr)	#计算RegisterAPI和SocketAPI之间的相关系数
				rp_corr = np.corrcoef(register_arr,process_arr)	#计算RegisterAPI和ProcessAPI之间的相关系数
				sp_corr = np.corrcoef(socket_arr,process_arr)	#计算SocketAPI和ProcessAPI之间的相关系数
				'''
				np.corrcoef()函数返回变量之间的相关系数矩阵。
				相关系数矩阵形式如下：
				[ 1.        , -0.05640533],
       			[-0.05640533,  1.        ]
				'''
				#取结果矩阵的第0行第一个数。
				corrcoef_list.append(fc_corr[0][1])
				corrcoef_list.append(fr_corr[0][1])
				corrcoef_list.append(fs_corr[0][1])
				corrcoef_list.append(cr_corr[0][1])
				corrcoef_list.append(cs_corr[0][1])
				corrcoef_list.append(rs_corr[0][1])
				corrcoef_list.append(fp_corr[0][1])
				corrcoef_list.append(cp_corr[0][1])
				corrcoef_list.append(rp_corr[0][1])
				corrcoef_list.append(sp_corr[0][1])
				'''
				Blocker:1	Teslacrypt:2	Cerber:3	CryptoLocker:4	CryptoWall:5
				Jigsaw:8	Reveton:9	Petya:10	Locky:11	Genasom:12
				normal:0
				'''
				#判断corrcoef_list中是否有数为NAN，有则更换为0
				for i in range(len(corrcoef_list)):
					if isnan(corrcoef_list[i]):
						corrcoef_list[i] = 0
				corrcoef_list.append("benign")#添加标签
				print(corrcoef_list)
				#将结果写入文件
				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\All_Data.csv", "a+",newline="") as f:
					writer = csv.writer(f, dialect="excel")
					# writer.writerow(["file-crypt","file-register","file-socket","crypt-register","crypt-socket","register-socket","label"])
					writer.writerow(corrcoef_list)
		# print(list[i]," Wrote to file succeed!!!!")
# with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Cerber\0b7f65d8f39ef6c5abd03be5a8687d70.json") as f:
