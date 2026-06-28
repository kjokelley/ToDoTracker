import sys
import pathlib
from Python_DB import task_handler as th
from Printer_Control import print_task as pt
from Python_DB import task_picker_logic as tpl

#th.create_task()



#allTasks = th.get_all_tasks()
#activeTasks = tpl.pickTasks(allTasks)
#print(activeTasks)
#for x in activeTasks:
#    task = th.get_task(x)
#    print(x)
#    pt.print_task_by_id(task[1])
pt.print_task_by_id(1)





#task = task_json[0][1]
#print(task)
#pt.print_task_by_id(task)
#pt.print_task_by_id("1")
#th.move_task("1")
#th.create_task()
#th.remove_task("2")
#th.move_task_to_completed("3")
#th.move_task_to_todo("3")
