#This is a quick tool for updating the folder dating convention from older versions of Lightroom Classic which are no longer supported and legacy organization conventions:
#"/year/month/year-month-day/."
#to match a naming convention which is currently supported with the current version of Lightroom Classic
#"/year/month/day/."

import os
import re

#LRpath = "/Volumes/4TB/Lightroom/LightroomMasters"
LRpath = input("Drag the LightroomMasters folder here")
LRpath = LRpath.strip('\'')

directory_list = list()
for root, dirs, files in os.walk(LRpath, topdown=False):
    for name in dirs:
        directory_list.append(os.path.join(root, name))

for i in range(len(directory_list)):

    if re.search(r"(\d{4}-\d{2}-\d{2})", directory_list[i]) is not None:

        folderstring = re.search(r"(\d{4}-\d{2}-\d{2})", directory_list[i]).group(1)
        newfolderstring = re.search(r"(?:\d{4}-\d{2}-)(\d{2})", folderstring).group(1)
        partialpath = re.search(r"(^.+?)(\d{4}-\d{2}-\d{2})", directory_list[i]).group(1)
        
        os.rename(directory_list[i], partialpath + newfolderstring)
