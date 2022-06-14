# BLE_DMM_Client
Bluetooth Multimeter Client
## Support DMM Models
Aneng 9002, BSIDE ZT-300AB, ZOYI ZT-300AB (Multimeter with 11 Byte Data) <br>
Aneng V05B	BSIDE ZT-5B	ZOYI ZT-5B (Small-Multimeter with 10 Byte Data) <br>
Not  tested: Aneng ST207	BSIDE ZT-5BQ	ZOYI ZT-5BQ	(Clamp-Multimeter with 10 Byte Data) <br>

Just tested with ZOYI ZT-300AB. This solution is very cheap, I just bought a new one by ~ 100 RMB (~ 10 + USD). <br>
<br>
This is the cheapest with capability to connect with Mobile Phone or Computer. They officially provide Mobile Phone version. So I just open this project for fun. <br>
## Supported OS
Windows, Linux and MAC OS (platform supported by python). <br>
Just tested in Windows and exe release version of Windows.
## Achived functions
- BLE devices Browser <br>
- Real time display <br>
- Data Export <br>
- Real time plot
## UI
v2.0 in win11: <br>
<br>
<img width="654" alt="image" src="https://user-images.githubusercontent.com/45794975/173481159-380d655d-07fd-4462-bd93-7f8b7353c908.png">
## Things To Do
- [x] Data Export <br>
- [x] Real time plot <br>
## Development
# Requirements
Python 3.8 <br>
PyQt5 pyqt5-tools pyqtgraph bleak <br>
# The way to compile for Windows:
First install the nuitka: <br>
`pip install nuitka` <br>
Then pack with nuitka: <br>
`nuitka --standalone --windows-disable-console --show-progress --enable-plugin=pyqt5  --enable-plugin=numpy --windows-icon-from-ico=The_Path_of_Logo.ico main.py` <br>
After compiled, copy Logo.png to app's root file. <br>
Then, for Windows, you can run directly or pack it with NSIS or other pack programs. <br>
Cross-platform ability in theory, but not tested yet. <br>
## License
GPL v3.0
## References
https://github.com/ludwich66/Bluetooth-DMM <br>
https://github.com/Shiro-Nek0/Bluetooth-DMM.py <br>
https://github.com/webspiderteam/Bluetooth-DMM-For-Windows/tree/master/BluetoothLEExplorer
