encrypted_message = "zkdw#duh#|rx#orrnlqj#iruB#Glg#|rx#h{shfw#wr#vhh#wkhuh#vrph#lpsruwdqw#wklqjvB"
decrypted_message = ""
key = 3

for sign in (encrypted_message):
    decrypted_message += chr(ord(sign) - key)
    # print(unlock)
print(decrypted_message)