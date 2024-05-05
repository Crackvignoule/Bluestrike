import time 
import os
import asyncio
import subprocess

from rich import print
from rich.prompt import Prompt
from rich.console import Console

from utils.logo import print_logo
from utils.kick import _kick_, deauth_Method_1, deauth_Method_2
from utils.scanner import main, scan_devices

modules = """[bright_white] [1] :mag: Scan for Bluetooth Devices
 [2] :satellite: Kick Out Bluetooth Devices
[red] [Q] :door: Exit (Ctrl + c)
"""

#TODO Build package with project.toml
#TODO remove useless dependencies like asyncio ?
#TODO remove dotenv and .en ; Symplifying usage by getting adress from user input during runtime
#TODO ask for package size and threads count with default values
#TODO GET MAC addr automatically for spoofing
#TODO change spoofing method (ifconfig deprecated)

def Main_Modules():
    print_logo()
    print(modules)
    
    asyncio.run(main())

    mac_address = Prompt.ask("[red] :signal_strength: Enter the Mac Adress ")
    start_time = Prompt.ask("[red] :question: In how many seconds do you want to start the attack ")
    _kick_(deauth_Method_1, mac_address, 600, 20, int(start_time))
        

if __name__ == "__main__":
    try:
        # Turns Bluetooth Adapter - ON
        os.system("rfkill unblock bluetooth")
        os.system("bluetoothctl power on")
        time.sleep(2)
        # ----------------------------------
        Main_Modules()
    except KeyboardInterrupt:
        Console.clear()
        print("[red] :door: User Quit")
        exit()
    except Exception as e:
        Console.clear()
        print(f"[red] :warning: ERROR VALUE [{e} ]")
        exit()
