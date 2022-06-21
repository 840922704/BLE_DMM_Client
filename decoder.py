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
        #print(tobinary)
        flipped = LSB_TO_MSB(tobinary) #reverse binary

        binary_array.append(flipped)
        fullbinary += flipped
    #print(fullbinary)
    return fullbinary


class type_detecter():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      type_dict = {
            # 1. Multimeter (1):	Aneng 9002	BSIDE ZT-300AB	ZOYI ZT-300AB	BABATools AD900
            '11000000':'1',
            # 2. Small-Multimeter (2):	Aneng V05B	BSIDE ZT-5B ZOYI ZT-5B	
            '01000000':'2',
            # 3. Clamp-Multimeter (3):	Aneng ST207	BSIDE ZT-5BQ	ZOYI ZT-5BQ
            '10000000':'3',
            # 4. Desk-Multimeter (4):	Aneng AN999S		ZOYI ZT-5566S
            '00100000':'4',
      }
      def decode (self, origin_value):
            
            return pre_process(origin_value)

      @classmethod
      def type (self, origin_value):
            type_code = ''
            for i in range (16,24,1):
                  type_code = type_code + self.decode(self, origin_value)[i]
            try:
                  type = self.type_dict[type_code]
            except:
                  type = None
            return type


## 1. Multimeter (1):	Aneng 9002	BSIDE ZT-300AB	ZOYI ZT-300AB	BABATools AD900
class decoder_1 ():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):
            
            return pre_process(origin_value)

      digit_dict = {
            '1110111':'0',
            '0010010':'1',
            '1011101':'2',
            '1011011':'3',
            '0111010':'4',
            '1101011':'5',
            '1101111':'6',
            '1010010':'7',
            '1111111':'8',
            '1111011':'9',
            '1111110':'A',
            '0000111':'u',
            '0101101':'t',
            '0001111':'o',
            '0100101':'L',
            '1101101':'E',
            '1101100':'F',
            '0001000':'-'
      }

      @classmethod
      def digit(self, segment, digi):
            # print(digi)
            signal = segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]
            #print(signal)
            try:
                  if digi != None:
                        digi = digi + self.digit_dict[signal]
            except:
                  digi = digi + ''
            return digi

      @classmethod
      def printdigit (self, prepared):
            digi = ''
            print(prepared)
            print(prepared[16]+prepared[17]+prepared[18]+prepared[19]+prepared[20]+prepared[21]+prepared[22]+prepared[23])
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
                  "F", "μ", "?5", "n", "Hz", "Ω", "K", "M",
                  "V", "m", "DC", "A", "Auto", "?7", "μ", "m",
                  "?8", "?9", "?10", "?11"]
            function = {60,63,64,65,80}
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





## 2. Small-Multimeter (2):	Aneng V05B	BSIDE ZT-5B	ZOYI ZT-5B	
class decoder_2():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):
            
            return pre_process(origin_value)



      digit_dict = {
            '1110111':'0',
            '0010010':'1',
            '1011101':'2',
            '1011011':'3',
            '0111010':'4',
            '1101011':'5',
            '1101111':'6',
            '1010010':'7',
            '1111111':'8',
            '1111011':'9',
            '1111110':'A',
            '0000111':'u',
            '0101101':'t',
            '0001111':'o',
            '0100101':'L',
            '1101101':'E',
            '1101100':'F',
            '0001000':'-'
      }
      
      @classmethod
      def digit(self, segment, digi):
            # print(digi)
            signal = segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]
            #print(signal)
            try:
                  if digi != None:
                        digi = digi + self.digit_dict[signal]
            except:
                  digi = digi + ''
            return digi

      
      @classmethod
      def printdigit (self, prepared):
            digi = ''
            print(prepared)
            print(prepared[16]+prepared[17]+prepared[18]+prepared[19]+prepared[20]+prepared[21]+prepared[22]+prepared[23])
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
            bits_1 = ["HOLD", "Flash", "BUZ"]
            for i in range(25,28,1):
                  if prepared[i]=='1':
                        # print(bits_1[i-25])
                        char_function.append(bits_1[i-25])
            bits_2 = ["n", "V", "DC", "AC","F", "->","A", "µ",
            "Ω", "k", "m", "M","", "Hz", "°F", "°C"]
            function = {64,69}
            for i in range(63+len(bits_2),63,-1):
                  if i in function:
                        if prepared[i]=='1':
                              # print(bits[i-64])
                              char_function.append(bits_2[i-64])

                  else:
                        if prepared[i]=='1':
                              # print(bits[i-64])
                              char_unit.append(bits_2[i-64])
            char = [char_function,char_unit]
            return char



