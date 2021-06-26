pyinstaller main.py --onefile
mv dist/main ./tbrws
# Remove End of file
rm -rf dist
rm -rf build
rm -rf __pycache__
rm -f main.spec
rm -f /usr/local/bin/tbrmv ./tbrws
mv ./tbrws /usr/local/bin/