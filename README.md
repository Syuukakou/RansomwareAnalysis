# RansomwareAnalysis
papers' code
RenameMoveFile.py:

1，先遍历文件夹，将report下的renport.json文件重命名为该样本的md5值

2，再遍历文件夹，将所有样本的report下的“md5”.json文件移动到pycharm的工作空间内，以便提取api统计数据

GetPPAPIstatis.py:获取特定文件下的所有Json文件的父进程API的statistic

ExecuteAPI.py:提取特定文件夹下的所有Json文件的所有进程的所有API

APIFilter.py:提取report.csv中的crypt_api，register_api,files_api,socket_api

GetJsonAPI:

1，遍历特定文件夹下的所有Json文件
           
2，抽取json文件的["behavior"]["apistats"]下的所有进程的crypt_api，register_api,files_api,socket_api

3，计算2中的四类api之间的corrceof系数，并输出至csv文件

cuckoosandbox-json-instructure.txt:

cuckoo sandbox的解析报告report.json的文件构造（各种属性）

ransomware download website.txt:ransomware下载网址
