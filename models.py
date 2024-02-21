from flask_sqlalchemy  import SQLAlchemy 
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(25))

    # since this is a one to one rlshp ie one user can only have one profile hence the use of uselist = False
    profile = db.relationship('Profile', backref = 'user', uselist = False)

    # db.relationship shows that this class is related to class Sales and (find out the use of backrefs/backpopulates)
    purchases = db.relationship("Sales", backref = 'user' )


class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key= True) 
    firstname = db.Column(db.String(25))
    lastname = db.Column(db.String(25))
    photo_url = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Sales(db.Model):
    __tablename__ = "sales"

    id = db.Column(db.Integer, primary_key= True)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))


class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    location = db.Column(db.String)

    orders = db.relationship('ProductOrder', backref="supplier")


class Product(db.Model, SerializerMixin):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String)
    perishable = db.Column(db.Boolean)
    quantity = db.Column(db.Integer)
    price= db.Column(db.Float)

    orders = db.relationship('ProductOrder', backref="product")
    sales = db.relationship('Sales', backref="product")

class ProductOrder(db.Model):
    __tablename__ = 'product_orders'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer, db.ForeignKey('suppliers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))



