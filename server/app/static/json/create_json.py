import json,os


class JSON:

    def __init__(self,dir):
        self.dir = dir
        if not os.path.exists(dir):
            os.makedirs(dir)

    def json_by_num(self,start,end):
        i = 0x0000
        image = []
        noimage = []
        while i <= 0xFFFF:
            img = '{0:016b}'.format(i)
            if i >= start and i <= end:
                noimage.append(img)
            else:
                image.append(img)
            i += 1
        json_str = {}
        json_str['image'] = image
        json_str['noimage'] = noimage
        filename = self.dir + '/data.json'
        f = open(filename, 'w')
        json.dump(json_str, f, indent=4)
        print(json.dumps(json_str,indent=4))

    def json_by_file(self):
        dir = './noimage/'
        image = []
        noimage = []
        json_str = {}
        for item in os.listdir(dir):
            img,postfix = item.split('.',1)
            noimage.append(img)
        i = 0x0000
        while i <= 0xFFFF:
            img1 = '{0:016b}'.format(i)
            if img1 not in noimage:
                image.append(img1)
            i += 1
        json_str['image'] = image
        json_str['noimage'] = noimage
        filename = self.dir + '/data.json'
        f = open(filename, 'w')
        json.dump(json_str, f, indent=4)
        print(json.dumps(json_str,indent=4))

if __name__ == '__main__':
    my_json = JSON('./data/238')
    #my_json.json_by_num(0x0000,0xFFFF)
    my_json.json_by_file()