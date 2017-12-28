import os


class PngFile:

    def __init__(self,fileDir):
        self.start = '89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 00 00 00 ' \
                     '20 00 00 00 20 02 03 00 00 00 0E 14 92 67 00 00 00 04 67 ' \
                     '41 4D 41 00 00 B1 8F 0B FC 61 05 00 00 00 0C 50 4C 54 45 ' \
                     'FF FF FF 00 00 00 FF 00 00 FF FF 00 31 F4 60 1E 00 00 00 ' \
                     '01 62 4B 47 44 00 88 05 1D 48 00 00 00 09 70 48 59 73 00 ' \
                     '00 0B 11 00 00 0B 11 01 7F 64 5F 91 00 00 00 91 49 44 41 ' \
                     '54 28 CF 55 D0 BB 0D 02 31 0C 80 E1 DF 92 43 9D E2 42 71 ' \
                     'D3 E4 24 44 9D 22 A1 60 03 98 82 11 32 C4 71 42 9E 82 D1 ' \
                     '28 CE 91 0E 57 9F FC 92 65 38 C6 94 1C 8F 0C 10 6A 33 32 ' \
                     'A0 C8 BB 39 B6 AD FF 83 E5 E6 60 2E 8E 10 1D 8C 8D 44 60 ' \
                     '02 4A 04 2E C1 33 8A BC 88 78 1F 57 2A 20 19 B4 02 52 D9 ' \
                     '6C CD 00 B3 D9 0A A0 03 E1 6E F6 C1 4B 3B 92 3D 9B DF 92 ' \
                     '65 60 5C 97 15 80 D0 52 39 7C E4 07 42 6D 1F 3E F9 D5 83 ' \
                     'F1 00 00 00 00 49 45 4E 44 AE 42 '

        self.start332 = '89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52 00 00 00 20 00 00 00 20 ' \
                      '04 03 00 00 00 81 54 67 C7 00 00 00 12 50 4C 54 45 FF FF FF FF FF FF FF ' \
                      'FF FF 00 00 00 FF 00 00 FF FF 00 7E B4 1A 6F 00 00 00 01 74 52 4E 53 00 ' \
                      '40 E6 D8 66 00 00 00 01 62 4B 47 44 00 88 05 1D 48 00 00 00 9F 49 44 41 ' \
                      '54 28 CF 7D D1 C1 11 C3 20 0C 44 D1 4C 4A 48 05 C9 DF 0E B4 54 60 54 41 ' \
                      'FA 2F 26 07 B0 6C 38 84 13 F3 66 A5 41 E2 F1 E6 F5 FC 70 9D C7 79 51 C8 ' \
                      '0B B4 1E 95 B0 C3 CE 84 98 10 80 D2 F6 0A 2D 5B FF 07 84 BC 02 28 BD 02 ' \
                      'D6 06 C8 B7 87 01 CC 84 66 C2 27 44 E0 25 31 DE 71 DC 4A 0C F0 05 39 46 ' \
                      'E2 6C 12 05 9E 1B A9 7D C8 B6 1D 2A 08 75 68 1D AA 47 CB 50 76 6A 16 B5 ' \
                      'CC CC 8C A8 1E 39 80 4A 6C 60 0F 38 D8 4A 6E E0 CC 96 BE 3E 4A 63 42 ED ' \
                      'C0 0E D7 2C D8 D6 68 B1 EE 54 E0 07 EC 70 50 42 91 F9 97 7A 00 00 00 09 ' \
                      '49 44 41 54 00 00 0B 12 00 00 0B 12 42 01 5A F9 B7 00 00 00 09 49 44 41 ' \
                      '54 00 00 0B 12 00 00 0B 12 42 01 5A F9 B7 00 00 00 09 49 44 41 54 00 00 ' \
                      '0B 12 00 00 0B 12 01 EE 8F E9 9D 00 00 00 01 49 44 41 54 01'
        self.end = ''
        self.fuzz = '60 82'
        self.fileDir = fileDir
        self.rDir = '../static/image/'
        dir = self.rDir + '259/'
        self.delete_file(dir)
        self.mkdir()

    def get_hex(self,fuzz):
        png = bytearray.fromhex(self.start)
        png.extend(fuzz)
        png.extend(bytearray.fromhex(self.end))
        return png

    def delete_file(self,file):
        if os.path.isfile(file):
            os.remove(file)
        elif os.path.isdir(file):
            for item in os.listdir(file):
                src = os.path.join(file,item)
                self.delete_file(src)


    def mkdir(self):
        dir = self.rDir + self.fileDir + '/'

        if not os.path.exists(dir):
            os.makedirs(dir)

        i = 1
        while i <= 14:
            exDir = dir + str(i) + '/'
            if not os.path.exists(exDir):
                os.makedirs(exDir)
            i += 1


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
        array_num.append(num >> 8 & 0xFF)
        array_num.append(num & 0xFF)
        return bytearray(array_num)

    def get_filename(self,num, exDir):
        filename = self.rDir + self.fileDir + '/' + exDir + '/{0:024b}'.format(num)
        return filename

    def run(self):
        i = 0x0000
        num = 0
        e = 1
        exDir = '1'
        while i <= 0xFFFF:
            fuzz = self.int_to_byte(i)
            png = self.get_hex(fuzz)
            filename = self.get_filename(i,exDir) + '.png'
            self.get_png(filename, png)
            print(filename)
            i += 1
            num += 1
            if num == 5000:
                num = 0
                e += 1
                exDir = str(e)

        print('end')


if __name__ == '__main__':
    png = PngFile('259')
    png.run()