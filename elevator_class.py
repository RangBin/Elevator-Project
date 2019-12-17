# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:48:20 2019

@author: Robin
"""
MAX_PASSENGER = 10


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
       
    def __updateLocation(self):
        # update location of the elevator        
        self.__location += self.__direction        
        # may add check if the elevator arrived the target floor
        
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
        
        
    def updatePassenger():
        # update passenger list (get in, get out ...)
        # empty method for now
        print('update passenger')
        
    def updateNextLocation():
        # update next location list of the elevator
        # empty method for now
        print('update next location')
        # call __updateLocation, __updateDirection
    
class ElevatorManager:
    __elevatorList = []

    def __init__(self, elvNum):
        self.__elevatorList = [Elevator() for i in range(elvNum)]
        
    def addElevator(self):
        self.__elevatorList.append(Elevator())
        
    def getNumOfElevator(self):
        return len(self.__elevatorList)
    
    def elevatorScheduler():
        # emtpy method for now
        print('scheduler')
        
    def elevatorMover():
        # emtpy method for now
        print('mover')
    

manager = ElevatorManager(3)
print(manager.getNumOfElevator())
manager.addElevator()
print(manager.getNumOfElevator())

