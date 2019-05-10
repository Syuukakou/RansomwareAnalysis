import csv
import pandas as pd
import APIlist
import numpy as np
from pprint import pprint

'''
提取report.csv中的crypt_api，register_api,files_api,socket_api
'''

# files_api = ["FindNextFile","FindFirstFile","FindFirstFileEx","SetFilePointer","SetFilePointerEx", "GetFileSize","GetFileSizeEx",
# 			"SetFileAttributes", "GetFileType","CopyFileEx","CopyFile","DeleteFile","EncryptFile","NtReadFile","NtWriteFile",
# 			 "GetFileAttributes","GetFileAttributesEx"]
# crypt_api = ["CryptDeriveKey", "CryptDecodeObject", "CryptGenKey", "CryptImportPublicKeyInfo", "CryptAcquireContext","CryptAcquireContextW"]
# register_api = ["RegCloseKey","RegCreateKeyExW","RegDeleteKeyW","RegQueryValueExW","RegSetValueExW",
# 				"RegEnumKeyExA","RegOpenKeyExW","NtQueryValueKey","NtOpenKey"]
# internet_api = ["socket", "InternetOpen","shutdown","sendto","connect","bind","listen","accept","recv","send",
# 				"InternetOpenUrl","InternetReadFile","InternetWriteFile"]
with open(r"E:\迅雷下载\585524\report.csv") as f:
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
		row_num = int(json_list / 2)
		for api_name, frequence in zip(data_as_list[json_list],data_as_list[json_list+1]):
			if api_name in APIlist.files_api:
				filted_files.append((api_name,frequence))
				print("file api succeed")
			if api_name in APIlist.crypt_api:
				filted_crypt.append((api_name,frequence))
				print("crypt api succeed")
			if api_name in APIlist.register_api:
				filted_register.append((api_name,frequence))
				print("register api succeed")
			if api_name in APIlist.internet_api:
				filted_internet.append((api_name,frequence))
				print("internet api succeed")
filted_files_dataframe = pd.DataFrame(filted_files)
filted_crypt_dataframe = pd.DataFrame(filted_crypt)
filted_register_dataframe = pd.DataFrame(filted_register)
filted_internet_dataframe = pd.DataFrame(filted_internet)
excel_writer = pd.ExcelWriter(r"E:\迅雷下载\585524\reports.xlsx")
filted_files_dataframe.to_excel(excel_writer,"files API")
filted_crypt_dataframe.to_excel(excel_writer,"crypt API")
filted_register_dataframe.to_excel(excel_writer,"register API")
filted_internet_dataframe.to_excel(excel_writer,"internet API")
excel_writer.save()