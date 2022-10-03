def txt_csv(file_name='guide.txt'):
    import export_import as ei
    ei.csv_creator(ei.txt_reader(file_name))


def csv_txt(file_name='guide.csv'):
    import export_import as ei
    ei.txt_creator(ei.csv_reader(file_name))


def txt_xml(file_name='guide.txt'):
    import export_import as ei
    ei.xml_creator(ei.txt_reader(file_name))


def txt_json(file_name='guide.txt'):
    import export_import as ei
    ei.json_creator(ei.txt_reader(file_name))


def csv_xml(file_name='guide.csv'):
    import export_import as ei
    ei.xml_creator(ei.csv_reader(file_name))


def csv_json(file_name='guide.csv'):
    import export_import as ei
    ei.json_creator(ei.csv_reader(file_name))


def json_xml(file_name='guide.json'):
    import export_import as ei
    ei.xml_creator(ei.json_reader(file_name))


def json_txt(file_name='guide.json'):
    import export_import as ei
    ei.txt_creator(ei.json_reader(file_name))


def json_csv(file_name='guide.json'):
    import export_import as ei
    ei.csv_creator(ei.json_reader(file_name))


def process(item, file_name):
    import Convertor as co

    if item == 1:
        co.txt_csv(file_name)
    elif item == 2:
        co.csv_txt(file_name)
    elif item == 3:
        co.txt_xml(file_name)
    elif item == 4:
        co.txt_json(file_name)
    elif item == 5:
        co.csv_xml(file_name)
    elif item == 6:
        co.csv_json(file_name)
    elif item == 7:
        co.json_xml(file_name)
    elif item == 8:
        co.json_txt(file_name)
    elif item == 9:
        co.json_csv(file_name)
