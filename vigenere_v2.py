# Small Python program that demonstrates vigenere cipher
# Created by SKS bros.

count=0

j=0

temp_key=""

key=""

print("1.Encryption")

print("2.Decryption")

i=input("Choose an option(1 or 2 ): ")

# condition for encrypting or decrypting

if(i=="1"):

    msg=input("Enter Message To Encrypt: ")
    message = msg.lower()
    key=input("Key: ")

    message_length=len(message)

    key_length=len(key)
    j=0
    for count in range(0,message_length):
        if(j==key_length):
            j=0

        temp_key+=key[j]
        j+=1
   

    count=0

    encrypted_message=""


    while(count<message_length):

        encrypted_message+=chr(((ord(message[count])+ord(temp_key[count]))%26+ord('A')))

        count+=1

    print("Encryped Message:\n",encrypted_message)    

elif(i=="2"):

    message=input("Enter the Message to Decrypt: ")

    key=input("Enter Key: ")

    message_length=len(message)

    key_length=len(key)

    count=0
    j=0

    for count in range(0,message_length):

        if(j==key_length):
            j=0

        temp_key+=key[j]
        j+=1
    count=0

    decrypted_message = ""

    while(count<message_length):
        decrypted_message+=chr(((ord(message[count])-ord(temp_key[count])+98)%26)+ord('A'))

        count+=1

    print("Decrypted Message:\n",decrypted_message)

else:

    print("Invalid Option")
