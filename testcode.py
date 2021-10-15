from blecontroller.model import BLEHandle

bleHandle = BLEHandle();
names = bleHandle.getDeviceNames();
print(names);

for i in range(0, len(names)):
    bleHandle.getServices(i);
