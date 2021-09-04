#!/usr/local/bin/python3

import asyncio
import time
from bleak import BleakScanner
from tkinter import *
from tkinter import ttk

mydevices = []
container = Tk()
container.title("Scanner")
frame = ttk.Frame(container, padding="4 4 4 4", name="myframe")           # Parent = container
frame.grid(column=0, row=0, sticky=(N, W, E,S));  # Place this on its parent's grid
container.columnconfigure(0, weight=1);                  # Configure column weight
container.rowconfigure(0, weight=1);                     # Configure row weight

listbox_widget = Listbox(frame, name="ble_dev_list")
listbox_widget.pack();

def getGATT():
    idxList = listbox_widget.curselection();
    if len(idxList):
        print("Selected ", idxList[0], "Of ", len(mydevices));
        device = mydevices[int(idxList[0])];
        print(device)

weiter = Button(frame, text="Query", command=getGATT);
weiter.pack();

async def mainloop_thread(container):
    try:
        while True:
            container.update()
            await asyncio.sleep(1);
    except TclError as e:
        pass;

async def kickoff(container):
    ml_task = asyncio.create_task(mainloop_thread(container));
    #listbox_widget = container.nametowidget("myframe.ble_dev_list");
    if listbox_widget is not None:
        print(listbox_widget);
        print("Called discover at :", time.time());
        devices = await BleakScanner.discover();
        print("Returned from discover at :", time.time());
        print(len(devices));
        for entry in devices:
            mydevices.append(entry.address);
            print(entry);
            listbox_widget.insert(END, entry.name);
    else:
        print("Nothing");
    
    await ml_task;


asyncio.run(kickoff(container));

