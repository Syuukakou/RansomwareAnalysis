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
# RenameMoveFile.rename_move(r"E:\PycharmWorkSpace\RansomwareAnalysis\Report\BenginSoftware",
# 							 "E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Bengin Software")
# with open("E:\PycharmWorkSpace\RansomwareAnalysis\Data_corrcoef.csv","a+",newline="") as f:
# 	writer = csv.writer(f,dialect="excel")
# 	writer.writerow(["file-crypt","file-register","file-socket","crypt-register","crypt-socket","register-socket","label"])
# print("--------------------提取json文件的API，并计算各类api之间的corrceof相关系数并输出至csv文件-------------------")
GetJsonAPI.GetAPI(r"E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Bengin Software")
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
'''
'''
Test Data Path
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\BenignSoftware
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\Cerber
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\CryptoLocker
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\CryptoWall
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\GenVirus
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\Jigsaw
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\Locky
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\Petya
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\Reveton
E:\PycharmWorkSpace\RansomwareAnalysis\TestDataJsonFile\TeslaCrypt
'''
