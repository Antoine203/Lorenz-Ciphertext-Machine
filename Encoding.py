class Encoding:
    # 32 Corresponding Encodings
    _encoding = ["11000", "10011", "01110", "10010", "10000", "10110", "01011", "00101", "01100", "11010", "11110",
                 "01001","00111", "00110", "00011", "01101", "11101", "01010", "10100", "00001",
                 "11100", "01111", "11001", "10111", "10101", "10001", "00010", "01000", "11111",
                 "11011", "00100", "00000"]

    # 32 Options
    _alpha_figures = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', '?', ',', ':', ' ', "'"]

    # Returns Encoding Array
    def getEncoding(self):
        return self._encoding

    # Returns Alpha_Figures Array
    def getAlphaFigures(self):
        return self._alpha_figures

    def checkCharacters(self, message):
        msg = message.upper()
        i = 0
        k = 0
        error = False
        errorChar = ""

        while i < len(message):
            while k < len(self._alpha_figures):
                if msg[i] == self._alpha_figures[k]:
                    break
                if msg[i] != self._alpha_figures[k] and k == 31:
                    error = True
                    errorChar = msg[i]
                k += 1
            k = 0
            i += 1
        if error:
            print "This character is not supported: " + errorChar
        return error
