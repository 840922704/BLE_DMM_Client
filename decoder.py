import logging


def pre_process(value):
    
    hex_data = []
    for i in range(0,len(value),2):
        hex_data.append(int("0x"+value[i]+value[i+1], base=16))

    def hex_to_binary(x):
        #return bin(int(x, base=16)).lstrip('0b').zfill(8)
        return bin(int(x, 16)).lstrip('0b').zfill(8)

    def LSB_TO_MSB(x):
        return x[::-1]

    xorkey = [0x41,0x21,0x73,0x55,0xa2,0xc1,0x32,0x71,0x66,0xaa,0x3b,0xd0,0xe2,0xa8,0x33,0x14,0x20,0x21,0xaa,0xbb]
    binary_array = []
    fullbinary = ""
    for x in range(len(hex_data)):
        #tohex = hex(hex_data[x]) #in case data its already XOR decoded
        tohex = hex(hex_data[x] ^ xorkey[x]) #Bytewyse XOR operation
 
        tobinary = hex_to_binary(tohex) #convert to binary
        print(tobinary)
        flipped = LSB_TO_MSB(tobinary) #reverse binary

        binary_array.append(flipped)
        fullbinary += flipped
    #print(fullbinary)
    return fullbinary



## 11 Byte DMM
class decoder_11 ():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):
            
            return pre_process(origin_value)


      @classmethod
      def digit(self, segment, digi):
            # print(digi)
            signal = segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]
            #print(signal)
            if signal=='1110111':
                  # print('0', end="")
                  if digi != None:
                        digi = digi + '0'
                  return digi
            elif signal=='0010010':
                  # print('1', end="")
                  if digi != None:
                        digi = digi + '1'
                  return digi
            elif signal=='1011101':
                  # print('2', end="")
                  if digi != None:
                        digi = digi + '2'
                  return digi
            elif signal=='1011011':
                  # print('3', end="")
                  if digi != None:
                        digi = digi + '3'
                  return digi
            elif signal=='0111010':
                  # print('4', end="")
                  if digi != None:
                        digi = digi + '4'
                  return digi
            elif signal=='1101011':
                  # print('5', end="")
                  if digi != None:
                        digi = digi + '5'
                  return digi
            elif signal=='1101111':
                  print('6', end="")
                  if digi != None:
                        digi = digi + '6'
                  return digi
            elif signal=='1010010':
                  # print('7', end="")
                  if digi != None:
                        digi = digi + '7'
                  return digi
            elif signal=='1111111':
                  # print('8', end="")
                  if digi != None:
                        digi = digi + '8'
                  return digi
            elif signal=='1111011':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + '9'
            elif signal=='1111110':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'A'
            elif signal=='0000111':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'u'
            elif signal=='0101101':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 't'
            elif signal=='0001111':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'o'
            elif signal=='0100101':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'L'
            elif signal=='1101101':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'E'
            elif signal=='1101100':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'F'
            elif signal=='0001000':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + '-'
            return digi
      @classmethod
      def printdigit (self, prepared):
            digi = ''
            print(prepared)
            if prepared[28]=='1':
                  # print('-', end="")
                  if digi != None:
                        digi = digi + '-'
            digi = self.digit(prepared[28:36], digi)
            if prepared[36]=='1':
                  # print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[36:44], digi)
            if prepared[44]=='1':
                  # print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[44:52], digi)
            if prepared[52]=='1':
                  # print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[52:60], digi)
            if digi == None:
                 digi = '0'
            return digi
      @classmethod
      def printchar (self, prepared):
            # Define a list to storage str
            char_function = []
            char_unit = []
            # bits_1 = ["∆", "BlueTooth", "BUZ"]
            # Ignore BlueTooth
            bits_1 = ["∆", "", "BUZ"]
            for i in range(25,28,1):
                  if prepared[i]=='1':
                        # print(bits_1[i-25])
                        char_function.append(bits_1[i-25])
            '''
            bits_2 = ["HOLD", "°F", "°C", "->", "MAX", "MIN", "%", "AC",
                  "F", "u(F)", "?5", "n(F)", "Hz", "Ω", "K(Ω)", "M(Ω)",
                  "V", "m(V)", "DC", "A", "Auto", "?7", "u(A)", "m(A)",
                  "?8", "?9", "?10", "?11"]
            '''
            bits_2 = ["HOLD", "°F", "°C", "->", "MAX", "MIN", "%", "AC",
                  "F", "u", "?5", "n", "Hz", "Ω", "K", "M",
                  "V", "m", "DC", "A", "Auto", "?7", "u", "m",
                  "?8", "?9", "?10", "?11"]
            function = {60,63,64,65,67,80}
            #for i in range(60,60+len(bits_2),1):
            # reverse to better unit display
            for i in range(59+len(bits_2),59,-1):
                  if i in function:
                        # char of function
                        if prepared[i]=='1':
                              char_function.append(bits_2[i-60])
                  else:
                        # char of unit
                        if prepared[i]=='1':
                              # print(bits[i-60])
                              char_unit.append(bits_2[i-60])
            char = [char_function,char_unit]

            return char





