import logging


class decoder ():
      def __init__(self, filename=None, parent=None):
            self.logger = logging.getLogger(__name__)
            self.ADDRESS = ADDRESS
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
            print(digi)
            if segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1110111':
                  print('0', end="")
                  if digi != None:
                        digi = digi + '0'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='0010010':
                  print('1', end="")
                  if digi != None:
                        digi = digi + '1'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1011101':
                  print('2', end="")
                  if digi != None:
                        digi = digi + '2'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1011011':
                  print('3', end="")
                  if digi != None:
                        digi = digi + '3'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='0111010':
                  print('4', end="")
                  if digi != None:
                        digi = digi + '4'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1101011':
                  print('5', end="")
                  if digi != None:
                        digi = digi + '5'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1101111':
                  print('6', end="")
                  if digi != None:
                        digi = digi + '6'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1010010':
                  print('7', end="")
                  if digi != None:
                        digi = digi + '7'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1111111':
                  print('8', end="")
                  if digi != None:
                        digi = digi + '8'
                  return digi
            elif segment[3]+segment[2]+segment[7]+segment[6]+segment[1]+segment[5]+segment[4]=='1111011':
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
            bits = ["HOLD", "degF", "degC", "->", "MAX", "MIN", "%", "AC",
                  "F", "u(F)", "?5", "n(F)", "Hz", "ohm", "K(ohm)", "M(ohm)",
                  "V", "m(V)", "DC", "A", "auto", "?7", "u(A)", "m(A)",
                  "?8", "?9", "?10", "?11"]
            char = ''
            for i in range(60,60+len(bits),1):
                  if prepared[i]=='1':
                        print(bits[i-60])
                        char = char + ' ' + bits[i-60]
            return char





#if __name__ == "__main__":
#    logging.basicConfig(level=logging.INFO)
#    asyncio.run(decoder.main(decoder(),sys.argv[1] if len(sys.argv) == 2 else ADDRESS))
