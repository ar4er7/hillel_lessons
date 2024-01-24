
message = "what are you looking for? Did you expect to see there some important things?"
encrypted_message = ""
decrypted_message = ""

key = 3
# o_char = ord(message[0])
# f_char = ord(message[0])+1
# print(o_char, f_char)

for character in message:
    encrypted_message += chr(ord(character) + key)

print(encrypted_message)


for sign in (encrypted_message):
    decrypted_message += chr(ord(sign) - key)
    # print(unlock)
print(decrypted_message)


# for index_of_char in range(ord("A"), ord("z")+1):
#     if not chr(index_of_char).isalpha():
#         continue
#     print(chr(index_of_char), index_of_char)
