#1，将所有实验样本的api统计数据输出到同一个csv文件中，index设置为各个样本的哈希值
#2，再通过遍历文件夹来读取各自的api数据的同时，来筛选需要的api数据
#---------------------------------------------
# 1，一个样本的親プロセス,定义为所有进程树中，children数最多的那个进程。
# 2，example.json ==> behavior ==> processtree ==> processtree[i] ==> children[....]
# 3，条件：①processtree[i]必须有children，②children内容非空，即children中还有其他进程
import json
import os
import pandas as pd
from nested_lookup import get_occurrence_of_key #返回嵌套字典中某个key的出现次数

def GetPProcesAPIStats(filepath,apistats_filename):
	list = os.listdir(filepath)
	process_max = {}
	for i in range(len(list)):
		path = os.path.join(filepath, list[i])
		if os.path.isfile(path):
			with open(path) as jfile:
				process_dict = {}  # 存储list[i]和其对应的json文件的親プロセス的api统计数据
				jf = json.load(jfile)
				jf_processtree = jf["behavior"]["processtree"]
				for process_id in range(len(jf_processtree)):
					# get_occurrence_of_key(jf_processtree[process_id],"children")返回嵌套字典中children的出现次数
					#将当前json文件中所有的process的children出现的次数统计后，赋给process_dict
					process_dict[jf_processtree[process_id]["pid"]] = get_occurrence_of_key(jf_processtree[process_id],
																							"children")
				try:
					process_max[list[i]] = max(process_dict,key=process_dict.get)  # 将list[i]和其对应的json文件的childern数最多的親プロセス的pid传入process_max字典中
					print(list[i], "==> complete!!!")
				except KeyError:
					print(list[i],"'s process ",max(process_dict,key=process_dict.get)," don;t have api calls!!PLEASE CHECK THIS FILE'S PROCESSES")
	print("~~~~~~~~~~~~~~~~~~~~~~~~~\nOutput json file's process id whose child's count is maximum!!")
	print(process_max)  # key是文件名，value是各自文件的親プロセス的id。====》{1.json:2376,.......}
	print("##############c#################################################################")
	for maxprocess_id in process_max:
		with open(filepath + "/" + maxprocess_id) as j_file:
			jfname = json.load(j_file)
			print(maxprocess_id, "'s parent process's id is ",process_max[maxprocess_id]," and api calls statistics:")  # Output json file name
			try:
				api_tmp = jfname["behavior"]["apistats"][
					str(process_max[maxprocess_id])]  # 将process_max[maxprocess_id]即进程id转换为字符串进行传值
				df = pd.DataFrame.from_dict(api_tmp, orient="index").T.to_csv(apistats_filename, index=True,
																			  index_label=str(maxprocess_id),
																			  mode="a+")  # mode="a+"表示追加数据，不会覆盖前面的数据
				print(process_max[maxprocess_id], "==> Write to CSV file succeed!!!!!")
			except KeyError:
				print(maxprocess_id, "'s process ", process_max[maxprocess_id],
					  " don;t have api calls!!PLEASE CHECK THIS FILE'S PROCESSES")
