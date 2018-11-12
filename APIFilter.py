import csv
import pandas as pd
import numpy as np
from pprint import pprint
# api_list = []
files_api = ["FindNextFile","FindFirstFile","FindFirstFileEx","SetFilePointer","SetFilePointerEx", "GetFileSize","GetFileSizeEx",
			"SetFileAttributes", "GetFileType","CopyFileEx","CopyFile","DeleteFile","EncryptFile","NtReadFile","NtWriteFile"]
crypt_api = ["CryptDeriveKey", "CryptDecodeObject", "CryptGenKey", "CryptImportPublicKeyInfo", "CryptAcquireContext","CryptAcquireContextW"]
register_api = ["RegCloseKey","RegCreateKeyExW","RegDeleteKeyW","RegQueryValueExW","RegSetValueExW","RegEnumKeyExA","RegOpenKeyExW"]
internet_api = ["socket", "InternetOpen","shutdown","sendto","connect"]
with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\sample_api_statistic\Cerber_apistats.csv") as f:
	reader = csv.reader(f)
	data_as_list = list(reader)
	print(len(data_as_list))
file_rows = (len(data_as_list))/2
# filted_api_list = [[] for _ in range(int(file_rows))]
filted_files = []
filted_crypt = []
filted_register = []
filted_internet = []
for json_list in range(len(data_as_list)):
	if json_list % 2 == 0:
		# print(data_as_list[json_list])
		row_num = int(json_list / 2)
		# print("++++++++++++++++++++++++++++++++++++++++++++")
		# filted_api_list.append(data_as_list[json_list][0])
		for api_name, frequence in zip(data_as_list[json_list],data_as_list[json_list+1]):
			# if api_name in api_list:
			# 	filted_api_list[row_num].append((api_name,frequence))
			if api_name in files_api:
				filted_files.append((api_name,frequence))
			if api_name in crypt_api:
				filted_crypt.append((api_name,frequence))
			if api_name in register_api:
				filted_register.append((api_name,frequence))
			if api_name in internet_api:
				filted_internet.append((api_name,frequence))
# print("files api:  ",filted_files)
filted_files_dataframe = pd.DataFrame(filted_files)
filted_files_dataframe.to_csv(r"E:\PycharmWorkSpace\RansomwareAnalysis\filted_apis_csv\files_api.csv", index = False, header = False)
print("Filted files api wrote to csv file successfully")
# print("crypt api:  ",filted_crypt)
filted_crypt_dataframe = pd.DataFrame(filted_crypt)
filted_crypt_dataframe.to_csv(r"E:\PycharmWorkSpace\RansomwareAnalysis\filted_apis_csv\crypt_api.csv", index = False, header = False)
print("Filted crypt api wrote to csv file successfully")
# print("register:",filted_register)
filted_register_dataframe = pd.DataFrame(filted_register)
filted_register_dataframe.to_csv(r"E:\PycharmWorkSpace\RansomwareAnalysis\filted_apis_csv\register_api.csv", index = False, header = False)
print("Filted register api wrote to csv file successfully")
# print("internet:",filted_internet)
filted_internet_dataframe = pd.DataFrame(filted_internet)
filted_internet_dataframe.to_csv(r"E:\PycharmWorkSpace\RansomwareAnalysis\filted_apis_csv\internet_api.csv", index = False, header = False)
print("Filted internet api wrote to csv file successfully")