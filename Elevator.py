# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:48:20 2019

@author: Robin
"""
MAX_PASSENGER = 10

from Passenger import Passenger

class Elevator():
    global MAX_PASSENGER
    
    # class variable
    elevator_counter = 1    
    def __init__(self):
        self.__elevatorID = Elevator.elevator_counter
        Elevator.elevator_counter +=1 
        self.__location = 1
        self.__currPassList = []
        self.__maxPassenger = MAX_PASSENGER
        self.__nextLocation = []
        self.__direction = 0
       
    def __updateLocation(self):
        # update location of the elevator        
        self.__location += self.__direction        
        self.updatePassenger([])
        
    def __updateDirection(self):
        # update direction of the elevator
        if not self.__nextLocation:
            self.__direction = 0
        else:
            nxtLoc = self.__nextLocation[0]
            curLoc = self.__location
            if nxtLoc==curLoc:
                self.__direction=0
            else:
                self.__direction=1 if nxtLoc>curLoc else -1    
        
    def updatePassenger(self, newPass):
        # update passenger list (get in, get out ...)
        if newPass!=[]:
            self.__currPassList.append(newPass)
            
        #check if someone has to get out
        for passenger in self.__currPassList:
            if passenger.dest == self.__location:
                print('get out '+str(passenger.ID))
                self.__currPassList.remove(passenger)
                # printer.log
        
    def updateNextLocation(self, newNextJob):
        # update next location list of the elevator
        if newNextJob!=[]:
            self.__nextLocation.append(newNextJob)
        
    def updateLocation(self):
        # move for a step
        self.__updateDirection()
        self.__updateLocation()
        print('ID('+str(self.__elevatorID)+') at '+str(self.__location))

    ### some getters and setters.
    def getID(self):
        return self.__elevatorID
    
    def getLocation(self):
        return self.__location
    
    def getCurrPassList(self):
        return self.__currPassList
    
    def getMaxPassenger(self):
        return self.__maxPassenger
    
    def getNextLocation(self):
        return self.__nextLocation
    
    def getDirection(self):
        return self.__direction
    
    def setLocation(self, loc):
        self.__location = loc
        
    def setMaxPassenger(self, maxNum):
        self.__maxPassenger = maxNum
        
    def setNextLocation(self, nextLoc):
        self.__nextLocation = nextLoc
    
    def setDirection(self, direction):
        self.__direction = direction

