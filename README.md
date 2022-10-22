# embedded_system_lab3

### About

這次作業的目標是在Raspberry Pi上執行BLE Central的Python程式，去跟Android手機app的`BLE Tool`所提供的`GATT server`溝通。

### How to Setup

#### Step 1
在Android手機上下載`BLE Tool`的app，然後打開`GATT server`

#### Step 2
準備好一個Rasperry Pi用來執行我們的Python程式。為了確保能夠正常執行，請先確認是否影精裝好`python3-pip`、`libglib2.0-dev`、`bluepy`。如果尚未安裝，請在Raspberry Pi上執行以下程式碼:
```
sudo apt install python3-pip
sudo apt install libglib2.0-dev
sudo pip install bluepy
```

#### Step 3
在Raspberry Pi上執行
```
python3 ble_changeCCCD.py
```
就開始執行我們的程式，並等待裝置掃描

### Step 4
輸入印在terminal上要連線的裝置代號

### Step 5
確認terminal上所列的訊息以及App`BLE Tool`的server log

### Function

在這次的作業中，我們透過了`bluepy`實現了以下功能:
* 改變`CCCD value`以主動開啟`GATT Server`service的`notify`功能
* 在`characteristic write value`被改變時，程式會去接收來自`GATT Server`的`notification`

### Demo

* 以下為terminal所顯示的結果:

* 以下為App的server log結果:
