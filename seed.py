from app import app

from models import db, User, Profile, Sales, Supplier, Product, ProductOrder



users = [{
  "id": 1,
  "name": "Pryce",
  "email": "phadley0@noaa.gov"
}, {
  "id": 2,
  "name": "Kathleen",
  "email": "kwillgoose1@unicef.org"
}, {
  "id": 3,
  "name": "Cilka",
  "email": "cgoodsell2@army.mil"
}, {
  "id": 4,
  "name": "Arlyne",
  "email": "acrusham3@1und1.de"
}, {
  "id": 5,
  "name": "Cornell",
  "email": "ccake4@cam.ac.uk"
}, {
  "id": 6,
  "name": "Lorenza",
  "email": "lodempsey5@alexa.com"
}, {
  "id": 7,
  "name": "Roshelle",
  "email": "rmacavddy6@purevolume.com"
}, {
  "id": 8,
  "name": "Ellie",
  "email": "eskeels7@about.me"
}, {
  "id": 9,
  "name": "Kikelia",
  "email": "kattenburrow8@devhub.com"
}, {
  "id": 10,
  "name": "David",
  "email": "dgrushin9@bravesites.com"
}]

profiles  = [{
  "id": 1,
  "firstname": "Clarice",
  "lastname": "Anfonsi",
  "user_id": 1,
  "photo_url": "http://dummyimage.com/110x100.png/ff4444/ffffff"
}, {
  "id": 2,
  "firstname": "Hesther",
  "lastname": "Cadle",
  "user_id": 2,
  "photo_url": "http://dummyimage.com/153x100.png/5fa2dd/ffffff"
}, {
  "id": 3,
  "firstname": "Erena",
  "lastname": "Keeley",
  "user_id": 3,
  "photo_url": "http://dummyimage.com/250x100.png/dddddd/000000"
}, {
  "id": 4,
  "firstname": "Sheffy",
  "lastname": "Rouch",
  "user_id": 4,
  "photo_url": "http://dummyimage.com/179x100.png/ff4444/ffffff"
}, {
  "id": 5,
  "firstname": "Shina",
  "lastname": "Sarjeant",
  "user_id": 5,
  "photo_url": "http://dummyimage.com/140x100.png/5fa2dd/ffffff"
}, {
  "id": 6,
  "firstname": "Barnabe",
  "lastname": "Vedenisov",
  "user_id": 6,
  "photo_url": "http://dummyimage.com/150x100.png/5fa2dd/ffffff"
}, {
  "id": 7,
  "firstname": "Benni",
  "lastname": "Rolfe",
  "user_id": 7,
  "photo_url": "http://dummyimage.com/119x100.png/5fa2dd/ffffff"
}, {
  "id": 8,
  "firstname": "Cicily",
  "lastname": "Braidman",
  "user_id": 8,
  "photo_url": "http://dummyimage.com/250x100.png/ff4444/ffffff"
}, {
  "id": 9,
  "firstname": "Dick",
  "lastname": "Benez",
  "user_id": 9,
  "photo_url": "http://dummyimage.com/141x100.png/5fa2dd/ffffff"
}, {
  "id": 10,
  "firstname": "Stevie",
  "lastname": "Kenna",
  "user_id": 10,
  "photo_url": "http://dummyimage.com/160x100.png/dddddd/000000"
}]

products = [{
  "id": 1,
  "name": "Chicken - Leg, Boneless",
  "perishable": False,
  "quantity": 79,
  "price": 177
}, {
  "id": 2,
  "name": "Turkey - Breast, Boneless Sk On",
  "perishable": True,
  "quantity": 32,
  "price": 183
}, {
  "id": 3,
  "name": "Wine - Red, Gallo, Merlot",
  "perishable": True,
  "quantity": 61,
  "price": 193
}, {
  "id": 4,
  "name": "Iced Tea - Lemon, 340ml",
  "perishable": False,
  "quantity": 12,
  "price": 127
}, {
  "id": 5,
  "name": "Wine - Cahors Ac 2000, Clos",
  "perishable": True,
  "quantity": 14,
  "price": 107
}, {
  "id": 6,
  "name": "Mushroom - Oyster, Fresh",
  "perishable": False,
  "quantity": 64,
  "price": 140
}, {
  "id": 7,
  "name": "Pepper - Julienne, Frozen",
  "perishable": True,
  "quantity": 34,
  "price": 68
}, {
  "id": 8,
  "name": "Wine - Masi Valpolocell",
  "perishable": False,
  "quantity": 83,
  "price": 153
}, {
  "id": 9,
  "name": "Chicken Breast Wing On",
  "perishable": False,
  "quantity": 12,
  "price": 179
}, {
  "id": 10,
  "name": "Dried Apple",
  "perishable": False,
  "quantity": 43,
  "price": 72
}]

