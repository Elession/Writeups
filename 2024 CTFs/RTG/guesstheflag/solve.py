import socket

max_char = 29
chars = "ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwxyz1234567890-=[]\;',./!@#$%^&*()_+{}|:\"<>?"
flag = "RTG"

# Loop through each character position in the flag
for i in range(3, max_char + 1):
    found = False
    for el in chars:
        server =socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server.connect(('server', 0000))

        # Ensure code can receive enough (because of the checks)
        data = server.recv(2048).decode()

        #  Payload is always 29 char long, the remaining unchecked characters are placement holders 
        payload = flag + el + ('a' * (max_char - i - 1))
        print(f"Sending payload: {payload}")

        server.send(payload.encode())
        server.send(b'\n')

        # Receive and decode server reply 
        reply = server.recv(2048).decode()
        print(f"Received reply: {reply}")
        print(i)

        # Break once correct character is found to start checking for next index
        if "{} is on target.".format(i) in reply:
            flag += el
            print('yes')
            found = True
            break 
            
print(flag)