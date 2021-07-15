import os
import beem
from beem import Hive
from beem.blockchain import Blockchain
from beem.amount import Amount
import winsound

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR


author_whitelist = []
f = open('author_whitelist', 'r')
for line in f:    
    author_whitelist.append(line.replace('\n', ''))
f.close

blacklist = []
f = open('blacklist', 'r')
for line in f:    
    blacklist.append(line.replace('\n', ''))
f.close



print("==============================++--***--++==============================")
print("                       Altonos comment finder   ")
print("")
print("                       https://peakd.com/@altonos")
print("=======================================================================")





blockchain = Blockchain()
for op in blockchain.stream(only_ops = "comment"):
    if op['type'] == 'comment':
        for x in blacklist:       
            if x in op['body']:
                if op['author'] not in author_whitelist:
                    if op['parent_author'] != "":
                        print("==============================++--***--++==============================")
                        print(bcolors.WARNING ,"Found one suspicious comment per tag",bcolors.FAIL,x,bcolors.RESET)
                        print("Author:"+op['author'])
                        print("=======================================================================")
                        print(bcolors.OK,"https://peakd.com/@"+op['author']+"/"+op['permlink'], bcolors.RESET)
                        print("=======================================================================")
                        #print(op)
                        winsound.PlaySound("ping.wav", winsound.SND_ASYNC)
                        break
                else:
                    #print(op['author'])
                    pass

                
