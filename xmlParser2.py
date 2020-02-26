""" 
Josh's XML Parser
1/23/2020
"""

import xml.etree.ElementTree as ET

def take_in_file():
    # Here is a sample file: 
    # C:\\Users\\joshua.frerichs\\Desktop\\PASSED_ESYNT19014_83_276_2020_1_8_18_28.xml
    get_xml = input("Please copy and paste the xml file and input here: ")
    return get_xml

def parseXML(get_xml):
    tree = ET.parse(get_xml)
    return tree

def change_elements(tree):
    trueFalse = False
    while trueFalse != True:
        print("To change testsuites, enter: 'testsuites'")
        print("To change testsuite, enter 'testsuite'")
        print(f"To change testcase, enter 'testcase'")
        print("To return to menu, enter 'Menu'")
        element_change = input("What element would you like to change? ")
        if element_change == "testsuites" or element_change =="testsuite" or element_change == "testcase":
            change_tags(tree, element_change)
            return element_change
        elif element_change == "Menu":
            trueFalse = True
    menu()

def change_tags(tree, element_change):
    trueFalse = False
    while trueFalse != True:
        print(f"To find all cases of a tag in {element_change}, enter: 'Find All'")
        print(f"To add a tag to {element_change}, enter 'Add Tag'")
        print(f"To remove a tag from {element_change}, enter 'Remove Tag'")
        print("To change different element, enter: 'Diff Element'")
        print("To return to home menu, enter: 'Home Menu'")
        option = input("Please enter a command: ")
        if option == "Find All":
            pass
        elif option == "Add Tag":
            pass
        elif option == "Remove Tag":
            pass
        elif option == "Diff Element":
            change_elements(tree)
        elif option == "Home Menu":
            menu()

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
        print("To enter a file, enter 'New File'")
        print("To read the current file, enter 'Read File'")
        print("To save your current file, enter 'Save File'")
        print("To enter change file elements, enter 'Change File Elements'")
        print("To display all file elements, enter 'Display Elements'")
        print("To quit the program, enter 'Quit'")
        option = input("Please enter a command: ")
        if option == "New File":
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

