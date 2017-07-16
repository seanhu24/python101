import time
import xml.etree.cElementTree as ET

def editXML(filename):
    tree=ET.ElementTree(file=filename)
    root=tree.getroot()

    for begin_time in root.iter("begin"):
        begin_time.text=time.ctime(int(begin_time.text))

    tree=ET.ElementTree(root)
    with open("appt2_new.xml",'wb') as f:
        tree.write(f)

if __name__ == '__main__':
    editXML("appt2.xml")

