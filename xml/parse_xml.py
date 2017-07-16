import xml.etree.cElementTree as ET

def parseXML(filename):
    tree=ET.ElementTree(file=filename)
    root=tree.getroot()
    print(root)
    print("tag=%s, attrib=%s" %(root.tag,root.attrib))

    for child in root:
        print(child.tag, child.attrib)
        if child.tag=='appointment':
            for step_child in child:
                print(step_child.tag)

    print("-" * 40)
    iter_=tree.iter()
    for elem in iter_:
        print(elem.tag)

    print("-" * 40)
    appointments=root.getchildren()
    for appointment in appointments:
        appt_children=appointment.getchildren()
        for appt_child in appt_children:
            print("%s=%s" %(appt_child.tag, appt_child.text))


if __name__ == '__main__':
    parseXML("appt.xml")