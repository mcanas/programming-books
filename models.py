from sqlalchemy import create_engine, Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///books.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    date_published = Column(Date)
    price = Column(Integer)

    def __repr__(self):
        return f'<User(title={self.title} author={self.author} date_published={self.date_published} price={self.price})>'
