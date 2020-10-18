from flask import Flask, render_template, redirect, request, url_for
import requests
import os 
import stripe

from pytube import YouTube



# Created by Mohammed Draem 
# HotSpot Liberia 

# Activate ENV
# source env/bin/activate
# deactivate


# Run flash 
# flask run
# Control + C = Stop server 



app = Flask(__name__)



# home route 
@app.route('/')
def index():
    # display only 
    return render_template('index.html') #home page
    

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
