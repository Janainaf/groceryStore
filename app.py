from calendar import month
from posixpath import split
from models import Base, session, Product, Brands, engine
import datetime
import csv

# ****************************** MENU 1 **************************************

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

            # ****************************** CLEANS DATA  **************************************

def clean_price(price_string):
    split_price= price_string.split('$')
    float_price = float(split_price[1])
    int_price =  int(float_price * 100)
    return int_price

def clean_date(date_str):
    split_date = date_str.split('/')
    year = int(split_date[2])
    day = int(split_date[1])
    month = int(split_date[0])
    final_date = datetime.date(year, month, day)
    return final_date

def clean_quantity(quantity_string):
    quantity_integer = int(quantity_string)
    return quantity_integer



def clean_brand(brand_str):
    brands = ["Einstein's", "Kraft", "Bob's Red Mill", "Delish", "Kroger", "V8", "Campbell's", "Kikkoman", "Del Monte", "Farberware", "Pam", "McCormick","Chateau Bonnet"]
    brand_id = brands.index(brand_str)
    return brand_id


# ****************************** READ CVS FILES **************************************
def add_csv():
    with open('brands.csv') as csvfile:
        data_brands = csv.reader(csvfile)
        next(data_brands)

        for row in data_brands:
            brand_name = row[0]
            new_brand= Brands(brand_name=brand_name)
            session.add(new_brand)
        session.commit()

    with open('inventory.csv') as csvfile:
        data_products = csv.reader(csvfile)
        next(data_products)

        for row in data_products :
            product_in_db = session.query(Product).filter(Product.product_name == row[0]).one_or_none()
            if product_in_db == None:
                product_name = row[0]
                product_price = clean_price(row[1])
                product_quantity = clean_quantity(row[2])
                date_updated = clean_date(row[3])
                brand_id = (clean_brand(row[4])+1)

                new_product = Product(product_name=product_name,
                product_price=product_price, 
                product_quantity=product_quantity, 
                date_updated=date_updated, 
                brand_id=brand_id) 
                session.add(new_product)
        session.commit()

# ****************************** APP FUNCTION   **************************************

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

# ****************************** DUNDER DATA  **************************************



if __name__ == '__main__':
    Base.metadata.create_all(engine)
    # app()
    add_csv()
    
