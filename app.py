from models import Base, session, Product, Brands, engine
import datetime
import csv


def menu():
    while True:
        print('''
            \nWelcome to My Store Inventory
            \n ****Here are your choices ****
            \nN) Add New Product
            \rV) View a Product by ID
            \rA) Product Analysis
            \rB) Backup the Database
            \rQ) Quit the Application
            ''')
        input('What would you like to do? ')

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
    print("hello")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    menu()
    # add_csv()