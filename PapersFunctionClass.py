import json
import shutil
from nested_lookup import get_occurrence_of_key
import os
import pandas as pd
class Paper_Function(object):
	def __init__(self, filepath,apistats_filename,path,newpath):
		self.filepath = filepath
		self.apistats_filename = apistats_filename
		self.path = path
		self.newpath = newpath
	# 1，将所有实验样本的api统计数据输出到同一个csv文件中，index设置为各个样本的哈希值
	# 2，再通过遍历文件夹来读取各自的api数据的同时，来筛选需要的api数据
	# ---------------------------------------------
	# 1，一个样本的親プロセス,定义为所有进程树中，children数最多的那个进程。
	# 2，example.json ==> behavior ==> processtree ==> processtree[i] ==> children[....]
	# 3，条件：①processtree[i]必须有children，②children内容非空，即children中还有其他进程
	# 父进程的ppid是不在apistats中的
	def GetPProcesAPIStats(self,filepath, apistats_filename):
		list = os.listdir(filepath)
		process_max = {}  # 存储list[i]和其对应的json文件的親プロセス的api统计数据
		for i in range(len(list)):
			path = os.path.join(filepath, list[i])
			if os.path.isfile(path):
				with open(path) as jfile:
					process_dict = {}
					jf = json.load(jfile)
					jf_processtree = jf["behavior"]["processtree"]
					for process_id in range(
							len(jf_processtree)):  # 当ppid不在apistats，且pid不在["500","388", "496"]之内，则执行取id操作。
						if (((jf_processtree[process_id]["ppid"] in jf["behavior"]["apistats"]) == False) and (
								jf_processtree[process_id]["pid"] in ["500", "388", "496"]) == False):
							process_dict[int(jf_processtree[process_id]["pid"])] = get_occurrence_of_key(
								jf_processtree[process_id], "children")
					# process_max[list[i]] = max(process_dict, key=process_dict.get)
					if (process_dict[max(process_dict, key=process_dict.get)] == 0):  # 当children的数量为零时
						print(process_dict)
						process_max[list[i]] = str(sorted(process_dict.keys(), reverse=True)[0])
					else:  # 否则取当前的children数最多的id，此时可能会出现多个id拥有最大的children数。所以取其中id最大的（2376：3，1264：3 时取2376）
						print(process_dict)
						maxValue = max(process_dict.values())
						maxValuelist = [k for k, v in process_dict.items() if v == maxValue]
						maxValuelist = sorted(maxValuelist, reverse=True)
						process_max[list[i]] = maxValuelist[0]
					print("Get ", list[i], "'s MaxChildren's process_id ", process_max[list[i]], " ==> complete!!!")

		print(process_max)  # key是文件名，value是各自文件的親プロセス的id。====》{1.json:2376,.......}
		print("##############c#################################################################")
		for maxprocess_id in process_max:
			with open(filepath + "/" + maxprocess_id) as j_file:
				jfname = json.load(j_file)
				print(maxprocess_id, "'s parent process's id is ", process_max[maxprocess_id],
					  " and api calls statistics:")  # Output json file name
				try:
					api_tmp = jfname["behavior"]["apistats"][
						str(process_max[maxprocess_id])]  # 将process_max[maxprocess_id]即进程id转换为字符串进行传值
					df = pd.DataFrame.from_dict(api_tmp, orient="index").T.to_csv(apistats_filename, index=True,
																				  index_label=str(maxprocess_id),
																				  mode="a+")  # mode="a+"表示追加数据，不会覆盖前面的数据
					print(process_max[maxprocess_id], "==> Write to CSV file succeed!!!!!")
				except KeyError:
					print(maxprocess_id, ".json ==>", process_max[maxprocess_id], " isn't in apistats")

	'''
	1，先遍历文件夹，将report下的renport.json文件重命名为该样本的md5值
	2，再遍历文件夹，将所有样本的report下的“md5”.json文件移动到pycharm的工作空间内，以便提取api统计数据
	'''
	# 1，先遍历文件夹，将report下的renport.json文件重命名为该样本的md5值
	def rename_move(self,path, newpath, rule="report.json"):
		allfile = []
		# rename_allfile = []
		for fpath, dirname, fnames in os.walk(path):  # search file with"report.json"
			for f in fnames:
				filename = os.path.join(fpath, f)
				if filename.endswith(rule):
					allfile.append(filename)
		for fs in allfile:  # rename files
			try:
				with open(fs) as jsonfile:
					jf = json.load(jsonfile)
					file_md5 = jf["virustotal"]["md5"]
				# name_tmp = os.path.basename(fs)
				name_tmp = str(file_md5) + ".json"
				dirname_tmp = os.path.dirname(fs)
				renamed_file = os.path.join(dirname_tmp, name_tmp)
				os.rename(fs, renamed_file)
				newfilepath = os.path.join(newpath, os.path.basename(renamed_file))
				shutil.move(renamed_file, newfilepath)
				print(name_tmp, " moved successfully!!!")
			except KeyError:
				with open(fs) as jsonfile:
					jf = json.load(jsonfile)
					file_target = jf["target"]["human"]
				name_tmp = file_target + ".json"
				newfilepath1 = os.path.join(newpath, name_tmp)
				shutil.move(fs, newfilepath1)
				print(name_tmp, " moved successfully!!!")

		return allfile
