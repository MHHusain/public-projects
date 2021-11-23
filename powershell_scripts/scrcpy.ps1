# $random_port = Get-Random -Minimum 5555 -Maximum 5600
# Set-Location "C:\Users\NS\Desktop\scrcpy-win64-v1.17"
# . "C:\Users\NS\Desktop\scrcpy-win64-v1.17\adb.exe" tcpip $random_port
. "C:\Users\NS\Desktop\scrcpy-win64-v1.17\adb.exe" connect 192.168.0.13:5556

. "C:\Users\NS\Desktop\scrcpy-win64-v1.17\scrcpy.exe" -s 192.168.0.13:5556