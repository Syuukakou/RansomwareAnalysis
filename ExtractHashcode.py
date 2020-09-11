import os
import json
import csv
file_folder =[r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\Blocker",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\Blocker",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\Cerber",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\CryptoLocker",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\CryptoWall",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\GenVirus",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\Jigsaw",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\Locky",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\Petya",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\Reveton",r"F:\RansomwareAnalysisDataset\AnalysisReportJsonFile\TeslaCrypt"]

for folder_num in range(len(file_folder)):
    variant_name = []
    variant_name.append(file_folder[folder_num])
    with open(r"F:\RansomwareAnalysisDataset\hash_code.csv","a+",newline="") as f:
        writer = csv.writer(f,dialect="excel")
        writer.writerow(variant_name)
    file_list = os.listdir(file_folder[folder_num])
    for file_num in range(len(file_list)):
        file_hash = []
        path = os.path.join(file_folder[folder_num],file_list[file_num])
        base = os.path.basename(path)
        file_hash.append(os.path.splitext(base)[0])
        with open(r"F:\RansomwareAnalysisDataset\hash_code.csv","a+",newline="") as f:
            writer = csv.writer(f, dialect="excel")
            writer.writerow(file_hash)

#file_list = os.listdir(file_folder)
#for i in range(len(file_list)):
  #  file_hash = [] 
   # path = os.path.join(file_folder, file_list[i])
    #base = os.path.basename(path)
   # file_hash.append(os.path.splitext(base)[0])

    #with open(r"F:\RansomwareAnalysisDataset\Blocker_hashcode.csv", "a+", newline="") as f:
     #   writer = csv.writer(f, dialect="excel")
      #  writer.writerow(file_hash)
