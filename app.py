from models import Base, session, Product, Brands, engine
import datetime
import csv


def menu():
    while True:
        print('''
            \nWelcome to My Store Inventory
            \n **** Here are your choices ****
            \nN) Add New Product
            \rV) View a Product by ID
            \rA) Product Analysis
            \rB) Backup the Database
            \rQ) Quit the Application
            ''')
        choice = input('What would you like to do? ')
        if choice in ['N','V', 'A', 'B', 'Q']:
            return choice
        else:
            input('''
            \rPlease choose one of the option above
            \rPress Enter to try again''')

def add_csv():
    with open('brands.csv') as csvfile:
        data_brands = csv.reader(csvfile)
        for row in data_brands:
            print(row)
    with open('inventory.csv') as csvfile:
        data_products = csv.reader(csvfile)
        for row in data_products:
            print(row)

def clean_data():
    print("hello")

def app():
    app_running = True
    while app_running:
        choice = menu()
        if choice == "N":
            product_name = input("What is the name of the product? " )
            product_quantity = input("How many products are available? " )
            product_price = input("How much is the product? " )
            # # for brand in brands
            # #     print(f'{brand})
            brand_id = input('''
            \rPlease select a brand from the following:
            \r1) Einstein's
            \r2) Kraft
            \r3) Bob's Red Mill
            \r4) Delish 
            \rPlease choose the number for the corresponding brand or press X if the brand is not listed -  ''')
            print(f'\n*** {product_name} has been added!***')
            pass
        elif choice == "V":
            product_id = input("Enter a product's ID number. " )
            # View a Product by ID
            pass
        elif choice == "A":
            # Product Analysis
            print(f'\n The most expensive product is: {product_name}.')
            print(f'The price is: {product_price}.')
            print(f'\n The most least product is: {product_name}.')
            print(f'The price is: {product_price}.')
            print(f'\n The most common brand is: {brand_name}.')
            pass
        elif choice == "B":
            # Backup the Database
            print(f'Backing up data ...')
            print(f'\n*** Your database has been backed up!***')
            pass
        else:
            print("Closing app... \nGoodbye :) ")
            app_running = False
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app()
    # add_csv()