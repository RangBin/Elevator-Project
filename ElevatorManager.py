# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 17:27:08 2019

@author: Robin
"""
import Elevator

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