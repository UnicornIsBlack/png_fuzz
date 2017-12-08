import os
class PngFile:

    def __init__(self):
        self.start = '89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 ' \
           '00 00 00 20 00 00 00 20 02 03 00 00 00 0E 14 92 ' \
           '67 00 00 00 04 67 41 4D 41 00 00 B1 8F 0B FC 61 ' \
           '05 00 00 00 0C 50 4C 54 45 FF FF FF 00 00 00 FF ' \
           '00 00 FF FF 00 31 F4 60 1E 00 00 00 01 62 4B 47 ' \
           '44 00 88 05 1D 48 00 00 00 09 70 48 59 73 00 00 ' \
           '0B 11 00 00 0B 11 01 7F 64 5F 91 00 00 00 91 49 ' \
           '44 41 54 28 CF 55 D0 BB 0D 02 31 0C 80 E1 DF 92 ' \
           '43 9D E2 42 71 D3 E4 24 44 9D 22 A1 60 03 98 82 ' \
           '11 32 C4 71 42 9E 82 D1 28 CE 91 0E 57 9F FC 92 ' \
           '65 38 C6 94 1C 8F 0C 10 6A 33 32 A0 C8 BB 39 B6 ' \
           'AD FF 83 E5 E6 60 2E 8E 10 1D 8C 8D 44 60 02 4A ' \
           '04 2E C1 33 8A BC 88 7B DF 57 6A 20 19 B4 02 52 ' \
           'F6 01 48 AD 2D 00 2C FD D4 15 90 EB 3A F7 02 E8 ' \
           'D9 6C CD 00 B3 D9 0A A0 03 E1 6E '
        self.end = ' 3B 92 42 6D 1F 3E F9 D5 83 F1 00 00 00 00 49 45 4E 44 AE 42 60 82'
        self.fuzz = 'F6 C1 4B'

    def get_hex(self,fuzz):
        png = bytearray.fromhex(self.start)
        png.extend(fuzz)
        png.extend(bytearray.fromhex(self.end))
        return png

    def delete_file(self):
        dir = 'image/'
        for item in os.listdir(dir):
            file = os.path.join(dir,item)
            print(file)
            if os.path.isfile(file):
                try:
                    os.remove(file)
                except OSError as e:
                    print(e)



    def get_png(self,filename,png):
        pngFile = open(filename, 'wb')
        try:
            pngFile.write(png)
        except IOError as e:
            print(e)
        finally:
            if 'pngFile' in locals():
                pngFile.close()

    def int_to_byte(self,num):
        array_num = []
        array_num.append(num >> 16 & 0xFF)
        array_num.append(num >> 8 & 0xFF)
        array_num.append(num & 0xFF)
        return bytearray(array_num)

    def get_filename(self,num):
        filename = 'image/' + '{0:024b}'.format(num)
        return filename

    def run(self):
        i = 0x000000
        num = 0
        while i <= 0xFFFFFF:
            fuzz = self.int_to_byte(num)
            png = self.get_hex(fuzz)
            filename = self.get_filename(num) + '.png'
            self.get_png(filename, png)
            print(filename)
            i += 1
            num += 1
            if num == 1000:
                num = 0
                break
        print('end')


png = PngFile()
png.run()
