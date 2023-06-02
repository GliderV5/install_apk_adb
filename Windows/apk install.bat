@echo off
<adb_path> disconnect
<adb_path> connect <ip>:<port>
cls
<adb_path> install %1
pause