sales = [{
  "id": 1,
  "quantity": 67,
  "user_id": 1,
  "product_id": 1
}, {
  "id": 2,
  "quantity": 70,
  "user_id": 2,
  "product_id": 2
}, {
  "id": 3,
  "quantity": 20,
  "user_id": 3,
  "product_id": 3
}, {
  "id": 4,
  "quantity": 74,
  "user_id": 4,
  "product_id": 4
}, {
  "id": 5,
  "quantity": 43,
  "user_id": 5,
  "product_id": 5
}, {
  "id": 6,
  "quantity": 46,
  "user_id": 6,
  "product_id": 6
}, {
  "id": 7,
  "quantity": 18,
  "user_id": 7,
  "product_id": 7
}, {
  "id": 8,
  "quantity": 39,
  "user_id": 8,
  "product_id": 8
}, {
  "id": 9,
  "quantity": 66,
  "user_id": 9,
  "product_id": 9
}, {
  "id": 10,
  "quantity": 32,
  "user_id": 10,
  "product_id": 10
}]


product_orders = [{
  "id": 1,
  "quantity": 17,
  "supplier_id": 1,
  "product_id": 1
}, {
  "id": 2,
  "quantity": 94,
  "supplier_id": 2,
  "product_id": 2
}, {
  "id": 3,
  "quantity": 79,
  "supplier_id": 3,
  "product_id": 3
}, {
  "id": 4,
  "quantity": 74,
  "supplier_id": 4,
  "product_id": 4
}, {
  "id": 5,
  "quantity": 55,
  "supplier_id": 5,
  "product_id": 5
}, {
  "id": 6,
  "quantity": 72,
  "supplier_id": 6,
  "product_id": 6
}, {
  "id": 7,
  "quantity": 78,
  "supplier_id": 7,
  "product_id": 7
}, {
  "id": 8,
  "quantity": 80,
  "supplier_id": 8,
  "product_id": 8
}, {
  "id": 9,
  "quantity": 43,
  "supplier_id": 9,
  "product_id": 9
}, {
  "id": 10,
  "quantity": 72,
  "supplier_id": 10,
  "product_id": 10
}]

suppliers = [{
  "id": 1,
  "name": "Browsezoom",
  "location": "Bartelt"
}, {
  "id": 2,
  "name": "Thoughtblab",
  "location": "Scofield"
}, {
  "id": 3,
  "name": "Linklinks",
  "location": "Harper"
}, {
  "id": 4,
  "name": "Fliptune",
  "location": "Shelley"
}, {
  "id": 5,
  "name": "Livefish",
  "location": "Dawn"
}, {
  "id": 6,
  "name": "Flipopia",
  "location": "Cascade"
}, {
  "id": 7,
  "name": "Dabvine",
  "location": "Dawn"
}, {
  "id": 8,
  "name": "Nlounge",
  "location": "Burning Wood"
}, {
  "id": 9,
  "name": "Browsedrive",
  "location": "Maryland"
}, {
  "id": 10,
  "name": "Jetpulse",
  "location": "Doe Crossing"
}]


with app.app_context():
    # db.session.add_all([User(**user) for user in users])
    # db.session.commit()

    # db.session.add_all([Profile(**profile) for profile in profiles])
    # db.session.commit()

    # db.session.add_all([Product(**product) for product in products])
    # db.session.commit()

    # db.session.add_all([Sales(**sale) for sale in sales])
    # db.session.commit()

    # db.session.add_all([ProductOrder(**product_order) for product_order in product_orders])
    # db.session.commit()

    # db.session.add_all([Supplier(**supplier) for supplier in suppliers])
    # db.session.commit() 
 
 
 