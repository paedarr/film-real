def readKeys(counter):
    with open('user-files/keys.txt', 'r') as file:
        for line in file:
            if (line == counter):
                return line
            # unused, save if needed -> print(line, end='')
        file.close()

def readPasswords(thisKey, counter):
    with open('user-files/passwords.txt', 'r') as file:
        read_encrypted_data = file.read()
        file.close()
    
def writeKeys():
    with open('user-files/keys.txt', 'w') as file:
        file.write(encrypted_data)
        file.close()
    
def writePasswords():
    with open('user-files/passwords.txt', 'w') as file:
        file.write(encrypted_data)
        file.close()



