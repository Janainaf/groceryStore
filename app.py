from models import Base, session, Product, Brands, engine

if __name__ == '__main__':
    Base.metadata.create_all(engine)