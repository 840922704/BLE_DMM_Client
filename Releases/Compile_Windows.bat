@echo off
echo Nuitka Single File
python -m nuitka --standalone --windows-disable-console --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Single" --onefile ../main.py

echo Nuitka Single File Debug
python -m nuitka --standalone --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Single_Debug" --onefile ../main.py

echo Nuitka Normal
python -m nuitka --standalone --windows-disable-console --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Normal" ../main.py

pause