# Test for broken links in markdown

1. Clone a repo with markdown files

2. By default getDocsMap.py writes output files to the /test folder so create a /test folder.

3. Open getDocsMap.py and change the repo name

```
testFolder = 'test/docsFolders.txt' # folders containing markdown files
testFile = 'test/docsFiles.txt'     # a list of markdown files
testDir = 'documentation/'          # repo name
```

4. Run getDocsMap.py

5. Go to the /test folder

6. Run ```python3 findCode.py``` to find code snippets encoded with ```
Results are stored in foundCode.txt

7. Run ```python3 findLinkExistsV5.py``` to read each markdown file in the docsFiles.txt list.  Find each URL, follow each URL, and report status.  The default is reporting only broken links, but you can change ```printPass= True``` to report the status of every link.  Results are stored in linkTestResults.txt
