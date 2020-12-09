from Encryption import Encryption
from Decryption import Decryption
from Encoding import Encoding
# Fix --- Handle One Character -> Also, Build Interface
# Instances of Classes
encryp = Encryption()
decrypt = Decryption()
encode = Encoding()


message = raw_input("Enter your message: ")

count = 0
count2 = 0

while len(message) == 0 and count2 != 1:
    if count2 == 1:
        print "Try again some other time."
    count2 += 1
    message = raw_input("Enter some text for your message: ")


print

while encode.checkCharacters(message) and count2 < 1:
    if count == 1:
        print "There was a character in your message that is not supported.\nPlease try again later."
        break
    count += 1
    print "Please enter only the following characters within your message:\nA-Z\n.\n?\n,\n:\nspace\n'\n_____________________________________________"
    message = raw_input("Re-enter your message: ")

if count < 2 and count2 < 2:
    print "_____________________________________________\n\nEncryption Area: \n\n_____________________________________________\n"
    encryp.getMessage(message)
    encryp.generatingEncryptionCode(message)
    print "\n_____________________________________________\n\nDecryption Area: \n\n_____________________________________________\n"
    decrypt.getKey(encryp.getKeyEncode())
    decrypt.getCode(encryp.getCode())
    decryptedMessage = decrypt.decrypt()
