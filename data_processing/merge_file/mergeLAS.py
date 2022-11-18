import sys
import traceback
import laspy
import os

'''

This file will merge all LAS file saved under "original" folder 
and write all data into the file under the "out" folder

In the code, 
we merged nine polygons of Stanley Park into one file named park.las

'''
try:
    print('Running Merge LAS')

    #This is the las file to append to.  
    out_las = 'out/park.las'
    #this is a directory of las files
    inDir = 'original'

    def append_to_las(in_laz, out_las):
        with laspy.open(out_las, mode='a') as outlas:
            with laspy.open(in_las) as inlas:
                for points in inlas.chunk_iterator(2_000_000):
                    outlas.append_points(points)


    for (dirpath, dirnames, filenames) in os.walk(inDir):
        for inFile in filenames:
            if inFile.endswith('.las'):
                in_las = os.path.join(dirpath, inFile)
                append_to_las(in_las, out_las)
        
        
    print('Finished without errors - mergeLAS.py')
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    print('Error in append las')
    print ("PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError     Info:\n" + str(sys.exc_info()[1]))  