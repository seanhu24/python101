import csv

def csv_reader(object):
    """
    read a csv file
    :param object:
    :return:
    """
    reader=csv.reader(object)
    for row in reader:
        print(" ".join(row))


if __name__=="__main__":
    csv_path="TB_data_dictionary_2017-07-09.csv"
    with open(csv_path) as f_obj:
        csv_reader(f_obj)
