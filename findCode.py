import os
import re

fo = open("foundCode.txt","w")

# store filenames in a list and remove the end of filename character 
with open("docsFiles.txt") as f:
    filenames = f.read().split('\n')
for filename in filenames:
    if len(filename) > 0:
        filename = "/home/$USERNAME/"+filename
        print("\n", filename, file=fo)

        # open each file in the list and read the contents into a string called txt
        g = open(filename,"r")
        txt = g.read()

        # find every instance of the formatting character (or marker) that designates code
        marks  = [m.start() for m in re.finditer('```',txt)]

        # if there are an even number of markers then gather the code between the markers
        if len(marks)%2==0:
            it = iter(marks)
            for first in it:
                print(txt[first:next(it)],file=fo)
        else:
            print("/nUNEVEN NUMBER OF ``` MARKERS in ", filename)


                
