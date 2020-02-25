# Elevator-Project
This project aims to simulate elevator movements and to find the best efficient control algorithm.
We start from barehand to develop a simulator and further to implement a better control algorithm that decreases the average waiting time.

- - -

We provide a class diagram as follows:

![class diagram](https://github.com/RangBin/Elevator-Project/blob/master/images/class_diagram_ver2.png)

As the diagram illustrates, there are 5 classes in this project.
- Elevator class has its own information such as ID and location. Also, it has a list of passengers who are inside.
- ElevatorManager class controls elevators to decide which one should go and pick up the passenger.
- TimeStamp class is the main class that imports passenger input test cases that include at which time and on which floor the passenger called the elevators.
- Passenger class includes personal passenger information such as ID and destination.
- Printer class is defined for printing log and output.

- - -

Also, we provide an event flow graph as follows:

![event flow graph](https://github.com/RangBin/Elevator-Project/blob/master/images/flow_graph_ver1.png) 

- - -

This project is still in progress. (2019. Dec. 9 ~)
