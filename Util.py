class UtilityMethods:
    def binaryToDecimal(self, binary):
        result = 0
        for bit in binary:
            result = (result << 1) + int(bit)
        return result