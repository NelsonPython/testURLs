'''
Read the github repo folder and get a list of subfolders with markdown files
'''

import os

testFolder = 'test/docsFolders.txt'
testFile = 'test/docsFiles.txt'
testDir = '<REPO>/'

f = open(testFile,'w')
ff = open(testFolder, 'w')

for dirname, dirnames, filenames in os.walk(testDir):
        for subdirname in dirnames:
                if "git" not in dirname:
                        if "git" not in subdirname:
                                print(os.path.join(dirname, subdirname))
                                print(os.path.join(dirname, subdirname), file=ff)

        for filename in filenames:
                if 'md'in filename:
                        if "git" not in dirname:
                                dirfile = dirname+"/"+filename
                                print(dirfile, file=f)
                                print(dirfile)
                if 'how-to-' in dirname:
                        if 'md' in filename:
                                print(os.path.join(dirname,filename), file=ff)
                                #print(os.path.join(dirname,filename))

                if 'htm' in filename:
                        print(os.path.join(dirname,filename), file=ff)
                        #print(os.path.join(dirname,filename))

f.close()
ff.close()

