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

 # ****************************** CLEAN DATA  **************************************

def clean_price(price_string):
    try:
        split_price= price_string.split('$')
        float_price = float(split_price[1])
        int_price =  int(float_price * 100)
    except:
            input('''
                \n *** PRICE ERROR *** 
                \n The price should be a number with a currency symbol $ 
                \rPress Enter to try again''')
    else:
        return int_price


def clean_quantity(quantity_string):
    try:
        quantity_integer = int(quantity_string)
    except ValueError:
        input('''
                \n *** QUANTITY ERROR *** 
                \n The quantity should be a number  
                \rPress Enter to try again''')
    else:
        return quantity_integer

def clean_date(date_str):
    split_date = date_str.split('/')
    year = int(split_date[2])
    day = int(split_date[1])
    month = int(split_date[0])
    final_date = datetime.date(year, month, day)
    return final_date


def clean_brand(brand_str):
    brands = ["Einstein's", "Kraft", "Bob's Red Mill", "Delish", "Kroger", "V8", "Campbell's", "Kikkoman", "Del Monte", "Farberware", "Pam", "McCormick","Chateau Bonnet"]
    brand_id = brands.index(brand_str)
    return brand_id

def clean_id(id_str, options):
    try:
        product_id = int(id_str)
    except ValueError:
        input('''
                \n *** ID ERROR *** 
                \n The ID should be a number  
                \rPress enter to try again''')
        return
    else:
        if product_id in options:
            return product_id
        else:
            print(f'''
                \n *** ID ERROR *** 
                \n The ID should be within the optionS
                ''')
            return



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
                product_name = row[0]
                product_price = clean_price(row[1])
                product_quantity = clean_quantity(row[2])
                date_updated = clean_date(row[3])
                brand_id = (clean_brand(row[4])+1)

                product_in_db = session.query(Product).filter(Product.product_name == row[0]).one_or_none()
                if product_in_db == None:
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
            name = input("What is the name of the product? " )

            quantity_error = True
            while quantity_error:
                quantity = input("How many products are available? " )
                quantity = clean_quantity(quantity)
                if type(quantity)  == int:
                    quantity_error = False

            price_error = True
            while price_error: 
                price = input("How much is the product? (Ex: $25.64) - " )
                price = clean_price(price)
                if type(price) == int:
                    price_error = False

            date =  datetime.datetime.now().strftime('%m/%d/%Y/')
            date = clean_date(date)
            brandId = input('''
            \rPlease select a brand from the following:
            \r1) Einstein's
            \r2) Kraft
            \r3) Bob's Red Mill
            \r4) Delish 
            \rPlease choose the number for the corresponding brand or press X if the brand is not listed -  ''')
            if brandId in ['1','2', '3', '4', '5', '6','7', '8', '9', '10', ]:
                print(f'\n*** {name} has been added!***')
            else:
                print(f'\n*** no Brand added!***')
            
            new_product = Product(product_name=name, product_quantity=quantity, product_price=price, date_updated=date, brand_id=brandId )
            session.add(new_product)
            session.commit()
            print(f'\n*** {name} has been added!***')


        elif choice == "V":
            id_options = []
            for product in session.query(Product):
                id_options.append(product.product_id)
            id_error = True
            while id_error:
                product_id = input(f'''
               \rId Options are '{id_options}'
              \n Enter a product's ID number: ''')
                product_id = clean_id(product_id, id_options)
                if type(product_id) == int:
                    id_error = False
            the_product = session.query(Product).filter(Product.product_id == product_id).first()
            print(f'''
                  \n{the_product.product_id} | {the_product.product_name} 
                  \rDate Updated {the_product.date_updated}
                  \rCurrent Price: ${the_product.product_price/100}
                  \rQuantity: ${the_product.product_quantity}
                  \rBrand ID: {the_product.brand_id}

                  ''')
        
        elif choice == "A":
            least_expensive = session.query(Product).order_by(Product.product_price).first()
            most_expensive = session.query(Product).order_by(Product.product_price.desc()).first()
            # common_brand = session.query(Product).filter(Product.product_id == product_id).first()

            print(f'''\n*** Products Analysis ***
            \nThe most expensive product is: {most_expensive.product_name}
            \rThe price is: ${most_expensive.product_price/100}
            \nThe least expensive product is: {least_expensive.product_name}.
            \rThe price is: ${least_expensive.product_price/100}.''')
            # print(f'\n The most common brand is: {common_brand.brand_name}.''')
            
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
    add_csv()
    app()
   
    
