import tkinter as tk
from tkinter import ttk
from .model import BLEHandle

class FirstView(ttk.Frame):
    def populateDevList(self):
        devnames = self.bleHandle.getDeviceNames();
        print("Populating ", len(devnames), " Devices");
        self.devicesBox.delete(0, 'end');
        for entry in devnames:
            self.devicesBox.insert(tk.END, entry);

    def queryDevice(self):
        idxList = self.devicesBox.curselection();
        if len(idxList):
            print("Selected ", idxList[0]);
            self.bleHandle.getServices(idxList[0]); 
            #self.bleHandle.doPrint(idxList[0]);
            #device = self.devices[idxList[0]];
            #print(device);

    def scanDevices(self):
        self.populateDevList();
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs);
        self.bleHandle = BLEHandle();
        scanButton = ttk.Button(self, text="Scan", command=self.scanDevices);
        scanButton.pack();
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S));
        parent.columnconfigure(0, weight=1);
        parent.rowconfigure(0, weight=1);
        self.devicesBox = tk.Listbox(self);
        self.devicesBox.pack();
        queryButton = ttk.Button(self, text="Query", command=self.queryDevice);
        queryButton.pack();
        self.populateDevList();
