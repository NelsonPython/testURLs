'''
find and follow all links in a markdown file to find broken links
'''

import os
import re

# SETUP TEST
userFolder = "/home/$USERNAME/"
githubFolder = ">REPO NAME<"
fileList = "docsFiles.txt"
rootURL = "https://www.somewebsite.com/docs"
imageURL = "https://www.somewebsite.com/assets/docs"
printPass = False    # True: prints test results when the link is found (HTTP codes 200 or 403)
results = "linkTestResults.txt"

fo = open(results, "w")

# get markdownFiles, remove the end of file character, and store them in a list
checkURLs=[]
with open(fileList) as f:
    markdownFiles = f.read().split('\n')
for markdownFile in markdownFiles:
    if len(markdownFile) > 0:
        # markdownFile includes the githubfolder by default
        markdownFile = userFolder+markdownFile
        # open each file and read the contents into a string called txt
        g = open(markdownFile,"r")
        txt = g.read()
        # parse the markdown file to find URLs:  [link name][(link URL)
        try:
            matches = [(a.start(),a.end()) for a in list(re.finditer('\[[a-zA-Z0-9.\/\-\_ ]+\]\([a-zA-Z0-9.\/\-\_ ]+\)', txt))]
            for match in matches:
                if len(match) > 0:
                    checkURL = [markdownFile, txt[match[0]:match[1]]]
                    checkURLs.append(checkURL)
        except:
            continue


def formatTest(leftOffset,markdown, link, newPathnum, httpAddr):
    '''
    sample links:        ../RasSenseHat.png, ../images/core.png, #iota-terms, /introduction/overview.md
    sample checkURL[0]:  /home/iotahub/documentation/node-software/0.1/chronicle/references/data-model.md
    '''

    if ".md" in markdown:  markdown = re.sub(".md","",markdown)
    markdown = markdown[leftOffset:]               # remove /home/iotahub/documentation/

    linkMatch = link.split("/")
    rightOffset = markdown.find(linkMatch[0])       # find matching subfolders, if any

    if rightOffset == -1:                           # if no matching subfolders, create the new path from all the subfolders
        markdown = markdown[1:]
        m = markdown.split("/")
        newPath=''
        for k in range(len(m)-newPathnum):
            newPath += m[k]+"/"
        return(httpAddr+"/"+newPath+link)
    else:
        return(httpAddr+markdown[:rightOffset]+link)

tst = ''
testURLs=[]
for checkURL in checkURLs:
    # get the link name and the link URL
    nu = checkURL[1].split('(')
    linkName = nu[0][1:-1]
    link = nu[1][:-1]

    # TODO - review the need for this code to remove trailing text after the link caused by more than 1 close paranthesis symbols ")" in the markdown text
    if ")" in link:
        i = link.split(")")
        link = i[0]

    if len(link) > 0:

        if 'png' in link or 'PNG' in link:
            if "../" in link: link = link[3:]
            tst = formatTest(len(userFolder)+len(githubFolder), checkURL[0], link, 2, imageURL)
        elif 'jpg' in link or 'JPG' in link:
            if "../" in link: link = link[3:]
            tst = formatTest(len(userFolder)+len(githubFolder), checkURL[0], link, 2, imageURL)
        elif 'gif' in link or 'GIF' in link:
            if "../" in link: link = link[3:]
            tst = formatTest(len(userFolder)+len(githubFolder), checkURL[0], link, 2, imageURL)
           
        elif link[:4] == "http":
            tst = link
        
        elif link[:4] == 'root':
            link = re.sub(".md","",link)
            tst = re.sub('root:/',rootURL, link)

        elif link[0] == '/':                    # link begins with / as in /code/test.py
            link = re.sub(".md","",link[1:])
            tst = formatTest(len(userFolder)+len(githubFolder), checkURL[0], link, 1, rootURL)

        elif link[:3] == '../':                 # link begins with ../ in order to use the root path
            link = re.sub(".md","",link[3:])
            tst = formatTest(len(userFolder)+len(githubFolder), checkURL[0], link, 2, rootURL)

        elif link[0] == '#':                    # link begins with # pointing to a location inside a webpage 
            checkURL[0] = re.sub(".md","",checkURL[0])
            tst = rootURL+checkURL[0][len(userFolder)+len(githubFolder):]+link

        elif link[-3:] == ".md":                # other links indicated by ".md" at the end
            link = re.sub(".md","",link)
            tst = formatTest(len(userFolder)+len(githubFolder), checkURL[0], link, 1, rootURL)

    testURL = [checkURL[0],tst,linkName]
    testURLs.append(testURL)
    tst = ''
    linkName = ''


# RUN TEST
# testURL[0] contains the markdown
# testURL[1] contains the link name: [link name](link.md)
# testURL[2] contains the link being tested

import urllib.request
import io

def printResult(testURL,res,fo):
    print("\nRead this markdown file: ", testURL[0], "\n follow this link name: ", testURL[2], "\n to find this webpage: ", testURL[1],file=fo)
    print(res,file=fo)

passK=0
HTTPErrorK=0
URLErrorK=0
OtherK=0
for testURL in testURLs:
    if len(testURL[1]) > 0:
        try:
            u = urllib.request.urlopen(testURL[1], data=None)
            fu = io.TextIOWrapper(u, encoding='utf-8')
            try:
                text = fu.read()
            except:
                if printPass is True:  printResult(testURL,"ERROR reading data from webpage (often an encoding error of png or jpg files)",fo)
                passK+=1
                continue
            if len(text) > 0:
                if printPass is True:  printResult(testURL,'PASSED',fo)
                passK+=1

        except urllib.error.HTTPError as e:
            if "403" in str(e):
                if printPass is True: printResult(testURL,e,fo)
                passK+=1
            elif "404" in str(e):
                printResult(testURL,e,fo)
                HTTPErrorK+=1
            else:
                printResult(testURL,e,fo)
                OtherK+=1

        except urllib.error.URLError as e:
            printResult(testURL,e,fo)
            URLErrorK+=1
    
print("Number of links tested: ", len(testURLs), file=fo)
print("Number of links found: ", passK, file=fo)
print("Number of HTTP 404 Not Found: ", HTTPErrorK, file=fo)
print("Number of URL errors: ", URLErrorK, file=fo)
print("Number of other errors: ", OtherK, file=fo)
