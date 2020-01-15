# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 16:26:07 2019

@author: yakku
"""

class elvLog:
    
    def __init__(self, time, elevID, elevLoc):
        self.time = time
        self.elevID = elevID
        self.elevLoc = elevLoc
        

class Printer:
    
    lognum = 1;
    elvlogList = []
    __output__ = []
    
    
    def elvlog_update(self, time, elevID, elevLoc):
        self.elvlogList.append(elvLog(time, elevID, elevLoc))
    
    
    def elvlog_print(self):
        f = open("C:\YEONJIN\GIT\Github\Elevator-Project\elvLog"+str(self.lognum)+".txt", 'w')
        
        for i in range(0, len(self.elvlogList)):
            tmp_elvlog = self.elvlogList[i]
            data = str(tmp_elvlog.time)+", "+str(tmp_elvlog.elevID)+", "+str(tmp_elvlog.elevLoc)+"\n"
            print(data)
            f.write(data)
        f.close()


p = Printer()
p.elvlog_update(10, 1, 4)
p.elvlog_update(13, 1, 6)
p.elvlog_print()