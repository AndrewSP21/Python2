def txt_creator(guide):
    with open('guide.txt', 'w') as file:
        for line in guide:
            for key, word in line.items():
                file.write(f'{word} \n\n')


def csv_creator(guide):
    with open('guide.csv', 'w') as file:
        t = ''
        for line in guide:
            for key, word in line.items():
                if key == 'post':
                    t += word + '\n'
                else:
                    t += word + ','
            file.write(f'{t}')
            t = ''


def xml_creator(guide):
    from dicttoxml2 import dicttoxml
    with open('guide.xml', 'w', encoding='utf-8-sig') as file:
        xml = dicttoxml(guide)
        file.write(xml.decode())


def json_creator(guide):
    import json
    with open('guide.json', 'w', encoding='utf-8-sig') as file:
        file.write(json.dumps(guide, ensure_ascii=False))

def txt_reader(file_name):
    with open(file_name, 'r') as file:
        i = 0
        d = {}
        g = []
        for line in file:
            i +=1
            if line !='\n':
                if i == 1:
                    d['surname'] = line.rsplit()[0]
                elif i == 3:
                    d['name'] = line.rsplit()[0]
                elif i == 5:
                    d['patronymic'] = line.rsplit()[0]
                elif i == 7:
                    d['phone'] = line.rsplit()[0]
                elif i == 9:
                    d['post'] = line.rsplit()[0]
            if i == 10:
                i = 0
                g.append(d)
                d = {}
    return g

def csv_reader(file_name):
    with open(file_name, 'r') as file:
        d = {}
        g = []
        for line in file:
            a = line.rsplit(',')
            d['surname'] = a[0]
            d['name'] = a[1]
            d['patronymic'] = a[2]
            d['phone'] = a[3]
            d['post'] = a[4].rsplit()[0]
            g.append(d)
    return g


def json_reader(file_name):
    import json
    with open(file_name, 'r', encoding='utf-8-sig') as file:
        js = json.loads(file.readline())
    return js