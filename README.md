# BLE_DMM_Client
Bluetooth Multimeter Client
## Support DMM Models
Aneng 9002, BSIDE ZT-300AB, ZOYI ZT-300AB (Multimeter with 11 Byte Data) <br>
Aneng V05B	BSIDE ZT-5B	ZOYI ZT-5B (Small-Multimeter with 10 Byte Data) <br>
Not  tested: Aneng ST207	BSIDE ZT-5BQ	ZOYI ZT-5BQ	(Clamp-Multimeter with 10 Byte Data) <br>


| Type:                    | Models       |                |               | Test          |
| :----------------------- | :----------- | :------------- | :------------ | :------------ |
| 1. Multimeter (1):       | Aneng 9002   | BSIDE ZT-300AB | ZOYI ZT-300AB | Yes           |
| 2. Small-Multimeter (2): | Aneng V05B   | BSIDE ZT-5B    | ZOYI ZT-5B    | Not completely|
| 3. Clamp-Multimeter (3): | Aneng ST207  | BSIDE ZT-5BQ   | ZOYI ZT-5BQ   | Not completely|
| 4. Clamp-Multimeter (4): | Aneng AN999S |                | ZOYI ZT-5566S | Not completely|


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
- Real time plot <br>
- Multilanguage <br>
- Multithemes <br>
## UI
v3.0 in win11: <br>
<br>
<img width="654" alt="image" src="https://github.com/840922704/BLE_DMM_Client/blob/6b8bd3faa6351fe2b8a9bddaab4d352b38588ce1/UI.png">
## Things To Do
- [x] ~~Data Export~~ <br>
- [x] ~~Real time plot~~ <br>
## Development
# Requirements
Python 3.8 <br>
PyQt5 pyqt5-tools pyqtgraph bleak <br>
# The way to compile for Windows:
## Environment：
First install the nuitka: <br>
`pip install nuitka` <br>
## Compile
Then pack with nuitka: <br>
`nuitka --standalone --windows-disable-console --show-progress --enable-plugin=pyqt5  --enable-plugin=numpy --windows-icon-from-ico=The_Path_of_Logo.ico main.py` <br>
Then pack with nuitka whit console to debug: <br>
`nuitka --standalone --show-progress --enable-plugin=pyqt5  --enable-plugin=numpy --windows-icon-from-ico=The_Path_of_Logo.ico main.py` <br>
After compiled, copy Logo.png、Logo.ico、Ui fold and qt_material fold to the app's root file. <br>
Then, for Windows, you can run directly or pack it with NSIS or other pack programs such as advanced installer. <br>

## Compile error

Compiled file may get the error below:
```
File "C:\MAIN~1.DIS\pyqtgraph\graphicsItems\ButtonItem.py", line 19, in __init__
ZeroDivisionError: float division by zero
```
They just fix this bug in [2022.04](https://github.com/pyqtgraph/pyqtgraph/blob/a237b6e6a606b6625069a39cda9aa072e07e1882/pyqtgraph/graphicsItems/ButtonItem.py), the pip version is old, so just fix it manually, change line 18 of ButtonItem.py in your env:
`if width is not None:` to `if width is not None and self.pixmap.width():` <br>
Cross-platform ability in theory, but not tested yet. <br>

## License
GPL v3.0
## References
https://github.com/ludwich66/Bluetooth-DMM <br>
https://github.com/Shiro-Nek0/Bluetooth-DMM.py <br>
https://github.com/webspiderteam/Bluetooth-DMM-For-Windows/tree/master/BluetoothLEExplorer
