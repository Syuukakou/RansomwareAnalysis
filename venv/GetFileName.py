import os
import os.path
from os.path import basename
import json
import shutil
import string
import random
import csv
def getname(path):
	allfile = []
	# rename_allfile = []
	for fpath, dirname, fnames in os.walk(path):#search file with"report.json"
		for f in fnames:
			b_name = os.path.splitext(os.path.basename(f))[0]
			allfile.append(b_name)
			print("Get name succeed")
	with open(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\TeslaCrypt_name.csv", "a+",newline="") as f:
		writer = csv.writer(f,dialect="excel")
		writer.writerow(allfile)
	for i in range(len(allfile)):
		print(allfile[i])