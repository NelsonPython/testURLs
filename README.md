# Test for broken links in markdown

1. Clone a repo with markdown files

2. By default, getDocsMap.py writes output files to the /test folder.  Create a /test folder

3. Open getDocsMap.py and change the repo name

```
testFolder = 'test/docsFolders.txt' # folders containing markdown files
testFile = 'test/docsFiles.txt'     # a list of markdown files
testDir = '<REPO>/'          # repo name
```

4. Run getDocsMap.py

5. Go to the /test folder

6. Run ```python3 findCode.py``` to find code snippets encoded with ```
Results are stored in foundCode.txt

7. Run ```python3 findLinkExistsV5.py``` to read each markdown file in the docsFiles.txt list.  Find each URL, follow each URL, and report status.  The default is reporting only broken links, but you can change ```printPass= True``` to report the status of every link.  Results are stored in linkTestResults.txt


# Natural Language Analysis
Run python3 NLPmarkdown.py

The results will give insight into words used in the markdown

```
NUMBER OF DOCUMENTS REVIEWED 217

TOTAL WORDS: 121,450

TOTAL DIFFERENT WORDS: 7072

 50  MOST COMMON WORDS:
iota 	 716
address 	 699
transaction 	 624
node 	 602
data 	 544
transactions 	 486
bash 	 449
command 	 413
following 	 393
file 	 388
hub 	 378
create 	 345
run 	 325
tangle 	 315
info 	 299
iri 	 283
hash 	 279
api 	 275
have 	 272
install 	 271
bundle 	 270
new 	 263
seed 	 259
network 	 259
tokens 	 258
server 	 243
addresses 	 237
nodes 	 236
account 	 234
const 	 221
value 	 217
request 	 216
number 	 215
json 	 215
should 	 213
field 	 211
balance 	 207
user 	 205
mam 	 199
error 	 196
send 	 193
set 	 192
connect 	 190
trytes 	 187
example 	 182
code 	 181
deposit 	 177
make 	 174
message 	 173
more 	 168

TOTAL COMPLEX WORDS: 525

