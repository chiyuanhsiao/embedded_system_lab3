from bluepy.btle import Peripheral, UUID
from bluepy.btle import Scanner, DefaultDelegate

ID = b"\x00"

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)
    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Recevied new data from", dev.addr)
    def handleNotification(self, cHandle, data):
#        print(str.decode(data))
        global ID
        ID = data
        


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
        print("try(%d/3)", i + 1)
#
print("Services...")
for svc in dev.services:
    print(str(svc))
#
try:
    setup_data = b"\x02\x00"

#   ch = dev.getCharacteristics(uuid=UUID(0xfff4))[0]
#   cccd = ch.getHandle() + 2
#   try:
#       dev.writeCharacteristic(cccd, bytes([0x01, 0x00]), withResponse=True)
#       print("change cccd!")
#       if (ch.supportsRead()):
#       print(ch.read())
#   except:
#       print("fail to change CCCD")
#
        

    
    testService = dev.getServiceByUUID(UUID(0xfff0))
    for ch in testService.getCharacteristics():

        print(str(ch), ch.propertiesToString())
        string = ch.read()
        print(string)
        i = ch.getHandle()
        for dpt in ch.getDescriptors():
            i += 1
            if (str(dpt.uuid) == "00002902-0000-1000-8000-00805f9b34fb"):
                print("Found CCCD!")
                try:
                    dev.writeCharacteristic(i, setup_data, withResponse=True)
                    print("change CCCD value into ", dev.readCharacteristic(i))
                    print(str(ch), ch.propertiesToString())
                except:
                   print("fail to change CCCD value")
    target = dev.getCharacteristics(uuid=UUID(0xfff4))[0]
    target_handle = target.getHandle()
    dev.writeCharacteristic(target_handle, str.encode("EMO_BLUE"), withResponse=True)
    
    print(dev.readCharacteristic(target_handle))
    if(target.supportsRead()):
        byte_data = target.read()
        val = byte_data.decode()
        print(val)
     
    while True:
        if dev.waitForNotifications(1.0):
            print("get")  
            print(str(ID.decode()))
            continue
            # handleNotification() was called
        print("waiting")  
         
finally:
    dev.disconnect()
