import sys
import pathlib
from Python_DB import task_handler as th
from Printer_Control import print_task as pt
from Python_DB import task_picker_logic as tpl
from Image_Handler import image_creator as ic
#th.create_task()



allTasks = th.get_all_tasks()
activeTasks = tpl.pickTasks(allTasks)
tasksToPrint = []


for x in activeTasks:
    task = th.get_task(x)
    tasksToPrint.append(task[1])
    th.set_active_task(x)
#    print(x)
#    pt.print_task_by_id(task[1])
image = ic.create_task_list_img(tasksToPrint)
pt.print_task_by_id(image)
#pt.print_task_by_id(1)





#task = task_json[0][1]
#print(task)
#pt.print_task_by_id(task)
#pt.print_task_by_id("1")
#th.move_task("1")
#th.create_task()
#th.remove_task("2")
#th.move_task_to_completed("3")
#th.move_task_to_todo("3")