COMPLEX WORDS: ['documentation', 'implementing', 'international', 'environment', 'requirements', 'specifications', 'measurement', 'accelerometer', 'magnetometer', 'orientation', 'temperature', 'instructions', 'installation', 'individually', 'prerequisites', 'interacting', 'automatically', 'preferences', 'configuration', 'localisation', 'information', 'getnodeinfo', 'asciitotrytes', 'initializes', 'initialization', 'placeholder', 'dontsharethis', 'calibration', 'scrollspeed', 'astropidata', 'updatelocation', 'trytestoascii', 'chronological', 'experiments', 'authenticated', 'subscription', 'acceleration', 'programming', 'tiltheading', 'implementation', 'coordinator', 'application', 'introduction', 'contribution', 'lightweight', 'computations', 'transactions', 'transaction', 'milliseconds', 'computation', 'dependencies', 'milestonestart', 'calculating', 'successfully', 'compromised', 'inconsistent', 'propagating', 'sequentially', 'getbalances', 'milestoneindex', 'architecture', 'presentation', 'distributed', 'description', 'neighbouring', 'probability', 'deterministic', 'unconfirmed', 'corrdinator', 'broadcasting', 'communication', 'calculations', 'compilation', 'development', 'architectures', 'recommended', 'outsourcing', 'directories', 'functionality', 'differences', 'limitations', 'applications', 'environments', 'confirmation', 'credentials', 'coinmarketcap', 'certificates', 'placeholders', 'autoswitching', 'certificate', 'rebroadcast', 'combination', 'bundletrytes', 'compressing', 'advertisements', 'coordinates', 'nphtqorl9xk', 'approximate', 'iotaareacodes', 'nphtqorl9xkf', 'authenticity', 'credibility', 'backgrounds', 'organization', 'administrator', 'participant', 'backgroundid', 'newpassphrase', 'testpassphrase', 'trainingtitle', 'administration', 'setblacklist', 'transporting', 'asynchronous', 'poextutorial', 'immutability', 'inspiration', 'withdrawing', 'expectedamount', 'communicating', 'conditional', 'unnecessary', 'withdrawals', 'createaccount', 'overwritten', 'generatecda', 'startattaching', 'stopattaching', 'descriptive', 'distributing', 'serializing', 'parsecdamagnet', 'pendingdeposit', 'selectinput', 'reattaching', 'contributing', 'annotations', 'diacritical', 'transferring', 'obsoletetag', 'currentindex', 'confirmations', 'semarketmam', 'initialized', 'contributors', 'incrementing', 'securitylevel', 'authentication', 'initialises', 'attachtotangle', 'initialised', 'stringified', 'channelroot', 'channelmode', 'fetchsingle', 'communications', 'verysecretkey', 'asyncronously', 'synchronously', 'announcements', 'syncronously', 'represented', 'transferred', 'reattachment', 'newtailhash', 'setinterval', 'confirmedtail', 'autoconfirm', 'understanding', 'relationship', 'experienced', 'seedprovider', 'apisettings', 'synchronized', 'eventmachine', 'eventlogger', 'balancecheck', 'timedecider', 'oraclesource', 'oraclesources', 'rejectioninfo', 'asmagnetlink', 'deserialize', 'contributions', 'integration', 'corresponding', 'testaddress', 'representation', 'conveniently', 'establishing', 'independent', 'communicate', 'supervision', 'communicates', 'supervisors', 'microservice', 'protections', 'authorization', 'cybersecurity', 'discovering', 'engineering', 'performance', 'unavailability', 'organizations', 'abbreviations', 'transmission', 'consistency', 'trustworthy', 'snapshotindex', 'permissionless', 'accumulates', 'partitioning', 'replication', 'microservices', 'collections', 'reliability', 'computational', 'calculation', 'explanation', 'surrounding', 'preparation', 'subsequently', 'transformed', 'optimizations', 'identifiers', 'consumption', 'considering', 'significantly', 'heuristically', 'optimization', 'walkvalidator', 'walkeralpha', 'randomnumber', 'highestrating', 'reconstruct', 'synchronize', 'synchronizing', 'connections', 'addneighbors', 'disconnected', 'subscriptions', 'solidifying', 'permanently', 'addedneighbors', 'intersection', 'maxgettrytes', 'maxbodylength', 'referencing', 'getneighbors', 'connectiontype', 'jrefreememory', 'jremaxmemory', 'jretotalmemory', 'dnsrefresher', 'temporarily', 'verification', 'availability', 'integrations', 'integrating', 'unavailable', 'validations', 'configuring', 'trustanchors', 'synchronizes', 'downloading', 'periodically', 'publishlocal', 'filteredstream', 'fundamental', 'nullpointer', 'keyedstream', 'partitioned', 'horizontally', 'aggregation', 'accumulator', 'simplification', 'timewindowall', 'slidingwindow', 'mostusedstream', 'mapwithcounts', 'constructor', 'approximately', 'controlling', 'consecutive', 'distributes', 'nodesharing', 'malfunction', 'interceptor', 'interception', 'responsible', 'visualization', 'autopeering', 'statusscreen', 'tipselection', 'containerid', 'neighborhood', 'corresponds', 'decentralized', 'developments', 'interconnected', 'accountstore', 'memorystore', 'iotaaccount', 'eventlistener', 'eventmanager', 'accountplugin', 'continuously', 'accountevent', 'cryptography', 'allprojects', 'repositories', 'synchronous', 'cryptocurrency', 'incompatible', 'fingerprint', 'customizable', 'certification', 'distributions', 'a440cce5664a', 'localization', 'withnamespaces', 'translations', 'appropriate', 'mycontainer', 'translating', 'configurations', 'vulnerability', 'discussions', 'getaddressinfo', 'getuserhistory', 'sweepdetail', 'userwithdraw', 'cancelation', 'balanceevent', 'payoutaddress', 'statsrequest', 'totalbalance', 'withdrawaluuid', 'useraddress', 'wascancelled', 'unsuccessful', 'insufficient', 'inefficient', 'efficiently', 'recoverfunds', 'reattachments', 'requestbyuuid', 'universally', 'stackoverflow', 'argon2tcost', 'listenaddress', 'authprovider', 'authenticate', 'hmackeypath', 'constraints', 'myrootpassword', 'hubpassword', 'usehttpsiri', 'a7fe9d77bfb', 'supervisorctl', 'signingmode', 'frameborder', 'distribution', 'fakexchange', 'statreloader', 'interactive', 'basecommand', 'commanderror', 'makemigrations', 'specialized', 'interfacing', 'outputaddress', 'inputaddress', 'keyseclevel', 'trytestotrits', 'getstatsreply', 'streamreply', 'createmetadata', 'printmetadata', 'sweepinterval', 'regenerating', 'introducing', 'programmers', 'conventions', 'compression', 'transparent', 'fragmentation', 'microkernel', 'permissions', 'distinguish', 'specifically', 'sensorconfig', 'interfacename', 'microprocessor', 'inexpensive', 'abstraction', 'sometimetimes', 'microcontoller', 'transportation', 'manufacturing', 'infrastructure', 'identification', 'automobiles', 'intervention', 'demonstrates', 'technologies', 'electricity', 'uncertainty', 'advantageous', 'registrations', 'traditional', 'registration', 'communicated', 'consolidate', 'maintaining', 'provisioning', 'alternative', 'contributed', 'deregistration', 'deregistered', 'additionally', 'producerprice', 'registering', 'unregistering', 'respectively', 'immediately', 'outstanding', 'conjunction', 'established', 'illustration', 'demonstration', 'scalability', 'intermediate', 'restriction', 'interaction', 'persistence', 'essentially', 'implemented', 'distributor', 'distributors', 'manufacturer', 'manufacturers', 'misplacement', 'stakeholders', 'stakeholder', 'incentivized', 'accountable', 'proprietary', 'centralized', 'interactions', 'participate', 'alternatively', 'reconciling', 'assetuniqueid', 'assetownerid', 'aggregating', 'cryptographic', 'channelsidekey', 'guaranteeing', 'newitemdata', 'assetuserid', 'messagebody', 'marketplace', 'micropayments', 'ingredients', 'contextualized', 'proliferation', 'fulfillment', 'overwhelming', 'compensating', 'diametrically', 'technological', 'perspective', 'prohibitively', 'intermediary', 'susceptible', 'organisation', 'organisations', 'marketplaces', 'competitive', 'participants', 'deployments', 'investigations', 'semiconductor', 'underscores', 'environmental', 'maintenance', 'precipitation', 'preconfigured', 'cornerstone', 'requirement', 'timestamped', 'interplanetary', 'retrievefile', 'addresponse', 'nextaddress', 'tanglepayload', 'unauthorized', 'grandparents', 'solidification', 'counterfeit', 'definitions', 'alphabetical', 'construction', 'disadvantage', 'disadvantages', 'particularly', 'restrictions', 'authenticates', 'cityxchange', 'cooperating', 'unprotected', 'walkthrough', 'invalidating', 'gangle9beat', 'tangle9beat', 'instruction', 'attachmenttag', 'authenticating', 'incremented', 'satisfactory', 'nameservers', 'unfortunately', 'prerequisite', 'necessarily']
```
