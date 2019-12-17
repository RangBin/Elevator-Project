# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:08:39 2019

@author: yakku
"""

class TimeStamp:
    
    duetime: int = 10000
    passList = []
    EM : ElevatorManager
    
    def __init__(self, time=10000): #time: int=10000
        #super().__init__()
        self.duetime = time
        self.EM = ElevatorManager()
        #inputStream init
        # -> passList init
        
        
    #def inputStreamInit(self):
    #여기서 passengerList init도 수행
        
    
    def main(self):
        eventList = []
        for i in range(0, self.duetime):
            #inputStream check -> get eventList
            #for i in range(0, len(eventList)):
                #eventList.pop()
                #EM.elevatorScheduler()
            #EM.elevaotrMover()
            
    

