# embedded_system_lab3

### About

這次作業的目標是在Raspberry Pi上執行BLE Central的Python程式，去跟Android手機app的 BLE Tool所提供的GATT server溝通。

### How to Setup

#### Step 1
在Android手機上下載BLE Tool的app，然後打開GATT server

#### Step 2
準備好一個Rasperry Pi用來執行我們的Python程式。為了確保能夠正常執行，請先確認是否影精裝好python3-pip、libglib2.0-dev、bluepy。如果尚未安裝，請在Raspberry Pi上執行以下程式碼:
'''
    sudo apt install python3-pip
    sudo apt install libglib2.0-dev
    sudo pip install bluepy
'''

#### Step 3
在Raspberry Pi上執行
'''
    python3 ble_changeCCCD.py
'''
就開始執行我們的程式
