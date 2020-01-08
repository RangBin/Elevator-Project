# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:27:08 2019

@author: Robin
"""
from Elevator import Elevator
from Passenger import Passenger

class ElevatorManager:
    __elevatorList = []

    def __init__(self, elvNum):
        self.__elevatorList = [Elevator() for i in range(elvNum)]
        
    def addElevator(self):
        self.__elevatorList.append(Elevator())
        
    def getNumOfElevator(self):
        return len(self.__elevatorList)
    
    def elevatorScheduler(self, newPassList):
        if newPassList==[]:
            return
        # for now just add
        self.__elevatorList[0].updatePassenger(newPassList)
        self.__elevatorList[0].updateNextLocation(newPassList.start)
        self.__elevatorList[0].updateNextLocation(newPassList.dest)
        print('scheduler')
        
    def elevatorMover(self):
        #move elevator for a step
        for elevator in self.__elevatorList:
            elevator.updateLocation()
        print('mover')
    
    
### testing codes ###
manager = ElevatorManager(1)
manager.elevatorMover()

passTest = Passenger(1, 1, 3)
manager.elevatorScheduler(passTest)

for i in range(3):
    manager.elevatorMover()
    
