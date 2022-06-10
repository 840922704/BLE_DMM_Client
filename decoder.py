import logging

## 11 Byte DMM
class decoder_11 ():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):

            a = int(origin_value, 16)
            b = 0x41217355a2c1327166aa3b

            #print((a ^ b).decode("utf-8"))
            result = bin(a ^ b)[0:1]+bin(a ^ b)[2:]

            prepared = ''

            for i in range(0,87,8):
                  tmp = result[i:(i+8)]
                  for j in range(8,0,-1):
                        prepared = prepared+tmp[(j-1):j]
            return prepared


      @classmethod
      def digit(self, segment, digi):
            # print(digi)
            signal = segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]
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
            char = []
            # bits_1 = ["∆", "BlueTooth", "BUZ"]
            # Ignore BlueTooth
            bits_1 = ["∆", "", "BUZ"]
            for i in range(25,28,1):
                  if prepared[i]=='1':
                        # print(bits_1[i-25])
                        char.append(bits_1[i-25])
            bits_2 = ["HOLD", "°F", "°C", "->", "MAX", "MIN", "%", "AC",
                  "F", "u(F)", "?5", "n(F)", "Hz", "Ω", "K(Ω)", "M(Ω)",
                  "V", "m(V)", "DC", "A", "auto", "?7", "u(A)", "m(A)",
                  "?8", "?9", "?10", "?11"]
            for i in range(60,60+len(bits_2),1):
                  if prepared[i]=='1':
                        # print(bits[i-60])
                        char.append(bits_2[i-60])
            return char

## 10 Byte DMM
class decoder_10 ():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)

      @classmethod
      def decode (self, origin_value):

            a = int(origin_value, 16)
            b = 0x41217355a2c1327166aa

            #print((a ^ b).decode("utf-8"))
            result = bin(a ^ b)[0:1]+bin(a ^ b)[2:]

            prepared = ''

            for i in range(0,87,8):
                  tmp = result[i:(i+8)]
                  for j in range(8,0,-1):
                        prepared = prepared+tmp[(j-1):j]
            return prepared


      @classmethod
      def digit(self, segment, digi):
            print(digi)
            signal = segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]
            if signal=='1110111':
                  print('0', end="")
                  if digi != None:
                        digi = digi + '0'
                  return digi
            elif signal=='0010010':
                  print('1', end="")
                  if digi != None:
                        digi = digi + '1'
                  return digi
            elif signal=='1011101':
                  print('2', end="")
                  if digi != None:
                        digi = digi + '2'
                  return digi
            elif signal=='1011011':
                  print('3', end="")
                  if digi != None:
                        digi = digi + '3'
                  return digi
            elif signal=='0111010':
                  print('4', end="")
                  if digi != None:
                        digi = digi + '4'
                  return digi
            elif signal=='1101011':
                  print('5', end="")
                  if digi != None:
                        digi = digi + '5'
                  return digi
            elif signal=='1101111':
                  print('6', end="")
                  if digi != None:
                        digi = digi + '6'
                  return digi
            elif signal=='1010010':
                  print('7', end="")
                  if digi != None:
                        digi = digi + '7'
                  return digi
            elif signal=='1111111':
                  print('8', end="")
                  if digi != None:
                        digi = digi + '8'
                  return digi
            elif signal=='1111011':
                  print('9', end="")
                  if digi != None:
                        digi = digi + '9'
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
            char = []
            bits_1 = ["HOLD", "Flash", "BUZ"]
            for i in range(25,28,1):
                  if prepared[i]=='1':
                        # print(bits_1[i-25])
                        char.append(bits_1[i-25])
            bits_2 = ["?1", "?2", "?3", "?4", "nano", "V", "DC", "AC",
                  "F", "->", "A", "µ(F)", "Ω", "kilo", "milli", "M(Ω)",
                  "?5", "Hz", "°F", "°C"]
            for i in range(60,60+len(bits_2),1):
                  if prepared[i]=='1':
                        # print(bits[i-60])
                        char.append(bits_2[i-60])
            return char
