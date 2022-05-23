# BLE_DMM_Client
Bluetooth Multimeter Client
## Support Models
Aneng 9002, BSIDE ZT-300AB, ZOYI ZT-300AB <br>
(BK3432 BT5.0 with 11 Byte Data) <br>
Just tested with ZOYI ZT-300AB. This solution is very cheap, I just bought a new one by 85 RMB (~ 13 USD). <br>
This is the cheapest with capability to connect with Mobile Phone or Computer. They officially provide Mobile Phone vsersion. So I just open this project for fun. <br>
## Achived functions
- BLE devices Browser <br>
- Real time display <br>
## Ui
<img width="512" alt="image" src="https://user-images.githubusercontent.com/45794975/169850282-e5b92050-d4e4-4bbd-a300-ee410a5a40ed.png">

## Things To Do
- Data Export <br>
- Real time plot <br>
## Development
Python 3.8 <br>
PyQt5 + Bleak <br>
The way to compile for Windows: <br>
`pyinstaller -F -w main.py`<br>
Cross-platform ability in theory, but not test yet. <br>
## License
GPL v3.0
## References
https://github.com/ludwich66/Bluetooth-DMM <br>
https://github.com/webspiderteam/Bluetooth-DMM-For-Windows/tree/master/BluetoothLEExplorer
