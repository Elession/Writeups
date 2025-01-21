## pwnnie_warmup

The server outputs the return address of the flag for the challenge.

This is a basic ret2win challenge (buffer overflow + overwrite return address).

The only issue was that the return address is dynamic based on the connection. So i just extracted the address based on what I received when connecting (unlike in Picoctf where the address is static).