echo Entering Pyside6-rcc Resources Compile
pyside6-rcc ../Ui/resources.qrc -o ../Ui/resources_rc.py

echo Entering Nuitka Single File Compile
python -m nuitka --standalone --windows-disable-console --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Single" --onefile ../main.py

echo Entering Nuitka Single File Debug Compile
python -m nuitka --standalone --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Single_Debug" --onefile ../main.py

echo Entering Nuitka Normal Compile
python -m nuitka --standalone --windows-disable-console --enable-plugin=pyside6 --show-progress --windows-icon-from-ico="..\Ui\Logo.ico" --include-package-data=qt_material --output-dir="./Normal" ../main.py