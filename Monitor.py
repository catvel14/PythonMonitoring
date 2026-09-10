import psutil
import time
from datetime import datetime
while True:
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:\\")


    print("==========================")

    if cpu > 1:
        print("Writing processes to log")
        show_top_processes();

    time.sleep(5)




    def show_top_processes():
        processes = []
        for process in psutil.process_iter(["pid", "name", "cpu_percent"]):
            try:
                if process.info["name"] == "System Idle Process":
                    continue
                processes.append({
                    "name": process.info["name"],
                    "pid": process.info["pid"],
                    "cpu": process.info["cpu_percent"]
                })
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        processes.sort(key=lambda process: process["cpu"], reverse=True)

        print("\nTop Processes:")
        

        timestamp = datetime.now()
        with open("log.txt", "a") as file:
                file.write(" Starting Log  \n")
                file.write(f"{timestamp}\n") 
                file.write('==========================\n') 
        for process in processes[:5]:
            print(f'{process["name"]:<25} {process["cpu"]}% CPU')
            with open("log.txt", "a") as file:
                file.write(f' {process["name"]:<25} {process["cpu"]}% CPU\n' )
      
