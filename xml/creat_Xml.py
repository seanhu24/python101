import xml.etree.ElementTree as xml

def createXML(filename):
    root=xml.Element("zAppointments")
    appt=xml.Element("appointment")
    root.append(appt)

    begin = xml.SubElement(appt, "begin")
    begin.text = "1181251680"

    state = xml.SubElement(appt, "state")

    tree=xml.ElementTree(root)

    with open(filename,'wb') as fh:
        tree.write(fh)

if __name__ == '__main__':
    createXML('appt1.xml')