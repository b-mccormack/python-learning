import os

fileList = []
pathList = []
imgCount = 0
txtCount = 0
otherFileCount = 0

for root, dirs, files in os.walk("C:/Git/python-projects/CIT/session14/session-14-files"):
    for i in files:
        fileList.append(i)
    for i in files:
        pathList.append(os.path.join(root, i))

for i in fileList:
    fileExtension = i[-3:]
    if fileExtension == 'txt':
        txtCount += 1
    elif fileExtension == 'jpg':
        imgCount += 1
    else:
        otherFileCount += 1

print('The number of images is:',imgCount)
print('The number of txt files is:',txtCount)
print('The number of other files is:',otherFileCount)
print('The total number of files is:', (imgCount + txtCount + otherFileCount))


# print(fileList)
# print(pathList)
# numFiles = len(fileList)
# print("\nThe total number of files is", numFiles)



# file_count=0
# dir_count=0
# total=0

# for root,dirs,files in os.walk("C:\Git\python-projects\CIT\session14\session-14-files"):
#     print(root)
#     print(dirs)
#     print(files)

# all_dir = len(dirs)
# dir_count = dir_count + all_dir
# all_files = len(files)
# file_count = file_count + all_files
# total = total + all_dir + all_files
# print([total,file_count,dir_count])