from flask import Flask, render_template, redirect, request, url_for
import requests
import os 
# import stripe

from flask import Flask, jsonify



# Created by Mohammed Draem 
# HotSpot Liberia 

# Activate ENV
# source env/bin/activate
# deactivate


# Run flash 
# flask run
# Control + C = Stop server 



app = Flask(__name__)

# Global Variables
# stripe.api_key = 'sk_test_yuGxi42ym6ora4NW7GwUUcwy00boyFSmp0'

# home route 
@app.route('/')
def index():
    # display only 
    return render_template('index.html') #home page

# @app.route('/create-checkout-session', methods=['POST'])
# def create_checkout_session():
#   session = stripe.checkout.Session.create(
#     payment_method_types=['card'],
#     line_items=[{
#       'price_data': {
#         'currency': 'usd',
#         'product_data': {
#           'name': 'T-shirt',
#         },
#         'unit_amount': 2000,
#       },
#       'quantity': 1,
#     }],
#     mode='payment',
#     success_url='https://example.com/success',
#     cancel_url='https://example.com/cancel',
#   )

#   return jsonify(id=session.id)
    

# downlaoding music processing route
@app.route('/converting', methods=['GET', 'POST'])
def converting_url():

    return render_template('converting.html',  urls=urls)

    


# about route 
@app.route('/about')
def about():
    # display only 
    return render_template('about.html') #home page
    
# Render contant to github page
    

# pravicy route 
@app.route('/pp')
def pp():
    # display only 


    return render_template('privacypolicy.html') #home page
    




# main module page 
if __name__ == "__main__":
    app.run(debug=True)

# Todo:
    # Error handle code
    # progress Hud
    # Specific Directory location to download file to
