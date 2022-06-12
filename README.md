# BLE_DMM_Client
Bluetooth Multimeter Client
## Support Models
Aneng 9002, BSIDE ZT-300AB, ZOYI ZT-300AB (BK3432 BT5.0 with 11 Byte Data) <br>
Aneng V05B	BSIDE ZT-5B	ZOYI ZT-5B (BK3432 BT5.0 with 10 Byte Data) <br>
Just tested with ZOYI ZT-300AB. This solution is very cheap, I just bought a new one by 85 RMB (~ 13 USD). <br>
This is the cheapest with capability to connect with Mobile Phone or Computer. They officially provide Mobile Phone vsersion. So I just open this project for fun. <br>
## Achived functions
- BLE devices Browser <br>
- Real time display <br>
## UI
<img width="674" alt="image" src="https://user-images.githubusercontent.com/45794975/173222650-fe2d726f-04fc-4054-b4b9-07a18afece9c.png">

## Things To Do
- [x] Data Export <br>
- [x] Real time plot <br>
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
