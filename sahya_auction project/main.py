from flask import Flask 
from public import public
from admin import admin
from seller import seller
from auctioner import auctioner
from buyer import buyer
from api import api


app=Flask(__name__)
app.secret_key="aaaaa"
app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(seller,url_prefix='/seller')
app.register_blueprint(auctioner,url_prefix='/auctioner')
app.register_blueprint(buyer,url_prefix='/buyer')

app.register_blueprint(api,url_prefix='/api')

app.run(debug=True,port=5234,host="0.0.0.0")



