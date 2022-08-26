@echo off
<adb path> disconnect
<adb path> connect <ip>:<port>
cls
<adb path> install %1
pause
