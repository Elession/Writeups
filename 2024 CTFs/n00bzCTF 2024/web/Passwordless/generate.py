import uuid

leet = uuid.UUID('13371337-1337-1337-1337-133713371337')
test = str(uuid.uuid5(leet,'admin123'))
print (test)

# output: 3c68e6cc-15a7-59d4-823c-e7563bbb326c