from models import Base, session, Product, Brands, engine
import datetime
import csv

def add_csv():
    with open('brands.csv') as csvfile:
        data_brands = csv.reader(csvfile)
        for row in data_brands:
            print(row)
    with open('inventory.csv') as csvfile:
        data_products = csv.reader(csvfile)
        for row in data_products:
            print(row)


def app():
    print("hello")

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    add_csv()