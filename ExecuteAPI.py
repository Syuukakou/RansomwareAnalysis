'''

提取特定文件夹下的所有Json文件的所有进程的所有API

'''


import json
import os
import pandas as pd
def ExecuteAPI(filepath,apistats_filename):
	list = os.listdir(filepath)
	all_api_list = []
	for i in range(len(list)):
		path = os.path.join(filepath, list[i])
		if os.path.isfile(path):
			with open(path) as jfile:
				# process_dict = {}
				jf = json.load(jfile)
				# jf_processtree = jf["behavior"]["processtree"]
				for pro_num in jf["behavior"]["apistats"]:
					all_api_list.append(jf["behavior"]["apistats"][pro_num])
				print("Execute ",list[i],"'s All API succeed!!")
	print("##############c#################################################################")
	for pid in range(len(all_api_list)):
		df = pd.DataFrame.from_dict(all_api_list[pid],orient="index").T.to_csv(apistats_filename,index=False,mode="a+")
		print(pid," Wrote to csv file succeed!!")