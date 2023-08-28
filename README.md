# BLE_DMM_Client
Bluetooth Multimeter Client <br>
蓝牙万用表客户端
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
- [x] None <br>
## Development
# Requirements
Python 3.8 <br>
pyside6 pyqtgraph bleak <br>
Also need Nuitka (or pyinstaller if you wanted) <br>
If using Linux, need BlueZ >= 5.43 (additionally required by bleak) <br>
Whether using conda (or other virtual env management) or not, it's recommended to use 'pip install' to install all packages listed in requirements.txt. <br>
# The way to compile for Windows:
## Environment：
First install the nuitka: <br>
`pip install nuitka` <br>
## Compile
### Script for Windows
Enter your enviroonment (Virtual recommand) -> Install all packages needed -> Enter ./Releases fold and type 'Compile_Windows.bat' to run script.
### Manually Compile
nuitka will occur crash with pyqtgraph (see issue #1532 in nuitka, Github). So delete the export function in pyqtgraph.<br>
```shell
# Enter fold
cd ./Releases
# All the resource files are included in ./Ui/resources.qrc. Then enter Ui fold and run if rousources been modified.
# Entering Pyside6-rcc Resources Compile
pyside6-rcc ../Ui/resources.qrc -o ../Ui/resources_rc.py

# Entering Nuitka Single File Compile
python -m nuitka --standalone --windows-disable-console --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Single" --onefile ../main.py

# Entering Nuitka Single File Debug Compile
python -m nuitka --standalone --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Single_Debug" --onefile ../main.py

# Entering Nuitka Normal Compile
python -m nuitka --standalone --windows-disable-console --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Normal" ../main.py
```

Then, for Windows, you can run directly or pack it with NSIS or other pack programs such as advanced installer. <br>

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
