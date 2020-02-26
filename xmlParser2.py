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
    return tree

def change_elements(tree):
    trueFalse = False

    while trueFalse != True:
        print("To change testsuites, enter: 'TTS'")
        print("To change testsuite, enter 'TT'")
        print("To change testcase, enter 'TC'")
        print("To return to menu, enter 'Menu'")
        option = input("What element would you like to change? ")
        if option == "TTS":
            change_testsuites(tree)
        elif option == "TT":
            change_testsuite(tree)
        elif option == "TC":
            change_testcase(tree)
        elif option == "Menu":
            trueFalse = True
    menu()

def change_testsuites(tree):
    pass

def change_testsuite(tree):
    pass

def change_testcase(tree):
    pass

def save_xml(tree, get_xml):
    yesNo = input("Would you like to save to the original file name? (yes/no): ")
    if yesNo == "yes":
        tree.write(get_xml)
    elif yesNo == "no":
        newFileName = input("Please enter new file name: ") + ".xml"
        tree.write(newFileName)

def displayElements(tree):
    testsuites = tree.getroot()
    print(testsuites.tag, testsuites.attrib) 
    for testsuite in testsuites:
        print(testsuite.tag, testsuite.attrib)
        for testcase in testsuite:
            print(testcase.tag, testcase.attrib)

def menu():
    
    trueFalse = False
    while trueFalse != True:
        print("To read a new file, enter 'Read File'")
        print("To parse current file, enter 'Parse'")
        print("To save your current file, enter 'Save File'")
        print("To enter change file elements, enter 'Change File Elements'")
        print("To display all file elements, enter 'Display Elements'")
        print("To quit the program, enter 'Quit'")
        option = input("Please enter a command: ")
        if option == "Read File":
            get_xml = take_in_file()
        elif option == "Parse":
            tree = parseXML(get_xml)
        elif option == "Save File":
            save_xml(tree, get_xml)
        elif option == "Change File Elements":
            change_elements(tree)
        elif option == "Display Elements":
            displayElements(tree)
        elif option == "Quit":
            confirmation = input("Would you like to save before quitting? (yes/no): ")
            if confirmation == "yes":
                save_xml(tree, get_xml)
                print("File has successfully saved!")
                trueFalse = True
            elif confirmation == "no":
                print("Thank you!")
                trueFalse = True
                   
    
menu()

"""def if __name__ == "__main__":
    pass"""

