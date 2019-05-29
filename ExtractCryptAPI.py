import json
import csv
import os
from numpy import *

cryptAPI = {"CryptDeriveKey":0, "CryptDecodeObject":0, "CryptGenKey":0, "CryptImportPublicKeyInfo":0,
			"CryptAcquireContext":0,"CryptAcquireContextW":0}

def ExtractAPI(filepath):
	list = os.listdir(filepath)
	for i in range(len(list)):
		print()
		path = os.path.join(filepath,list[i])
		if os.path.isfile(path):
			with open(path) as file:
				cryptapi_num = []
				jf = json.load(file)
				apistats = jf["behavior"]["apistats"]
				for pro_id in apistats:
					for api_name in apistats[pro_id]:
						if api_name in cryptAPI:
							cryptAPI[api_name] += int(apistats[pro_id][api_name])
				print("---------------------------API extracted succeed!!!-------------------------")
				print(cryptAPI)
				for cryptapi in cryptAPI:
					cryptapi_num.append(cryptAPI[cryptapi])
				print(cryptapi_num)
				cryptapi_num.append("Bengin")

				with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\CryptoFunction specialized classification\features.csv", "a+", newline="") as f:
					writer = csv.writer(f, dialect="excel")
					writer.writerow(cryptapi_num)

