from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/shop')
def shop_front_view():
    products = [
        {
            "name": "Dog Shampoo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15
        },
         {
            "name": "Dog Shampoo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15
        },
         {
            "name": "Dog Shampoo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15
        },
         {
            "name": "Dog Shampoo",
            "brand" : "Top fin",
            "price" : 14.24,
            "stock" : 15,
            "image" : "https://s7d2.scene7.com/is/image/PetSmart/5252898?$HP3101$"
        },
    ]


    return render_template('shopfront.html', products=products)


@app.route('/<nomber>')
def geeting(nomber):
    return render_template('front.html', nomber=nomber)

