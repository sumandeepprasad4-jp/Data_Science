class PhoneBook:
    #we will store all the contact in side phone_directory
    phone_directory=[]
    def __init__(self, name,phone_number):
        self.name = name
        self.phone_number = phone_number
        PhoneBook.phone_directory.append(self)

    def Show_Contacts(self):
        return (f"Name: {self.name}, Phone Number: {self.phone_number}")
    @classmethod
    def Show_all_Contact(cls):
        if len(cls.phone_directory) == 0:
            print("No contacts found in the phone directory ")
        else:
            print("---------------------------------------------")
            print("All contacts found in the phone directory are")
            print("---------------------------------------------")
            for contact in cls.phone_directory:
                print(contact.Show_Contacts())
    @staticmethod
    def valid_phone_number(phone_number):
        if len(phone_number)>=8 and phone_number.isdigit():
            return True
        return False
    #searching a contact with given name:
    # @classmethod
    # def Search_Contact(cls, serch_name):
    #     for contact in cls.phone_directory:
    #         if contact.name.lower() == serch_name.lower():
    #             print(f"Contact number of {serch_name} is :{contact.phone_number}")
    #     return "No contacts found in the phone directory"

no_contact= int(input("how many contacts do you want to add?:"))
for i in range(no_contact):
    name=input("Enter your name:")
    phone_number=input("Enter your phone number:")
    if PhoneBook.valid_phone_number(phone_number):
        PhoneBook(name,phone_number)
    else:
        print(f"Invalid phone number for {name},phone number should be atleaste 8 digit and should contain numbers")
# serch_name=input("Enter the name whome you want to serch:")

PhoneBook.Show_all_Contact()
# print()
# PhoneBook.Search_Contact(serch_name)
