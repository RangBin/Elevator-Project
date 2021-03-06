# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:27:08 2019

@author: Robin
"""
from Elevator import Elevator
from Passenger import Passenger

class ElevatorManager:
    __elevatorList = []
    __waitingPassList = []

    def __init__(self, elvNum):
        self.__elevatorList = [Elevator() for i in range(elvNum)]
        
    def addElevator(self):
        self.__elevatorList.append(Elevator())
        
    def getNumOfElevator(self):
        return len(self.__elevatorList)
    
    def elevatorScheduler(self, newPassList):
        # whenever event happens, distribute waiting passenger to elev. and re-schedule
        # TODO: not implemented yet
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
            isReached = elevator.move()
            if isReached:
                elvLocation = elevator.getLocation()
                elvDir = elevator.getDirection()
                
                for waitingPass in self.__waitingPassList:
                    if waitingPass.start!=elvLocation:
                        continue
                    if waitingPass.start < waitingPass.dest:
                        passDir = 1
                    else:
                        passDir = -1
                    if passDir==elvDir:
                        # TODO: may handle max people elevator problem later..
                        elevator.addPassenger(waitingPass)  
        #print('mover')
    
