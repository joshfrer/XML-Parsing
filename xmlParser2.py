""" 
Josh's XML Parser
1/23/2020

"""

import xml.etree.ElementTree as ET

def take_in_file():
    get_xml = input("Please copy and paste the xml file and input here: ")
    return get_xml

def parseXML(get_xml):
    #xml = "C:\\Users\\joshua.frerichs\\Desktop\\PASSED_ESYNT19014_83_276_2020_1_8_18_28.xml"
    tree = ET.parse(get_xml)
    # this is the root
    testsuites = tree.getroot()
    # this is the child.
    print(testsuites.tag, testsuites.attrib) 
    for testsuite in testsuites:
        print(testsuite.tag, testsuite.attrib)
        # this is the child of the child
        for testcase in testsuite:
            print(testcase.tag, testcase.attrib)


    return tree

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

def save_xml(tree, get_xml):
    yesNo = input("Would you like to save to the original file name? (yes/no): ")
    if yesNo == "yes":
        tree.write(get_xml)
    elif yesNo == "no":
        newFileName = input("Please enter new file name: ") + ".xml"
        tree.write(newFileName)


def menu():
    
    trueFalse = False
    print("To read a new file enter 'Read File'")
    print("To parse current file enter 'Parse'")
    print("To save your current file enter 'Save File'")
    print("To quit the program enter 'Quit'")
    while trueFalse != True:
        option = input("Please enter a command: ")
        if option == "Read File":
            get_xml = take_in_file()
        elif option == "Parse":
            tree = parseXML(get_xml)
        elif option == "Save File":
            save_xml(tree, get_xml)
        elif option == "Quit":
            confirmation = input("Would you like to save before quitting? (yes/no): ")
            if confirmation == "yes" and "Yes" and "y":
                save_xml(tree, get_xml)
                print("File has successfully saved!")
                trueFalse = True
            elif confirmation == "no" and "No" and "n":
                print("Thank you!")
                trueFalse = True
                   
    
menu()

"""def if __name__ == "__main__":
    pass"""

