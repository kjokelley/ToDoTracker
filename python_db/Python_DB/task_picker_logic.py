import random
"""tasks = [(1, "task1",1), (2, "task1",1), (3, "task1",1), (4, "task1",1), (5, "task1",1), 
         (6, "task2",2), (7, "task1",2), (8, "task1",2), (9, "task1",2), (10, "task1",3), 
          (11, "task1",3), (12, "task1",3), (13, "task1",3), (14, "task1", 2), (15, "task1",2), 
           (16, "task1",1), (17, "task1",1), (18, "task1",1), (19, "task1",1), (20, "task1",1) ]"""

#Task day = 6 Total Points
#Task day (5,1) = 6, Task day (4,2) or (4, 1, 1) = 6, Task day (3, 1, 1, 1) = 6

def pickTasks(tasks):
    taskDayTotal = 0
    activeTasks = []
    taskDict = {1:[], 2:[], 3:[], 4:[], 5:[]}
    runningTotalOfPriority = {1:0, 2:0, 3:0, 4:0, 5:0}
    for x in tasks:
        if(x[8] == True):
            if(x[7] == False):
                activeTasks.append(x[0])
                taskDayTotal += x[3]
            else:
                activeTasks.append(x[0])

        #taskDict[x[0]] = x[2]
        if(x[7] == False):
            match x[3]:
                case 1:
                    runningTotalOfPriority[1] += 1
                    taskDict[1].append(x[0])
                case 2:
                    runningTotalOfPriority[2] += 1
                    taskDict[2].append(x[0])
                case 3:
                    runningTotalOfPriority[3] += 1
                    taskDict[3].append(x[0])
                case 4:
                    runningTotalOfPriority[4] += 1
                    taskDict[4].append(x[0])
                case 5:
                    runningTotalOfPriority[5] += 1
                    taskDict[5].append(x[0])
                case _:
                    print("err: Task Priority not in list...")


    print(taskDict)
    print(runningTotalOfPriority)

    
    
    while taskDayTotal < 6:
        if(runningTotalOfPriority[5] >= 1 and (taskDayTotal + 5) <= 6):
            activeTasks.append(taskDict[5][random.randint(0, len(taskDict[5]) - 1)])
            taskDayTotal += 5
        if(runningTotalOfPriority[4] >= 1 and (taskDayTotal + 4) <= 6):
            if(random.randint(1,3) == 1):
                activeTasks.append(taskDict[4][random.randint(0, len(taskDict[4]) - 1)])
                taskDayTotal += 4
        if(runningTotalOfPriority[3] >= 1 and (taskDayTotal + 3) <= 6):
            if(random.randint(1,7) == 1):
                activeTasks.append(taskDict[3][random.randint(0, len(taskDict[3]) - 1)])
                taskDayTotal += 3
        if(runningTotalOfPriority[2] >= 1 and (taskDayTotal + 2) <= 6):
            if(random.randint(1,10) == 1):
                activeTasks.append(taskDict[2][random.randint(0, len(taskDict[2]) - 1)])
                taskDayTotal += 2
        if(runningTotalOfPriority[1] >= 1 and (taskDayTotal + 1) <= 6 or taskDayTotal == 5):
            if(random.randint(1,14) == 1):
                activeTasks.append(taskDict[1][random.randint(0, len(taskDict[1]) - 1)])
                taskDayTotal += 1
    return activeTasks