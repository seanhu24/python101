import csv

def csv_dict_reader(file_obj):
    """
    read a csv file as dict
    :param file_obj:
    :return:
    """
    reader=csv.DictReader(file_obj, delimiter=",")
    for line in reader:
        print(line['first_name'],line['last_name'])

if __name__=="__main__":
    with open('data.csv') as csv_f:
        csv_dict_reader(csv_f)