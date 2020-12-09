from Encoding import Encoding
import random


class Encryption:
    # Creating Instance of Encodings
    _encryption = Encoding()
    _alphaBank = _encryption.getAlphaFigures()
    _encodingBank = _encryption.getEncoding()

    # Initializing the Psi-key, Chi-key, Key, Message, Encoding Array and Code
    _psiKey = ""
    _chiKey = ""
    _code = ""
    _message = ""
    _count = 0
    _key = ""
    _encodings = []

    # All Keys will be Generated as Letters
    def _generatingKey(self):
        length_message = len(self._message)

        # Message length of 1
        if length_message == 1:
            randomIndex = random.randint(0, 31)
            self._key = self._alphaBank[randomIndex]
            self._encodings.append(self._encodingBank[randomIndex])
        # Message length is Divisible by 2
        elif (length_message % 2) == 0:
            _half = length_message / 2
            for i in range(length_message):
                randomIndex = random.randint(0, 31)
                if i < _half:
                    self._psiKey += self._alphaBank[randomIndex]
                    self._encodings.append(self._encodingBank[randomIndex])
                if i >= _half and self._count < length_message:
                    self._chiKey += self._alphaBank[randomIndex]
                    self._encodings.append(self._encodingBank[randomIndex])
            self._key = self._psiKey + self._chiKey
        # Message length is a Odd Number
        else:
            firstHalf = length_message / 2
            for i in range(length_message):
                randomIndex = random.randint(0, 31)
                if i < firstHalf:
                    self._psiKey += self._alphaBank[randomIndex]
                    self._encodings.append(self._encodingBank[randomIndex])
                if i >= firstHalf and self._count < length_message:
                    self._chiKey += self._alphaBank[randomIndex]
                    self._encodings.append(self._encodingBank[randomIndex])
            self._key = self._psiKey + self._chiKey

        return self._key

    # Key Alpha
    def getKey(self):
        return self._key

    # Key Encoding
    def getKeyEncode(self):
        return self._encodings

    # Code
    def getCode(self):
        return self._code

    # Collects the User's Message
    def getMessage(self, message):
        if True:
            self._message = message
            print "Successfully received the message."
        else:
            print "Did not receive the message."

    # Encodes the User's Message
    def generatingEncryptionCode(self, _userMessage):
        # Creates the Key
        key = self._generatingKey()

        values = []

        print "Message: " + _userMessage
        print "Key Alpha_Symbols: " + key + "\n"
        code = self._encodingMessageBinary(key, _userMessage)
        alphaCode = self._encodingMessageAlphaSymbols(code)

        # Setting Key & Code Values for Decryption
        self._key = key
        self._code = code[0]

        # UNCOMMENT TO SEE KEY ENCODINGS
        messageLength = len(self._message)
        for i in range(messageLength):
            print "Key Encodings " + str(i) + ": " + self._encodings[i]

        print "\nEncryption: " + code[1]

        print "Encryption in Alpha_Symbols: " + alphaCode

        values.append(code[1])
        values.append(alphaCode)
        return values

    # Encryption Generator --> Adding Key and Message Together --> Binary Display
    def _encodingMessageBinary(self, key, _usermessage):
        code = ""
        codeDisplay = ""
        coder = []

        # Converting the Message to its Binary Correspondence Values
        messageEncodings = self._convertMessage(_usermessage)
        # Message Length in Characters
        messageCodeLength = len(_usermessage)
        i = 0
        k = 0

        while i < messageCodeLength:
            j = 0

            for character in messageEncodings[i]:
                if (j % 5) == 0:
                    codeDisplay += " "
                if character == self._encodings[i][j]:
                    code += "0"
                    codeDisplay += "0"
                else:
                    code += "1"
                    codeDisplay += "1"
                j += 1
            i += 1

        # Used for Alpha Conversion Category
        coder.append(code)

        # Code Display --> Used for Elegant Display to User
        coder.append(codeDisplay)
        return coder

    # Encryption Generator --> Adding Key and Message Together --> Letters & Symbols Display
    def _encodingMessageAlphaSymbols(self, code):
        alphaCoding = []
        alpha = ""
        alphaEncoding = ""
        for index in code[0]:
            alpha += index
            if (len(alpha) % 5) == 0:
                alphaCoding.append(alpha)
                alpha = ""
        for index in range(len(alphaCoding)):
            i = 0
            while i < len(self._encodingBank):
                if self._encodingBank[i] == alphaCoding[index]:
                    alphaEncoding += self._alphaBank[i]
                i += 1
            i = 0
        return alphaEncoding

    # Converting the Message to its Binary Correspondence Values
    def _convertMessage(self, userMessage):
        messagePiece = []
        message = userMessage.upper()
        print "Message: (Read into Bank) " + message + "\nLength of Message: " + str(range(0, len(message)))
        # Converting the Message into Corresponding Encodings
        for index in range(0, len(message)):
            count = 0
            while count < len(self._alphaBank):
                if message[index] == self._alphaBank[count]:
                    messagePiece.append(self._encodingBank[count])
                    print "Message Encodings " + str(index) + ": " + messagePiece[index]

                count += 1
        return messagePiece
