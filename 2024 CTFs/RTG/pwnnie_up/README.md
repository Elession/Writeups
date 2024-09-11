## pwnnie_up

My first time dealing with shellcode in pwn.

Quite straight forward since the vulnerability reads & executes any input.

So i just use Pwntools to generate a shell.

This can be done using the following command:

```shell
pwn shellcraft -o shellcraft.sh amd64.linux.sh
```