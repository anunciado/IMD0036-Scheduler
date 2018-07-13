# Scheduler

In this project, we implemented a scheduler simulator that allows the control of the behavior of processes, with the algorithms: FIFO (First in, first out), where as its own name already says, the first one that arrives will be the first one to be executed, non-preemptivo, that is, it executes the whole process from beginning to end not interrupting the executed process until finalized; RR (Round Robin), in this scheduling the operating system has a timer, called quantum, where all processes gain the same quantum value to run on the CPU, after the quantum ends and the process does not end, a preemption occurs and the process is inserted into the quantum. end of the queue. If the process finishes before a quantum, the CPU is released for the execution of new processes, and finally, Normal, where the scheduling will be given only by its priority. The files that contain the execution parameters of the processes are in tables separated by commas without the names of the columns. As shown below:

| ID 	| Priority 	| Quantum 	| Timeleft 	|
|---	|---	|---	|---	|
| 1 	| 2 	| 2 	| 4 	|
| 2 	| 3 	| 4 	| 5 	|
| 3 	| 4 	| 5 	| 6 	|

The ID determines its unique number among existing processes, priority determines its execution priority in relation to the other processes, the quantum determines the execution time given to it for preemptive type schedules, and timeleft determines the execution time remaining for the process is finished. After reading the process file and storing it in the process table, it will be executed according to the scheduling algorithm.

### Prerequisites

You will need to install the modules below to run the program: 
* [python 3.7 or greater](https://www.python.org/downloads/release/python-370/)

### Running

There are two ways to run the program:

* Compile the IDE (PyCharm - Python IDE):
1. Just open the IDE
2. Import the project folder as a Project
3. Select Run/Debug Configurations:
For scheduling:
```
<processesfile> <typeofscheduler>
```
An example would be:
```
./tests/input.txt normal
```
4. Choose Run scheduling on the context menu.
5. From this it only interacts with the system and add in script parameters box contents:

* Compile by terminal:
1. Enter the src folder and run the following command:
For scheduling:
```
python scheduling.py <processesfile> <typeofscheduler>
```
An example would be:
```
python scheduling.py ./tests/input.txt normal
```
2. From this it only interacts with the system.

## Built With

* [PyCharm](https://www.jetbrains.com/pycharm/) - A IDE used

## Authors
### Developers: 
* **Luís Eduardo Anunciado Silva ([cruxiu@ufrn.edu.br](mailto:cruxiu@ufrn.edu.br))** 
* **Larissa Gilliane Melo De Moura ([larissagilliane@ufrn.edu.br](mailto:larissagilliane@ufrn.edu.br))** 
### Project Advisor: 
* **Julio Cesar Paulino De Melo ([julio.melo@imd.ufrn.br](mailto:julio.melo@imd.ufrn.br))** 

See also the list of [contributors](https://github.com/cruxiu/IMD0036-Scheduler/contributors) who participated in this project.

## License

This project is licensed under the GPL 3.0 - see the [LICENSE](LICENSE) file for details
