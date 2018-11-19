import RenameMoveFile
import GetPPAPIStatis
import random
import string
from pandas import DataFrame
import pandas as pd

from scipy.stats import pearsonr
import numpy as np
import csv
import ExecuteAPI
import json
from pprint import  pprint
import GetJsonAPI
# print("---------------从解析报告中中提取report.json，并更名为当前样本的MD5值---------------")
# RenameMoveFile.rename_move(r"E:\PycharmWorkSpace\RansomwareAnalysis\Report\teslareport",
# 							 "E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\TeslaCrypt")
# GetPPAPIStatis.GetPProcesAPIStats("E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\GenVirus",
# 								  "E:\PycharmWorkSpace\RansomwareAnalysis\sample_api_statistic\Genasom_apistats.csv")
# print("--------------------------提取样本的所有API序列----------------------------------")
# ExecuteAPI.ExecuteAPI(r"E:\迅雷下载\585524\reports",
# 								  r"E:\迅雷下载\585524\report.csv")
# with open("E:\PycharmWorkSpace\RansomwareAnalysis\Data_corrcoef.csv","a+",newline="") as f:
# 	writer = csv.writer(f,dialect="excel")
# 	writer.writerow(["file-crypt","file-register","file-socket","crypt-register","crypt-socket","register-socket","label"])
GetJsonAPI.GetAPI(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\TeslaCrypt")