# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:08:39 2019

@author: yakku
"""
import csv
import numpy as np
#import ElevatorManager


class TimeStamp:
    
    duetime: int = 20
    passList = []
    cache = []
    #EM : ElevatorManager
    
    
    def __init__(self, time=20): #time: int=10000
        #super().__init__()
        self.duetime = time
        #self.EM = ElevatorManager()
        self.f = open('test_case1.csv','r',encoding = 'utf-8')
        self.rdr = csv.reader(self.f)
        #inputStream init
        # -> passList init
        
        
    #def inputStreamInit(self):
        
        
    #여기서 passengerList init도 수행
    
    def __getEventList__(self, time):
        eventList = []
        print('time = '+str(time)+'sec')
        if(len(self.cache) != 0):
            if(self.cache[0]==time):
                eventList = [[int(x) for x in self.cache]]
            else:
                return eventList
                
        for line in self.rdr:
            if int(line[0]) != time:
                self.cache = [int(x) for x in line]
                #print('cache = '+str(self.cache))
                return eventList
            else:
                np.append(eventList,[[int(x) for x in line]], axis=0)
                
        
        return eventList
    
    def main(self):
        eventList = []
        
        for i in range(0, self.duetime):
            eventList = self.__getEventList__(i)
            if len(eventList) == 0:
                continue
            else:
                print('eventList =')
                for i in range(0, len(eventList)):
                    print(eventList[i])
            
            
            #inputStream check -> get eventList
            #for i in range(0, len(eventList)):
                #eventList.pop()
                #EM.elevatorScheduler()
            #EM.elevaotrMover()
            


#pseudo
#    def reroute(self, elvnum, dest):
        #nroute = Elevator[elvnum].route
        #if (방향 == up):
        #   if(Elevator[elvnum].cur_loc < dest):
        #       reroute할 때 passenger의 방향 고려 추가
        #       for i in range(0,nroute.index(max(nroute))):
        #           if(nroute[i]>dest):
        #               nroute.insert(i,dest)
        #               break
        #   elif(Elevator[elvnum].cur_loc > dest):
        #       for i in range(nroute.index(max(nroute))+1,len(nroute)):
        #           if(dest>nroute[i]):
        #               nroute.insert(i,dest)
        #elif (방향 == down):
        #   if(Elevator[elvnum].cur_loc > dest):
        #       reroute할 때 passenger의 방향 고려 추가
        #       for i in range(0,len(nroute)):
        #           if(nroute[i]<dest):
        #               nroute.insert(i,dest)
        #               break
        #   elif(Elevator[elvnum].cur_loc < dest):
        #       for i in range(nroute.index(min(nroute))+1,len(nroute)):
        #           if(dest<nroute[i]):
        #               nroute.insert(i,dest)
        #Elevator[elvnum].route = nroute
        #return

