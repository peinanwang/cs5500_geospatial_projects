"""
Put names of zip files in a certain folder into a new text file,
then extract files end with .las from these zip files by traversing
names of zip files from the created text file.
"""

import os
from zipfile import ZipFile

text_file = open("zip_name_list.txt", "w")
for path, subdirs, files in os.walk(r'/Users/glenn_hyh/Desktop/CS5500 Found of ' +
    'Software Engineering/cs5500_geospatial_projects/library/LiDAR_zips'):
    for filename in files:
        if filename.endswith(".zip"):
            filename_line = os.path.join(path, filename)
            text_file.write(str(filename_line) + os.linesep)

text_file = open("zip_name_list.txt", "r")
lines = text_file.readlines()
for line in lines:
    file = line.strip()
    print(file + "\n")
    with ZipFile(file, 'r') as zipObj:
        filename_list = zipObj.namelist()
        for filename in filename_list:
            if filename.endswith(".las"):
                zipObj.extract(filename, 'LiDar_las')