_author_ = "Ninad"

from pathlib import Path
import os

path = "C:/Users/nsapa/Dropbox/R/Admin/RA Bible/"


# List of path to all the files
allPathList = []
for root, directories,files in os.walk(path):
    for name in files:
        p = os.path.join(root, name)
        allPathList.append(os.path.abspath( p ))


with open("RABibleTOC"+".txt", "w") as f:
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = '\t' * level
        depth = '*' * level
        depthDir = format(depth+os.path.basename(root))
        parentDir = format(indent +depthDir)
        print(parentDir, file=f)
        subindent = '\t' * (level + 1)
        for file in files:
            printSubDir = format(subindent+file)
            print(printSubDir, file=f)
        print('\n',file=f)


#------------ The following code derives Table of content for only one level-----------------#

#Fetch all the directories for the path
# root, directories,files = os.walk(path).__next__()
#
# # Add all the documents under each folder into a dictionary
# toc_dict = dict()
# for dirs in directories:
#     f = os.walk(os.path.join(path, dirs)).__next__()
#     toc_dict[dirs] = f[2]

# with open("RABibleTOC"+".txt", "w") as f:
#     for folder,files in toc_dict.items():
#         print(folder+'\n', file=f)
#         print('\n\n')
#         for file in files:
#             print('\t'+file, file=f)
#         print('\n\n\n', file=f)
