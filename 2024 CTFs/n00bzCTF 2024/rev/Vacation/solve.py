enc = 'm33ayxeqln\\sbqjp\\twk\\{lq~'
flag = ''
for i in enc:    
    flag += chr(ord(i) ^ 3)
print(flag)

# Output: n00bz{from_paris_wth_xor}