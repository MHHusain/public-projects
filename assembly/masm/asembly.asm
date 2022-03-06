.386 ; 386 Processor Instruction Set

.model flat,stdcall ; Flat memory model and stdcall method

option casemap:none ; Case Sensitive

;Libaries and Include files used in this project

; Windows.inc defines alias (such as NULL and STD_OUTPUT_HANDLE in this code
include \masm32\include\windows.inc 

; Functions that we use (GetStdHandle, WriteConsole, and ExitProcess)
; Listing of all available functions in kernel32.lib
include \masm32\include\kernel32.inc 
; Actuall byte code available of the functions
includelib \masm32\lib\kernel32.lib  

.data
; Labels that with the allocated data (in this case Hello World!...) that are aliases to memory.
output db "Hello World!", 0ah, 0h; This String Hello World! and then a the newline character \n (0ah) and then the null character 0h

.code 
start: 

; --------------------------------------------------------------------------------------------------------------------------------------
; Retrieves that handle to the output console
;
; ====Arguments===
;
; STD_OUTPUT_HANDLE - alias for -11 and indicates that we want the handle to 
;                     write to console output
;
invoke GetStdHandle, STD_OUTPUT_HANDLE
; --------------------------------------------------------------------------------------------------------------------------------------

; --------------------------------------------------------------------------------------------------------------------------------------
; Writes the text in output (.data section) to the console
;
; ====Arguments===
;
; eax - the handle to the console buffer
;
; addr output - pass by reference the text of output (Hello World!)
;
; sizeof output - the size of the string so that the WriteConsole knows when to 
;                 stop (doesn't support NULL terminated strings I guess);
;
; ebx - secondary "return" value that contains the number of bytes written (eax
;       is used for an error code)
;
; NULL - this is reserved and MSDN says just to pass NULL
;
; MSDN Link: http://msdn.microsoft.com/en-us/library/ms687401(v=VS.85).aspx
;
invoke WriteConsole, eax, addr output, sizeof output, ebx, NULL
; --------------------------------------------------------------------------------------------------------------------------------------

; --------------------------------------------------------------------------------------------------------------------------------------
; Exits the program with return code 0 (default one that usually is used to 
; indicate that the program did not error
;
; ====Arguments===
;
; 0 - the exit code
;
; MSDN Link: http://msdn.microsoft.com/en-us/library/ms682658(VS.85).aspx
;
invoke ExitProcess, 0
; --------------------------------------------------------------------------------------------------------------------------------------

end start