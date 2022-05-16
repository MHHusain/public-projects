.386
.model flat,stdcall
option casemap:none
include \masm32\include\windows.inc 
include \masm32\include\kernel32.inc 
includelib \masm32\lib\kernel32.lib  
.data
output db "Hello World!", 0ah, 0h
.code 
main: 
invoke GetStdHandle, STD_OUTPUT_HANDLE
invoke WriteConsole, eax, addr output, sizeof output, ebx, NULL
invoke ExitProcess, 0
end main