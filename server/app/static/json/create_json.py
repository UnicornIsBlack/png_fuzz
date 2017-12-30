import json

data = {
    'gender':'male'
}
name = ['chdr','chai']
data['name'] = name
f = open('data.json','w')
json.dump(data,f,indent=4)

class JSON:

    def __init__(self):
        pass

    def json_by_num(self,start,end):
        i = 0x0000
        image = []
        noimage = []
        while i <= 0x00FF:
            img = '{0:016b}'.format(i)
            if i >= start and i <= end:
                image.append(img)
            else:
                noimage.append(img)
            i += 1
        json_str = {}
        json_str['image'] = image
        json_str['noimage'] = noimage
        print(json.dumps(json_str,indent=4))

if __name__ == '__main__':
    my_json = JSON()
    my_json.json_by_num(1,5)