## 3. Clamp-Multimeter (3):	Aneng ST207	BSIDE ZT-5BQ	ZOYI ZT-5BQ
class decoder_3():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):
            
            return pre_process(origin_value)



      digit_dict = {
            '1110111':'0',
            '0010010':'1',
            '1011101':'2',
            '1011011':'3',
            '0111010':'4',
            '1101011':'5',
            '1101111':'6',
            '1010010':'7',
            '1111111':'8',
            '1111011':'9',
            '1111110':'A',
            '0000111':'u',
            '0101101':'t',
            '0001111':'o',
            '0100101':'L',
            '1101101':'E',
            '1101100':'F',
            '0001000':'-'
      }
      
      @classmethod
      def digit(self, segment, digi):
            # print(digi)
            signal = segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]
            #print(signal)
            try:
                  if digi != None:
                        digi = digi + self.digit_dict[signal]
            except:
                  digi = digi + ''
            return digi

      
      @classmethod
      def printdigit (self, prepared):
            digi = ''
            print(prepared)
            print(prepared[16]+prepared[17]+prepared[18]+prepared[19]+prepared[20]+prepared[21]+prepared[22]+prepared[23])
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
            bits_1 = ["HOLD", "Flash", "BUZ"]
            for i in range(25,28,1):
                  if prepared[i]=='1':
                        # print(bits_1[i-25])
                        char_function.append(bits_1[i-25])
            bits_2 = ["n", "V", "DC", "AC", "F", "->", "A", "μ",
                  "Ω", "k", "m", "M", "", "Hz", "°F", "°C",
                  "", "", "", ""]
            function = {65,69}
            for i in range(59+len(bits_2),59,-1):
                  if i in function:
                        if prepared[i]=='1':
                              # print(bits[i-60])
                              char_function.append(bits_2[i-60])

                  else:
                        if prepared[i]=='1':
                              # print(bits[i-60])
                              char_unit.append(bits_2[i-60])
            char = [char_function,char_unit]
            return char



## 4. Clamp-Multimeter (4): image	Aneng AN999S		ZOYI ZT-5566S
class decoder_4():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):
            
            return pre_process(origin_value)



      digit_dict = {
            '1110111':'0',
            '0010010':'1',
            '1011101':'2',
            '1011011':'3',
            '0111010':'4',
            '1101011':'5',
            '1101111':'6',
            '1010010':'7',
            '1111111':'8',
            '1111011':'9',
            '1111110':'A',
            '0000111':'u',
            '0101101':'t',
            '0001111':'o',
            '0100101':'L',
            '1101101':'E',
            '1101100':'F',
            '0001000':'-',
            '1010':'1'
      }
      
      @classmethod
      def digit(self, segment, digi):
            # print(digi)
            signal = segment
            #print(signal)
            try:
                  if digi != None:
                        digi = digi + self.digit_dict[signal]
            except:
                  digi = digi + ''
            return digi

      
      @classmethod
      def printdigit (self, prepared):
            #print(prepared[16]+prepared[17]+prepared[18]+prepared[19]+prepared[20]+prepared[21]+prepared[22]+prepared[23])
            digi = ''
            print(prepared)
            if prepared[95]=='1':
                  #print('-', end="")
                  if digi != None:
                        digi = digi + '-'
            digi = self.digit(prepared[91]+prepared[90]+prepared[89]+prepared[88], digi)
            if prepared[84]=='1':
                  #print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[87]+prepared[86]+prepared[83]+prepared[82]+prepared[85]+prepared[81]+prepared[80], digi)
            if prepared[76]=='1':
                  #print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[79]+prepared[78]+prepared[75]+prepared[74]+prepared[77]+prepared[73]+prepared[72], digi)
            if prepared[68]=='1':
                  #print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            if prepared[92]=='1':
                  #print(':', end="")
                  if digi != None:
                        digi = digi + ':'
            digi = self.digit(prepared[71]+prepared[70]+prepared[67]+prepared[66]+prepared[69]+prepared[65]+prepared[64], digi)
            if prepared[60]=='1':
                  #print('.', end="")
                  if digi != None:
                        digi = digi + '.'
            digi = self.digit(prepared[63]+prepared[62]+prepared[59]+prepared[58]+prepared[61]+prepared[57]+prepared[56], digi)
            if digi == None:
                 digi = '0'
            return digi
      @classmethod
      def printchar (self, prepared):
            # Define a list to storage str
            char_function = []
            char_unit = []
            bits_1 = ["Auto","","Rel","Buzz","->","","Min","Max","Peek","Hold","V","","","μ"]
            for i in range(34,48,1):
                  if i != 44 and i != 47:
                        if prepared[i]=='1':
                              # print(bits_1[i-25])
                              char_function.append(bits_1[i-34])
                  else:
                        if prepared[i]=='1':
                              # print(bits_1[i-25])
                              char_unit.append(bits_1[i-34])

            bits_2 = ["DC", "%", "AC", "M", "k", "Ω", "Hz", "F",
                  "μ", "m", "n", "A"]
            bits_2_num = [97,100,102,124,125,126,127,128,129,130,131,140]
            for i in bits_2_num :
                  if prepared[i]=='1':
                        # print(bits_2.index(i))
                        char_unit.append((bits_2[bits_2_num.index(i)]))
            char = [char_function,char_unit]
            return char

#debug

# type 1 test
#value = "1b8470b1496a9f3c66aa3b"
# type 2 test test
#value = "1b847155a2619ffc662a"
#value = "1b847155482ac9fe22ae"

'''
type = type_detecter.type(value)
if type == '1':
      A = decoder_1.printdigit(decoder_1.decode(value))
      B = decoder_1.printchar(decoder_1.decode(value))
elif type == '2':
      A = decoder_2.printdigit(decoder_2.decode(value))
      B = decoder_2.printchar(decoder_2.decode(value))
elif type == '3':
      A = decoder_3.printdigit(decoder_3.decode(value))
      B = decoder_3.printchar(decoder_3.decode(value))
elif type == '4':
      A = decoder_4.printdigit(decoder_4.decode(value))
      B = decoder_4.printchar(decoder_4.decode(value))

B_function = ' '.join(B[0])
B_unit = ' '.join(B[1])
print("digit:"+str(A))
print("function: "+B_function+"\n"
      +"unit: "+B_unit)
'''

#print(type_detecter.type(value))

