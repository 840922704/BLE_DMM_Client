@ rem Pack with PyInstaller in Windows, python3.8
set "script_dir=%~dp0"
cd "%script_dir%"

echo Entering Pyside6-rcc Resources Compile
pyside6-rcc ..\..\Ui\resources.qrc -o ..\..\Ui\resources_rc.py

set main_py_path="..\..\main.py"
set name="BLE DMM Client"
set upx_dir=".\Tools\upx-4.1.0-win64"
@ rem Relative to work path, so set the script_dir to it
set icon_dir="%script_dir%..\..\Ui\Logo.ico"
set splash_dir="%script_dir%..\..\Ui\splash.png"
set portable_work_path=".\build\win64_pyinstaller_Portable"
set portable_dist_path=".\dist\win64_pyinstaller_Portable"
set single_work_path=".\build\win64_pyinstaller_Single"
set single_dist_path=".\dist\win64_pyinstaller_Single"
set single_debug_work_path=".\build\win64_pyinstaller_Single_Debug"
set single_debug_dist_path=".\dist\win64_pyinstaller_Single_Debug"

@ rem -F for Singlefile
@ rem -w for no-console

pyInstaller %main_py_path% --name=%name% -w --clean --noconfirm --upx-dir=%upx_dir% --icon=%icon_dir% --workpath=%portable_work_path% --specpath=%portable_work_path% --distpath=%portable_dist_path%

pyInstaller %main_py_path% --name=%name% -Fw --clean --noconfirm --upx-dir=%upx_dir% --icon=%icon_dir% --splash %splash_dir% --workpath=%single_work_path% --specpath=%single_work_path% --distpath=%single_dist_path%

pyInstaller %main_py_path% --name=%name% -F --clean --noconfirm --upx-dir=%upx_dir% --icon=%icon_dir% --splash %splash_dir% --workpath=%single_debug_work_path% --specpath=%single_debug_work_path% --distpath=%single_debug_dist_path%