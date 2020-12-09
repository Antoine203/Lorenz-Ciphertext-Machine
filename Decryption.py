from Encryption import Encryption
from Encoding import Encoding


class Decryption:
    _encrypt = Encryption()
    _key = ""
    _code = ""
    _encode = Encoding()

    # Collect the Key from the Encryption File
    def getKey(self, key):
        self._key = key
        return self._key

    # Collect the Encryption from the Encryption File
    def getCode(self, code):
        self._code = code
        return self._code

    def decrypt(self):
        # Object of Messages:
        #       Position 0 = Display Version ------------ Position 1 = Regular Version
        message = self._decryptMessageBinary()

        # Message as Alpha
        alpha = self._decryptAlphaCorrespondence(message[1])

        print "Message (Binary): " + message[0]
        print "Message (Alpha): " + alpha

    def _decryptAlphaCorrespondence(self, message):
        i = 0
        j = 0
        k = 0
        code = ""
        alpha = ""
        encodings = self._encode.getEncoding()
        # Obtain characters in message
        while i < len(message):
            if j == 5:
                j = 0
                for index in encodings:
                    if code == index:
                        alpha += self._encode.getAlphaFigures()[k]
                        k = 0
                        break
                    k += 1
                code = ""
            code += message[i]
            j += 1
            i += 1

        # To obtain last character in message
        for index in encodings:
            if code == index:
                alpha += self._encode.getAlphaFigures()[k]
                k = 0
                break
            k += 1
        return alpha




    # Decrypts the User's Encrypted Message back to the original Binary Message
    def _decryptMessageBinary(self):
        i = 0
        j = 0
        k = 0
        _messageMemory = []
        _message = ""
        _messageDisplay = ""
        code = self._code
        key = self._key
        print "Decryption Key: "
        print key
        print "Decryption Code: " + code
        while i < len(code):
            if k == 5:
                _messageDisplay += " "
                k = 0
                j += 1
            if key[j][k] == code[i]:
                _messageDisplay += "0"
                _message += "0"
            else:
                _messageDisplay += "1"
                _message += "1"
            i += 1
            k += 1
        _messageMemory.append(_messageDisplay)
        _messageMemory.append(_message)

        return _messageMemory


