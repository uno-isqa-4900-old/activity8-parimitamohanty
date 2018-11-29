import csv


class Customer:

    def __init__(self, cust_id, cust_firstName, cust_lastName, company, address, city, state, zip):
        self.cust_id = cust_id
        self.cust_firstName = cust_firstName
        self.cust_lastName = cust_lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def Address(self):
        print("",self.cust_firstName, self.cust_lastName)
        if self.company !='':
             print("", self.company)
        print("", self.address)
        print("", self.city, self.state, self.zip)
        print("\n")


def display_title():
    print("Customer Viewer")

    

def main():
    display_title()

    while True:
        cust_id = str(input("Enter the customer ID: "))
        if 100 < int(cust_id) < 601:
            with open('customers.csv', 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)

                for row in csv_reader:

                    i = str(row[0])

                    if i == cust_id:
                        print("\n")
                        cust1 = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                        cust1.Address()
            choice = input("Continue? (y/n): ")
            if choice != "y":
                print("Bye!")
                break

        else:
            print("\n No customer with that ID \n")
            choice = input("Continue? (y/n): ")
            if choice != "y":
                print("Bye!")
                break

if __name__ == '__main__':
    main()




