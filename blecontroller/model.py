#!/usr/local/bin/python3
import asyncio
import time
from bleak import BleakScanner
from bleak import BleakClient

async def deviceScan(devices):
    devs = await BleakScanner.discover();
    for entry in devs:
        devices.append(entry);

async def serviceDiscovery(device, services):
    svcs = await BleakClient(device).get_services();
    for svc in svcs:
        services.append(svc); 

class BLEHandle:
    def __init__(self):
        self.devices = [];

    def runDeviceScan(self):
        self.devices.clear();
        asyncio.run(deviceScan(self.devices));
         
    def getDeviceNames(self):
        self.runDeviceScan();
        ret = []
        for device in self.devices:
            ret.append(device.name);
        return ret; 

    def getServices(self, idx):
        if (idx >= len(self.devices)):
            return None;
        services = []
        asyncio.run(serviceDiscovery(self.devices[idx], services));
        print("Found ", len(services), " services for device ", self.devices[idx].name);
        for service in services:
            print(service);
