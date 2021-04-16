import os
import csv
import numpy as np


path = './annotation'
files = os.listdir(path)

def write_anno_xml(img,annos):
    anno_folder = './aaa'
    img_path = './JPEGImages'

    xml_file = open((anno_folder + '/' + img + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('        <folder>JPEGImages</folder>\n')
    xml_file.write('        <filename>' + img + '</filename>\n')
    xml_file.write('        <path>' + img_path + '/' + img + '</path>\n')
    xml_file.write('        <source>\n')  
    xml_file.write('                <database>Unknown</database>\n')
    xml_file.write('        </source>\n')     
    xml_file.write('        <size>\n')
    xml_file.write('                <width>' + '300' + '</width>\n')
    xml_file.write('                <height>' + '300' + '</height>\n')
    xml_file.write('                <depth>3</depth>\n')
    xml_file.write('        </size>\n')
    xml_file.write('        <segmented>0</segmented>\n')
    for anno in annos:
        xml_file.write('        <object>\n')
        xml_file.write('                <name>' + 'apple' + '</name>\n')
        xml_file.write('                <pose>Unspecified</pose>\n')
        xml_file.write('                <truncated>0</truncated>\n')
        xml_file.write('                <difficult>0</difficult>\n')
        xml_file.write('                <bndbox>\n')
        xml_file.write('                        <xmin>' + str(anno[0]) + '</xmin>\n')
        xml_file.write('                        <ymin>' + str(anno[1]) + '</ymin>\n')
        xml_file.write('                        <xmax>' + str(anno[2]) + '</xmax>\n')
        xml_file.write('                        <ymax>' + str(anno[3]) + '</ymax>\n')
        xml_file.write('                </bndbox>\n')
        xml_file.write('        </object>\n')
    xml_file.write('</annotation>')
    xml_file.close()

for file in files:
    f = open(path + "/" + file)
    reader = csv.DictReader(f)
    x = [row['c-x'] for row in reader]
    x = [float(num) for num in x]
    x = np.array(x)
    num = x.size

    f = open(path + "/" + file)
    reader = csv.DictReader(f)
    y = [row['c-y'] for row in reader]
    y = [float(num) for num in y]
    y = np.array(y)


    f = open(path + "/" + file)
    reader = csv.DictReader(f)
    r = [row['radius'] for row in reader]
    r = [float(num) for num in r]
    r = np.array(r)


    

    xmin = x - r/2
    xmin = xmin.tolist()
    xmin_arr = []
    for item in xmin:
        if item < 0:
            item = 0
        if item > 308:
            item = 308
        xmin_arr.append(item)
            
    xmax = x + r/2
    xmax = xmax.tolist()
    xmax_arr = []
    for item in xmax:
        if item < 0:
            item = 0
        if item > 308:
            item = 308    
        xmax_arr.append(item)        
            
    ymin = y - r/2
    ymin = ymin.tolist()
    ymin_arr = []
    for item in ymin:
        if item < 0:
            item = 0
        if item > 202:
            item = 202
        ymin_arr.append(item)
            
    ymax = y + r/2
    ymax = ymax.tolist()
    ymax_arr = []
    for item in ymax:
        if item < 0:
            item = 0
        if item > 202:
            item = 202
        ymax_arr.append(item)
        
        
    annotation = []
    annotations = []
    for i in range(num):
        annotation = [xmin_arr[i], ymin_arr[i], xmax_arr[i], ymax_arr[i]]
        annotations.append(annotation)
        
    img = file.split('.csv')[0]

    write_anno_xml(img, annotations)

        
#    for row in reader:
#        x = row[1]


        #print(annotation)

    #    write_anno_xml(img, annos)
#    line = f.readlines()
#    i = 1
#    for i in line[i]:



