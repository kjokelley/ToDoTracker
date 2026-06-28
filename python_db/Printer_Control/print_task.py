from escpos.printer import Usb
import sys
#from Python_DB import task_handler as th

def print_task_by_id(task_id):
    """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
    p = Usb(0x04b8, 0x0202, 0, profile="TM-T88V")
    #p.text("Hello World\n")
    #p.text("123\n\n\n\n\n")
    #p.text("end")
    #p.image("Tux.svg.png")
    #p.barcode('4006381333931', 'EAN13', 64, 2, '', '')

    #task = th.get_task(task_id)
    p.text("Hello\n")
    #if len(sys.argv) != 4:
    #    raise ValueError("4 arguments required, only " + str(len(sys.argv)) + " were passed")
    #def print_task(task_name, task_type, priority):
    #p.text(sys.argv[1] + "\n")
    #p.text(sys.argv[2] + "\n")
    #p.text(sys.argv[3] + "\n")
    #p.text(task[1] + "\n")
    #p.text(task[2] + "\n")
    #p.text(str(task[4]) + "\n")

print_task_by_id(1)
