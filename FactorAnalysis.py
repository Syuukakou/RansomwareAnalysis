import json
import csv
from numpy import *
import os
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

def GetAPITest(filepath):
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
				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\fileapi.csv", "a+",newline="") as file:
					writer = csv.writer(file, dialect="excel")
					writer.writerow(files_list)
				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\cryptapi.csv", "a+",newline="") as file:
					writer = csv.writer(file, dialect="excel")
					writer.writerow(crypt_list)
				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\registerapi.csv", "a+",newline="") as file:
					writer = csv.writer(file, dialect="excel")
					writer.writerow(register_list)
				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\socketapi.csv", "a+",newline="") as file:
					writer = csv.writer(file, dialect="excel")
					writer.writerow(socket_list)
				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\processapi.csv", "a+",newline="") as file:
					writer = csv.writer(file, dialect="excel")
					writer.writerow(process_list)



if __name__ == "__main__":
	# fileapi_analysis_path = "E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\CryptoWall\CryptoWall-fileapi.csv"
	# cryptapi_analysis_path = "E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\CryptoWall\CryptoWall-fileapi.csv"
	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\fileapi.csv", "a+",
			  newline="") as file:
		writer = csv.writer(file, dialect="excel")
		writer.writerow(
			["FindNextFile", "FindFirstFile", "FindFirstFileEx", "SetFilePointer", "SetFilePointerEx",
		 	 "GetFileSize", "GetFileSizeEx",
			 "SetFileAttributes", "GetFileType", "CopyFileEx", "CopyFile", "DeleteFile", "EncryptFile",
			 "NtReadFile", "NtWriteFile",
			 "GetFileAttributes", "GetFileAttributesEx"])
	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\cryptapi.csv", "a+",
			  newline="") as file:
		writer = csv.writer(file, dialect="excel")
		writer.writerow(
			["CryptDeriveKey", "CryptDecodeObject", "CryptGenKey", "CryptImportPublicKeyInfo", "CryptAcquireContext","CryptAcquireContextW"])
	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\registerapi.csv", "a+",
			  newline="") as file:
		writer = csv.writer(file, dialect="excel")
		writer.writerow(
			["RegCloseKey","RegCreateKeyExW","RegDeleteKeyW","RegQueryValueExW","RegSetValueExW",
				"RegEnumKeyExA","RegOpenKeyExW","NtQueryValueKey","NtOpenKey"])
	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\socketapi.csv", "a+",
			  newline="") as file:
		writer = csv.writer(file, dialect="excel")
		writer.writerow(
			["socket", "InternetOpen","shutdown","sendto","connect","bind","listen","accept","recv","send",
				"InternetOpenUrl","InternetReadFile","InternetWriteFile"])
	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\Factory Analysis\BenignSoftware\processapi.csv", "a+",
			  newline="") as file:
		writer = csv.writer(file, dialect="excel")
		writer.writerow(
			["CreateThread","CreateRemoteThread","NtResumeThread","NtGetContextThread","NtSetContextThread","CreateProcessInternalW",
			 "NtOpenProcess","Process32NextW","Process32FirstW","NtTerminateProcess"])
		# writer.writerow(
		# 	)
	GetAPITest("E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Bengin Software")