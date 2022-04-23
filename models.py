from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Brands(Base):
    __tablename__ = "brands"
    brand_id = Column(Integer, primary_key=True)
    brand_name = Column("Name", String)
    products = relationship("Product", back_populates="brand")

    def __repr__(self):
        return f'Brand: {self.brand_name}'

class Product(Base):
    __tablename__ = "products"
    product_id = Column(Integer, primary_key=True)
    product_name = Column("Name", String)
    product_quantity = Column("Quantity", Integer)
    product_price = Column("Price", Integer)
    date_updated = Column("Date", Date)
    brand_id = Column(Integer, ForeignKey("brands.brand_id"))
    brand = relationship("Brands", back_populates="products")


    def __repr__(self):
        return f"""
        \nProduct: {self.product_name} \r
        Quantity: {self.product_quantity}
        Price: {self.product_price}
        Date: {self.date_updated}
        Brand ID: {self.brand_id}
      
        """

