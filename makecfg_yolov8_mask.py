def emptydir(dirname):  #清空資料夾
    if os.path.isdir(dirname):  #資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(2)  #需延遲,否則會出錯
    os.mkdir(dirname)  #建立資料夾

import glob
import os, shutil

from time import sleep
import random

batch = 24
subdivisions = 3
classname = ['none', 'bad', 'good']  #分類標籤
train = 'yolodata/custom/train.txt'  #訓練資料檔 
valid = 'yolodata/custom/valid.txt'  #驗證資料檔
test = 'yolodata/custom/test.txt'  #測試資料檔

validratio = 0.1  #驗證資料比例

print('開始建立設定資料！(第一次執行會較久，請耐心等候！)')
#下載預訓練檔

emptydir('yolodata/custom')  #建立設定資料夾


#建立obj.data
classes = len(classname)  #分類標籤數量
f = open('yolodata/custom.yaml', 'w')
out = 'nc : ' + str(classes) + '\n'
out += 'train : ' + train + '\n'
out += 'val : ' + valid + '\n'
out += 'test : ' + test + '\n'
out += 'names: [ '
# for cla in classname:
#     out += cla+","
for cla in classname:
    out += cla+","

out += ']\n'
f.write(out)


#建立訓練及驗證資料檔
imgfiles = glob.glob('yolodata/images/*.png')  #讀取圖形檔
for i in range(len(imgfiles)):
    imgfiles[i] = imgfiles[i].replace('\\', '/')
validnum = int(len(imgfiles) * validratio)  #驗證資料數量
validlist = random.sample(imgfiles, validnum)  #取出驗證資料
f = open(valid, 'w')
out =''
for val in validlist:
    out += val + '\n'
f.write(out)
f = open(train, 'w')
out =''
for tra in imgfiles:
    if tra not in validlist:  #不是驗證資料的圖形資料
        out += tra + '\n'
f.write(out)

f.close()
print('建立設定資料完成！')
    
