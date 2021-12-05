from sqlalchemy import DateTime, Boolean, Column, String, Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from my_app import db
from flask_login import UserMixin
from datetime import datetime
import enum

class MyRole(enum.Enum):
    USER = 1
    ADMIN = 0


class Category (db.Model):
    __tablename__ = "cate"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship("Product", backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(String(100), nullable=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)
    receipt_details = relationship("ReceiptDetail", backref="product", lazy=True)

    def __str__(self):
        return self.name

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    joines_date = Column(DateTime, default=datetime.now())
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    avatar = Column(String(100), nullable=True)
    role = Column(Enum(MyRole), default=MyRole.USER)
    receipts = relationship("Receipt", backref="user", lazy=True)
    def __str__(self):
        return self.name

class Receipt(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    details = relationship("ReceiptDetail", backref="receipt", lazy=True)

class ReceiptDetail(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    receipt_id = Column(Integer, ForeignKey(Receipt.id), nullable=False)
    product_id = Column(Integer, ForeignKey(Product.id), nullable=False)
    quantity = Column(Integer, default=0)
    unit_price = Column(Float, default=0)



if __name__ == "__main__":
    db.create_all()
