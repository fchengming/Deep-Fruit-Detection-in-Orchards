import os
import csv
import re

path = './annotation'
ann_path = './Annotations'
img_path = './JPEGImages'
test_path = './ImageSets/Main/test.txt'
train_path = './ImageSets/Main/train.txt'
trainval_path = './ImageSets/Main/trainval.txt'
val_path = './ImageSets/Main/val.txt'
ttest_path = './ImageSets/Mainn/test.txt'
ttrain_path = './ImageSets/Mainn/train.txt'
ttrainval_path = './ImageSets/Mainn/trainval.txt'
vval_path = './ImageSets/Mainn/val.txt'

files = os.listdir(path)
name = []
lines = []


for file in files:
    f = open(path + "/" + file)
    reader = csv.DictReader(f)
    x = [row['c-x'] for row in reader]
    if len(x) < 1:
        name.append(file.split('.csv')[0])
    
f.close()
    
      

for item in name:
    # os.remove(ann_path + "/" + item + '.xml')
    os.remove(img_path + "/" + item + '.png')  
    os.remove(path + "/" + item + '.csv')     
 
 
## val   
f = open(val_path, 'r')
lines = f.read().splitlines() 
       
for item in name:


    for l in lines:
        if l == item:
            lines.remove(item)
f.close()

f = open(vval_path, 'w+')
for line in lines:
    f.writelines(line + '\n')
f.close()
            

##train
f = open(train_path, 'r')
lines = f.read().splitlines() 
       
for item in name:


    for l in lines:
        if l == item:
            lines.remove(item)
f.close()

f = open(ttrain_path, 'w+')
for line in lines:
    f.writelines(line + '\n')
f.close()


##trainval
f = open(trainval_path, 'r')
lines = f.read().splitlines() 
       
for item in name:


    for l in lines:
        if l == item:
            lines.remove(item)
f.close()

f = open(ttrainval_path, 'w+')
for line in lines:
    f.writelines(line + '\n')
f.close()

##test
f = open(test_path, 'r')
lines = f.read().splitlines() 
       
for item in name:


    for l in lines:
        if l == item:
            lines.remove(item)
f.close()

f = open(ttest_path, 'w+')
for line in lines:
    f.writelines(line + '\n')
f.close()

        

    


    
