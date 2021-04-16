import os

files = os.listdir('./Annotations')

for file in files:
    filename = file.split('.png.xml')[0] +'.xml'
    os.rename(file, filename)
