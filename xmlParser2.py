""" 
Josh's XML Parser
1/23/2020
"""

import sys
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
    menuLoop = False
    while menuLoop != True:
        print("To change testsuites, enter: 'testsuites'")
        print("To change testsuite, enter 'testsuite'")
        print("To change testcase, enter 'testcase'")
        print("To return to menu, enter 'Menu'")
        element_change = input("What element would you like to change? ")
        if element_change == "testsuites" or element_change =="testsuite" or element_change == "testcase":
            change_tags(tree, element_change)
            return element_change
        elif element_change == "Menu":
            menuLoop = True

def change_tags(tree, element_change):
    menuLoop = False
    while menuLoop != True:
        print(f"To view all {element_change}'s, enter: \'Find All\'")
        print(f"To update all cases of a tag in {element_change}, enter: 'Update Tags'")
        print(f"To add a tag to {element_change}, enter 'Add Tag'")
        print(f"To remove a tag from {element_change}, enter 'Remove Tag'")
        print("To change different element, enter: 'Diff Element'")
        print("To return to home menu, enter: 'Home Menu'")
        option = input("Please enter a command: ")
        if option == "Find All":
            view_all_elements(tree, element_change)
        elif option == "Update Tags":
            update_all_tags(tree, element_change)
        elif option == "Add Tag":
            add_tag_to_elements(tree, element_change)
        elif option == "Remove Tag":
            remove_tag_from_element(tree, element_change)
        elif option == "Diff Element":
            change_elements(tree)
        elif option == "Home Menu":
            menuLoop = True

def update_all_tags(tree, element_change):
    testsuites = tree.getroot()
    tag = input("Which tag do you want to update? ")
    attribute = input("What is the new attribute? ")
    if element_change == "testuites":
        testsuites.find(element_change)
        testsuites.set(tag, attribute)
    elif element_change == "testsuite":
        for testsuite in testsuites:
            testsuite.find(element_change)
            testsuite.set(tag, attribute)
    elif element_change == "testcase":
        for testsuite in testsuites:
            for testcase in testsuite:
                testcase.find(element_change)
                testsuite.set(tag, attribute)
    
    return tree

def view_all_elements(tree, element_change):
    element = tree.getroot()
    if element_change == "testsuites":
        print(element.tag, element.attrib) 
    elif element_change == "testsuite":
        for testsuite in element:
            print(testsuite.tag, testsuite.attrib)
    elif element_change == "testcase":
        for testsuite in element:
            for testcase in testsuite:
                print(testcase.tag, testcase.attrib)


def add_tag_to_elements(tree, element_change):
    testsuites = tree.getroot()
    tag = input("Enter new tag name: ")
    attribute = input("Enter tag attribute ")
    if element_change == "testsuites":
        testsuites.find(element_change)
        testsuites.set(tag, attribute)
    elif element_change == "testsuite":
        for testsuite in testsuites:
            testsuite.find(element_change)
            testsuite.set(tag, attribute)
    elif element_change == "testcase":
        for testsuite in testsuites:
            for testcase in testsuite:
                testcase.find(element_change)
                testsuite.set(tag, attribute)
        
    return tree
    
def remove_tag_from_element(tree, element_change):
    testsuites = tree.getroot()
    tag = input("Which tag do you want to remove? ")
    attribute = input("What is the attribute you want to remove? ")
    if element_change == "testsuites":
        #path = testsuites.find('./[@{0}={1}]'.format(tag, attribute))
        #testsuites.remove(path)
        testsuites.attrib.pop(tag, attribute)
    elif element_change == "testsuite":
        for testsuite in testsuites:
            testsuite.attrib.pop(tag, attribute)
    elif element_change == "testcase":
        for testsuite in testsuites:
            for testcase in testsuite:
                testcase.attrib.pop(tag, attribute)
    
    return tree


def add_elements(tree, element_change):
    tree = tree.getroot()
    update_tag = input("Which tag do you want to update? ")
    new_tag = input("What will the tag display? ")
    if element_change == "testsuites":
        tag = ET.SubElement(tree, element_change)
        tag.set(update_tag, new_tag)
        return tree

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
    menuLoop = False
    while menuLoop != True:
        print("To enter a file, enter 'Enter File'")
        print("To read the current file, enter 'Read File'")
        print("To save your current file, enter 'Save File'")
        print("To enter modify file, enter 'Modify File'")
        print("To display file, enter 'Display File'")
        print("To quit the program, enter 'Quit'")
        option = input("Please enter a command: ")
        if option == "Enter File":
            get_xml = take_in_file()
        elif option == "Read File":
            tree = parseXML(get_xml)
        elif option == "Save File":
            save_xml(tree, get_xml)
        elif option == "Modify File":
            change_elements(tree)
        elif option == "Display File":
            displayElements(tree)
        elif option == "Quit":
            confirmation = input("Would you like to save before quitting? (yes/no): ")
            if confirmation == "yes":
                save_xml(tree, get_xml)
                print("File has successfully saved!")
                menuLoop = True
            elif confirmation == "no":
                print("Thank you!")
                menuLoop = True
                   
    
def main():
    menu()
    
if __name__ == "__main__":
    main()

