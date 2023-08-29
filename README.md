# BLE_DMM_Client 蓝牙万用表客户端
An Bluetooth Multimeter Client. Using Pyside6 and bleak. <br>
适配市场主流蓝牙通讯的万用表，使用pyside6和bleak <br>
## UI
v3.2 in win11: <br>
<br>
<img width="654" alt="image" src="https://github.com/840922704/BLE_DMM_Client/blob/main/Preview.png">
## Support DMM Models

| Type:                    | Models       |                |               | Test          |
| :----------------------- | :----------- | :------------- | :------------ | :------------ |
| 1. Multimeter (1):       | Aneng 9002   | BSIDE ZT-300AB | ZOYI ZT-300AB | Yes           |
| 2. Small-Multimeter (2): | Aneng V05B   | BSIDE ZT-5B    | ZOYI ZT-5B    | Yes           |
| 3. Clamp-Multimeter (3): | Aneng ST207  | BSIDE ZT-5BQ   | ZOYI ZT-5BQ   | Yes           |
| 4. Desk-Multimeter (4):  | Aneng AN999S |                | ZOYI ZT-5566S | Not completely|


Just tested with ZOYI ZT-300AB. This solution is very cheap, I just bought a new one by ~ 100 RMB (~ 10 + USD). <br>
<br>
This is the cheapest with capability to connect with Mobile Phone or Computer. They officially provide Mobile Phone version. So I just open this project for fun. <br>
## Supported OS
| Operate System| Code Version         | Released Version | Test          |
| :------------ | :------------------- | :--------------- | :------------ |
| Windows       | x86/x64 10 and above*| x64 10 and above*| Yes           |
| Linux         | x86/x64              | No               | Not completely|
| Mac OS        | x86/x64              | No               | Not completely|

\* *Because the BLE module bleak just support win10 and above in windows platform.* <br>
Windows(10 and above), Linux and MAC OS (platform supported by python). <br>
Just tested in Windows and exe release version of Windows.
## Achived functions
- BLE devices Browser <br>
- Real time display <br>
- Data Export <br>
- Real time plot <br>
- Multi-devices
- Multi-languages <br>
- Multi-themes <br>
## Things To Do
- None <br>
- Maybe self-defined ble decoder support in the future.<br>

## Development
# Requirements
Python 3.8 <br>
pyside6 pyqtgraph qt_material bleak <br>
Also need Nuitka (or pyinstaller if you wanted) <br>
If using Linux, need BlueZ >= 5.43 (additionally required by bleak) <br>
Whether using conda (or other virtual env management) or not, it's recommended to use 'pip install' to install all packages listed in requirements.txt. <br>
# The way to compile for Windows:
## Environment：
First install the nuitka: <br>
`pip install nuitka` <br>
## Compile (Scripts for Windows)
See the files in releases fold for detail.
### Nuitka
Enter your enviroonment (Virtual recommand) -> Install all packages needed -> Enter ./Releases fold and type 'Compile_Windows.bat' to run script.<br>
nuitka will occur crash with pyqtgraph (see issue #1532 in nuitka, Github). So the export function in pyqtgraph had been deleted.<br>
**Note**: All the resource files are included in ./Ui/resources.qrc.<br>
### Advanced Installer
Then, for Windows, you can run directly or pack it with NSIS or other pack programs such as advanced installer. <br>
For example, using "BLE DMM Client.aip" in /Releases/Advanced_Install.<br>
### Zip for Releases
Run "/Releases/3.Copy_and _Compress.bat".
## Known issues

### Compiled file may get the error below:
```
File "C:\MAIN~1.DIS\pyqtgraph\graphicsItems\ButtonItem.py", line 19, in __init__
ZeroDivisionError: float division by zero
```
They just fix this bug in [2022.04](https://github.com/pyqtgraph/pyqtgraph/blob/a237b6e6a606b6625069a39cda9aa072e07e1882/pyqtgraph/graphicsItems/ButtonItem.py), if you use old version, please fix it manually, change line 18 of ButtonItem.py in your env:
`if width is not None:` to `if width is not None and self.pixmap.width():` <br>
Cross-platform ability in theory, but not tested yet. <br>

### qt_material issue
qt_material's dark theme have some issues with pyside6. Current version (2.14) not fixed yet, so manually add part of stylesheet in main.py.
```python
self.apply_stylesheet(self, theme='dark_lightgreen.xml', extra=extra)
tooltip_stylesheet = """
    QToolTip {
        background-color: black;
    }
    QComboBox {
        color: white;
    }
"""
self.setStyleSheet(self.styleSheet()+tooltip_stylesheet)
```

## License
GPL v3.0
## References
https://github.com/ludwich66/Bluetooth-DMM <br>
https://github.com/Shiro-Nek0/Bluetooth-DMM.py <br>
https://github.com/webspiderteam/Bluetooth-DMM-For-Windows/tree/master/BluetoothLEExplorer
