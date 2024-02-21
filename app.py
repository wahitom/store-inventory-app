from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api, reqparse, abort

from models import db, User, Profile, Sales, Supplier, Product, ProductOrder



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)
post_args = reqparse.RequestParser()
post_args.add_argument('id', type=int, required=True)
post_args.add_argument('name', type = str, required = True, help = "name of the product")
post_args.add_argument('perishable', type = bool, required = True, help = "perishability of the product required")
post_args.add_argument('quantity', type = int, required = True, help = "quantity of the product required")
post_args.add_argument('price', type = float, required = True, help='Price is required')


class ProductResource(Resource):
    
    def get(self):
        products = Product.query.all()
        response = [product.to_dict() for product in products]
        return response

    def post(self):
        pass


class ProductById(Resource):

    def get(self, id):
        # get a product by its id  
        product = Product.query.get(id)
        if not product:
            abort(404, detail = f"producct with {id = } does not exist")
        return product.to_dict()

    def post(self, id):
        pass

    def patch(self, id):
        pass

    def delete(self, id):
        # delete a product by its id 
        product = Product.query.filter_by(id = id).first()

        # check if the prodct exists
        if not product:
         abort(404, detail = f"producct with {id = } does not exist")

    
        db.session.delete(product)
  
        db.session.commit()
        return{"message": f"product with {id =} has been deleted sucessfully"}
    

api.add_resource(ProductResource, '/products')
api.add_resource(ProductById, '/products/<int:id>')



   
if __name__ == '__main__':
    app.run(port = 5000, debug=True)