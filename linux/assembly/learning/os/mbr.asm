
mov al, 65

mov ah, 0x0e
loop1:
	cmp al, 'Z' + 1
	je end1
	int 0x10
	add al,33
	int 0x10
	sub al,31
	jmp loop1
end1:
jmp $
times 510-($-$$) db 0
db 0x55,0xaa
