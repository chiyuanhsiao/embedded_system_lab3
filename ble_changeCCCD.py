from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Recevied new data from", dev.addr)
        


scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)
n = 0
addr = []
for dev in devices:
    if(dev.rssi >= -80):
        print("%d:Device %s (%s), RSSI=%d dB"% (n, dev.addr, dev.addrType, dev.rssi))
        addr.append(dev.addr)
        n += 1
        for (adtype, desc, value) in dev.getScanData():
            print(" %s = %s"%(desc, value))

number = input('Enter your device number:')
print('Device', number)
num = int(number)
print(addr[num])
#
print("Connecting...")
for i in range(3):
    try:
        dev = Peripheral(addr[num], 'random')
        break
    except:
        print("try (%d/3)", i + 1)
#
print("Services...")
for svc in dev.services:
    print(str(svc))
#
try:
    setup_data = b"\x02\x00"
    
    testService = dev.getServiceByUUID(UUID(0xfff0))
    for ch in testService.getCharacteristics():
        print(str(ch), ch.propertiesToString())
        i = ch.getHandle()
        for dpt in ch.getDescriptors():
            i += 1
            if (str(dpt.uuid) == "00002902-0000-1000-8000-00805f9b34fb"):
                print("Found CCCD!")
                try:
                    dev.writeCharacteristic(i, setup_data, withResponse=True)
                    print("change CCCD value into 2")
                except:
                   print("fail to change CCCD value")
         
finally:
    dev.disconnect()
