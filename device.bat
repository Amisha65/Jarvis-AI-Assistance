@echo off
echo Checking for existing ADB connections...
adb devices

:: Check if the device is connected via USB first
for /f "tokens=1" %%a in ('adb devices ^| findstr /i "device"') do (
    set DEVICE=%%a
)

:: If device is already connected over Wi-Fi, skip USB connection
if defined DEVICE (
    echo Device %DEVICE% already connected.
    echo Connecting over Wi-Fi...
    adb connect %DEVICE%:5555
    goto :end
)

:: If no device is found, connect via USB first
echo No device found over Wi-Fi, connecting over USB...
adb devices
adb tcpip 5555
echo Disconnecting USB...
adb disconnect

:: Wait for device to switch to TCP mode
timeout /t 5

:: Get the IP address of the Android device (it should be connected via USB)
for /f "tokens=2" %%G in ('adb shell ip addr show wlan0 ^| find "inet "') do set ipfull=%%G
for /f "tokens=1 delims=/" %%G in ("%ipfull%") do set ip=%%G

:: Connect to the device over Wi-Fi using the obtained IP address
echo Connecting to device with IP %ip%...
adb connect %ip%:5555

:end
echo Process completed. You can now control the device over Wi-Fi.
pause
