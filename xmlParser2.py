""" 
Josh's XML Parser
1/23/2020

"""

import xml.etree.ElementTree as ET


def take_in_file():
    # get_xml = input("Please copy and paste the xml file and input here: ")
    pass

def parseXML():
    # xml = input("Please copy and paste the xml file and input here: ")
    xml = "C:\\Users\\joshua.frerichs\\Desktop\\PASSED_ESYNT19014_83_276_2020_1_8_18_28.xml"
    tree = ET.parse(xml)
    # this is the root
    testsuites = tree.getroot()
    # this is the child.
    print(testsuites.tag, testsuites.attrib) 
    for testsuite in testsuites:
        print(testsuite.tag, testsuite.attrib)
        # this is the child of the child
        for testcase in testsuite:
            print(testcase.tag, testcase.attrib)
            
parseXML()

def change_testsuites():
    """ find = input("What do you want to remove in testsuites? ")
        for testsuite in testsuites.findall(find)
        #testsuites.remove(testsuite) """
    """ tag = input("What is the name of your new tag? ")
    #tagText = input("What do you want the tag to say? ") """
    pass

def change_testsuite():
    pass

def change_testcase():
    pass

def save_xml():
    """ yesNo = input("Would you like to save to the original file? (yes/no)")
    if yesNo == "yes":
        tree.write(get_xml)
    else:
        newFileName = input("Please enter new file name: ") + ".xml"
        tree.write(newFileName) """
    pass

def menu():
    pass

def if __name__ == "__main__":
    pass



