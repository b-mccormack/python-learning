import os

fileList = []
pathList = []

for root,dirs,files in os.walk("C:/Git/python-projects/CIT/session14/session-14-files"):
    for i in files:
        fileList.append(i)
    for i in files:
        pathList.append(os.path.join(root, i))

print(pathList)
for i in pathList:
    size = os.path.getsize(i)
    if size > 600000:
        print(i, "is over 600kb. Removing")
        os.remove(i)
