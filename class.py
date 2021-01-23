import os
import numpy as np

root = "/Users/zwj/Desktop/UCMerced_LandUse/Images"

#构建所有文件名的列表，dir为label
filename = []
#label = []
dirs = os.listdir(root)
for dir in dirs:
    # dir_path = root + '/' + dir
    # names = os.listdir(dir_path)
    # for n in names:
    #     filename.append(dir_path + '/' + n + '\t')


# #打乱文件名列表
# np.random.shuffle(filename)
#划分训练集、测试集，默认比例4:1
# train = filename[:int(len(filename)*0.8)]
# test = filename[int(len(filename)*0.8):]

#分别写入train.txt, test.txt
# with open('train.txt', 'w') as f1, open('test.txt', 'w') as f2:
#     for i in train:
#         f1.write(i + '\n')
#     for j in test:
#         f2.write(j + '\n')
with open('class.txt','w') as f1:
    for i in filename:
        f1.write(i+'\n')


print('成功！')
