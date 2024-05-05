import os
import asyncio

from rich import print
from rich.prompt import Prompt

from .utils.logo import print_logo
from .utils.kick import _kick_, deauth_Method_1, deauth_Method_2
from .utils.scanner import scan

# modules = """[bright_white] [1] :mag: Scan for Bluetooth Devices
#  [2] :satellite: Kick Out Bluetooth Devices
# [red] [Q] :door: Exit (Ctrl + c)
# """

#TODO interactive choices with curses (like nvtop)
#TODO GET MAC addr automatically for spoofing
#TODO change spoofing method (ifconfig deprecated)

def Main_Modules():
    print_logo()
    
    # Unblocking Bluetooth
    os.system("rfkill unblock bluetooth")
    
    # Start Bluetooth Scan
    mac_addr = asyncio.run(scan())
    print(f"[yellow]:satellite: Selected Device [{mac_addr}]")

    # TODO Ask for method 1 or 2

    # Ask for packet size and threads count
    packet_size = Prompt.ask("[red]:question: Enter the packet size (600)", default=600)
    threads_count = Prompt.ask("[red]:question: Enter the threads count (100)", default=100)

    # Start attack
    _kick_(deauth_Method_1, mac_addr, int(packet_size), int(threads_count))