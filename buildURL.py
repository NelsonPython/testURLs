import re

'''
../how-to-guides/create-plugin.md
../how-to-guides/create-account.md
../concepts/channels.md


/home/iotahub/documentation/iota-js/0.1/account-module/how-to-guides/create-and-manage-cda.md
https://docs.iota.org/docs/iota-js/0.1/account-module/how-to-guides/create-and-manage-cdreferences/cda-advice
https://docs.iota.org/docs/iota-js/0.1/account-module/how-to-guides/create-plugin
HTTPError:  HTTP Error 404: Not Found

Test:  follow the link in  /home/iotahub/documentation/iota-js/0.1/mam/introduction/overview.md  with name:  channel  and URL:  https://docs.iota.org/docs/iota-js/0.1/mam/introduction/overvieconcepts/channels
HTTPError:  HTTP Error 404: Not Found

/home/iotahub/documentation/iota-js/0.1/account-module/how-to-guides/listen-to-events.md
https://docs.iota.org/docs/iota-js/0.1/account-module/how-to-guides/create-account
https://docs.iota.org/docs/iota-js/0.1/account-module/how-to-guides/create-account
PASSED
'''
userFolder = "/home/iotahub/"
githubFolder = "documentation"
fileList = "docsMD.txt"
rootURL = "https://docs.iota.org/docs"

#link = '../how-to-guides/create-account.md'
link='../concepts/channels.md'

#markdown='/home/iotahub/documentation/iota-js/0.1/account-module/how-to-guides/listen-to-events.md'
markdown='/home/iotahub/documentation/iota-js/0.1/mam/introduction/overview.md'

# link begins with / as in /code/test.py
if link[0] == '/':
    leftOffset = len(userFolder)+len(githubFolder)+1
    markdown = markdown[leftOffset:]
    m = markdown.split('/')
    dir=''
    for k in range(len(m)-1):
        dir += m[k]+"/"
    tst = rootURL+"/"+dir+link[:-3]

# link begins with ../ in order to use the root path
if link[:3] == '../':
    link = link[3:-3]
    leftOffset=len(userFolder)+len(githubFolder)
    markdown = re.sub(".md","",markdown)
    markdown = markdown[leftOffset:]
    linkMatch = link.split("/")
    rightOffset = markdown.find(linkMatch[0])
    if rightOffset == -1:
        markdown = markdown[1:]
        m = markdown.split("/")
        dir=''
        for k in range(len(m)-2):
            dir += m[k]+"/"
        tst = rootURL+"/"+dir+link
    else:
        tst = rootURL+markdown[:rightOffset]+link
    print(tst)


