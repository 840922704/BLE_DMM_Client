@ rem Copy and Compress

cd /d %~dp0

del .\Final_Releases\BLE.DMM.Client.x64_win_Installer.zip
.\Tools\zip.exe -j .\Final_Releases\BLE.DMM.Client.x64_win_Installer.zip ".\Advanced_Install\BLE DMM Client-SetupFiles\BLE DMM Client.exe"

del .\Final_Releases\BLE.DMM.Client.x64_win_Single.zip
.\Tools\zip.exe -j .\Final_Releases\BLE.DMM.Client.x64_win_Single.zip ".\dist\win64_pyinstaller_Single\BLE DMM Client.exe"

del .\Final_Releases\BLE.DMM.Client.x64_win_Single_Debug.zip
.\Tools\zip.exe -j .\Final_Releases\BLE.DMM.Client.x64_win_Single_Debug.zip ".\dist\win64_pyinstaller_Single_Debug\BLE DMM Client.exe"