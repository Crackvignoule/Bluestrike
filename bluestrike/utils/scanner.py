import asyncio
from bleak import BleakScanner
import re

from rich import print
from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table

# bl_scan = subprocess.check_output("bluetoothctl devices", shell=True, stderr=subprocess.STDOUT, text=True)
#     # from the output of blutetoothctl scan, build dictionary of devices
#     devices = {}
#     for line in bl_scan.split("\n"):
#         if "Device" in line:
#             mac = line.split()[1]
#             name = " ".join(line.split()[2:])
#             devices[mac] = name
#     print("[yellow] :satellite: Devices Found")
#     for mac, name in devices.items():
#         print(f"[yellow] {mac} - {name}")
#     user_choice = Prompt.ask("[cyan] :question: Enter your choice ")

async def scan_devices():
    print("[yellow]:satellite: Starting Bluetooth Scan")
    scanner = BleakScanner()
    await scanner.start()
    await asyncio.sleep(5)  # Scan for 5 seconds
    await scanner.stop()
    devices = scanner.discovered_devices
    return devices

def display_devices(devices):
    console = Console()
    table = Table(title="Bluetooth Devices")
    table.add_column("No.", justify="center", style="cyan")
    table.add_column("Device Name", style="magenta")
    table.add_column("MAC Address", style="green")

    for i, device in enumerate(devices, start=1):
        device_name = device.name
        mac_address = device.address
        table.add_row(str(i), device_name, mac_address)

    console.print(table)

def select_option(devices):
    selection = Prompt.ask("[red]:signal_strength: Select an option (enter the No. or a MAC address)")
    try:
        index = int(selection) - 1
        if index >= 0 and index < len(devices):
            return devices[index].address
        else:
            raise ValueError()
    except ValueError:
        # Check if the input is a valid MAC address.
        if re.match("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$", selection):
            return selection
        else:
            print("Invalid option. Please try again.")
            return select_option(devices)

async def main():
    while True:
        # Starting Bluetooth Scan
        devices = await scan_devices()
        display_devices(devices)

        # Ask if the user wants to scan again
        scan_again = Prompt.ask("[bold cyan]:repeat: Scan again \[y/N]? [/bold cyan]")
        if scan_again.lower() == "y":
            continue

        selected_device = select_option(devices)
        mac_address = selected_device
        return mac_address

if __name__ == "__main__":
    asyncio.run(main())

