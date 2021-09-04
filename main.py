import tkinter as tk
from tkinter import ttk

class FirstView(ttk.Frame):
    def populateDevList(self):
        print("Populating");
        for entry in self.devices:
            self.devicesBox.insert(tk.END, entry);

    def queryDevice(self):
        idxList = self.devicesBox.curselection();
        if len(idxList):
            print("Selected ", idxList[0], "Of ", len(self.devices));
            device = self.devices[idxList[0]];
            print(device);

    def scanDevices(self):
        self.devices = ["A", "B", "C"];
        self.populateDevList();
    
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs);
        scanButton = ttk.Button(self, text="Scan", command=self.scanDevices);
        scanButton.pack();
        self.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S));
        parent.columnconfigure(0, weight=1);
        parent.rowconfigure(0, weight=1);
        self.devicesBox = tk.Listbox(self);
        self.devicesBox.pack();
        queryButton = ttk.Button(self, text="Query", command=self.queryDevice);
        queryButton.pack();
        self.devices = [];
        self.populateDevList();

class MyApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs);
        self.title("BLE Scanner");
        self.geometry("800x600")
        FirstView(self);

app = MyApplication();
app.mainloop();
