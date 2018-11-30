'''
1，先遍历文件夹，将report下的renport.json文件重命名为该样本的md5值
2，再遍历文件夹，将所有样本的report下的“md5”.json文件移动到pycharm的工作空间内，以便提取api统计数据
'''
import os
import os.path
import json
import shutil
import string
import random
# 1，先遍历文件夹，将report下的renport.json文件重命名为该样本的md5值
def rename_move(path,newpath,rule="report.json"):
	allfile = []
	# rename_allfile = []
	for fpath, dirname, fnames in os.walk(path):#search file with"report.json"
		for f in fnames:
			filename = os.path.join(fpath,f)
			if filename.endswith(rule):
				allfile.append(filename)
	for fs in allfile:#rename files
		try:
			with open(fs) as jsonfile:
				jf = json.load(jsonfile)
				file_md5 = jf["virustotal"]["md5"]
			# name_tmp = os.path.basename(fs)
			name_tmp = str(file_md5)+".json"
			dirname_tmp = os.path.dirname(fs)
			renamed_file = os.path.join(dirname_tmp,name_tmp)
			os.rename(fs,renamed_file)
			newfilepath = os.path.join(newpath,os.path.basename(renamed_file))
			#移动文件到新路径
			shutil.move(renamed_file,newfilepath)
			print(name_tmp," moved successfully!!!")
		except KeyError:
			# with open(fs) as jsonfile:
			# 	jf = json.load(jsonfile)
				# file_target = jf["target"]["human"]
			# name_tmp = file_target+".json"
			str_tmp = ''.join(random.sample(string.ascii_letters+string.digits,34))
			name_tmp = "Random_"+str_tmp+".json"
			newfilepath1 = os.path.join(newpath,name_tmp)
			shutil.move(fs, newfilepath1)
			print(name_tmp, " moved successfully!!!")

	return allfile

# oldpath = "E:\Program Files scholar\OneDrive\OneDrive - 東京電機大学\IOT43-SPT合同研究会\实验\论文实验最终数据收集（单次实验）\Petya"
# newpath = "E:\PycharmWorkSpace\RansomwareAnalysis\AnalysisReportJsonFile\Petya"
# if __name__ == "__main__":
# 	b = get_files(oldpath,newpath)
# 	for i in b:
# 		print(i)