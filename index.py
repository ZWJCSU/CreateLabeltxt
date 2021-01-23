import os
import numpy as np

root = "/Users/zwj/Desktop/UCMerced_LandUse/Images"

#构建所有文件名的列表，dir为label
filename = []
#label = []
dirs = os.listdir(root)
i=0
train = []
test = []
i=0
for dir in dirs:

    dir_path = root + '/' + dir
    names = os.listdir(dir_path)
    for n in (names[:int(len(names) * 0.8)]):
        train.append('data/UCMerced_LandUse/Images/' +dir+ '/' + n + '\t'+str(i))
    for m in (names[int(len(names) * 0.8):]):
        test.append('data/UCMerced_LandUse/Images/'+dir+ '/' + m + '\t'+str(i))
    i = i + 1
#打乱文件名列表

#划分训练集、测试集，默认比例4:1
# train = filename[:int(len(filename) * 0.8)]
# test = filename[int(len(filename) * 0.8):]

#分别写入train.txt, test.txt
with open('train.txt', 'w') as f1, open('test.txt', 'w') as f2:
    for i in train:
        f1.write(i + '\n')
    for j in test:
        f2.write(j + '\n')

print('成功！')