## 10 Byte DMM
class decoder_10 ():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):
            
            return pre_process(origin_value)



      @classmethod
      def digit(self, segment, digi):
            # print(digi)
            signal = segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]
            #print(signal)
            if signal=='1110111':
                  # print('0', end="")
                  if digi != None:
                        digi = digi + '0'
                  return digi
            elif signal=='0010010':
                  # print('1', end="")
                  if digi != None:
                        digi = digi + '1'
                  return digi
            elif signal=='1011101':
                  # print('2', end="")
                  if digi != None:
                        digi = digi + '2'
                  return digi
            elif signal=='1011011':
                  # print('3', end="")
                  if digi != None:
                        digi = digi + '3'
                  return digi
            elif signal=='0111010':
                  # print('4', end="")
                  if digi != None:
                        digi = digi + '4'
                  return digi
            elif signal=='1101011':
                  # print('5', end="")
                  if digi != None:
                        digi = digi + '5'
                  return digi
            elif signal=='1101111':
                  print('6', end="")
                  if digi != None:
                        digi = digi + '6'
                  return digi
            elif signal=='1010010':
                  # print('7', end="")
                  if digi != None:
                        digi = digi + '7'
                  return digi
            elif signal=='1111111':
                  # print('8', end="")
                  if digi != None:
                        digi = digi + '8'
                  return digi
            elif signal=='1111011':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + '9'
            elif signal=='1111110':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'A'
            elif signal=='0000111':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'u'
            elif signal=='0101101':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 't'
            elif signal=='0001111':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'o'
            elif signal=='0100101':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'L'
            elif signal=='1101101':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'E'
            elif signal=='1101100':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + 'F'
            elif signal=='0001000':
                  # print('9', end="")
                  if digi != None:
                        digi = digi + '-'
            return digi
      @classmethod
      def printdigit (self, prepared):
            digi = ''
            print(prepared)
            if prepared[28]=='1':
                  print('-', end="")
                  if digi != None:
                        digi = digi + '-'
            digi = self.digit(prepared[28:36], digi)
            if prepared[36]=='1':
                  print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[36:44], digi)
            if prepared[44]=='1':
                  print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[44:52], digi)
            if prepared[52]=='1':
                  print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[52:60], digi)
            if digi == None:
                 digi = '0'
            return digi
      @classmethod
      def printchar (self, prepared):
            # Define a list to storage str
            char_function = []
            char_unit = []
            bits_1 = ["HOLD", "Flash", "BUZ"]
            for i in range(25,28,1):
                  if i == 26:
                        if prepared[i]=='0':
                              # print(bits_1[i-25])
                              char_function.append(bits_1[i-25])
                  else:
                        if prepared[i]=='1':
                              # print(bits_1[i-25])
                              char_function.append(bits_1[i-25])
            bits_2 = ["", "", "", "", "nano", "V", "DC", "AC",
                  "F", "->", "A", "µ(F)", "Ω", "kilo", "milli", "M(Ω)",
                  "", "Hz", "°F", "°C"]
            function = {64,69}
            for i in range(60,60+len(bits_2),1):
                  if i in function:
                        if i == 79 or i == 62:
                              if prepared[i]=='0':
                                    
                                    # print(bits[i-60])
                                    char_function.append(bits_2[i-60])
                        else:
                              if prepared[i]=='1':
                                    # print(bits[i-60])
                                    char_function.append(bits_2[i-60])
                  else:
                        if i == 79 or i == 62:
                              if prepared[i]=='0':
                                    # print(bits[i-60])
                                    char_unit.append(bits_2[i-60])
                        else:
                              if prepared[i]=='1':
                                    # print(bits[i-60])
                                    char_unit.append(bits_2[i-60])
            char = [char_function,char_unit]
            return char


#debug
'''
value = str("1b8470b1496a9f3c66aa")
A = decoder_10.printdigit(decoder_10.decode(value))
B = decoder_10.printchar(decoder_10.decode(value))
'''

'''
value = "1b8470b1496a9f3c66aa3b"
A = decoder_11.printdigit(decoder_11.decode(value))
B = decoder_11.printchar(decoder_11.decode(value))

B_function = ' '.join(B[0])
B_unit = ' '.join(B[1])
print(A)
print(B_function+B_unit)
'''
