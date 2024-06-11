from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():

	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
    if "submit" in request.form:
        user=request.form['username']
        pasd=request.form['password']
        q="select * from login where username='%s' and password='%s'"%(user,pasd)
        res=select(q)
        if res:
            login_id=res[0]['login_id']
            session['login_id']=login_id

            if res[0]['usertype']=="admin":
                return redirect(url_for('admin.admin_home'))

            if res[0]['usertype']=='seller':
                q="SELECT * FROM `seller` WHERE login_id='%s'"%(login_id)
                res=select(q)
                if res:
                    session['sid']=res[0]['seller_id']
                    flash("welcome seller")
                    return redirect(url_for('seller.seller_home'))

            if res[0]['usertype']=='buyer':
                q="SELECT * FROM `buyer` WHERE login_id='%s'"%(login_id)
                res=select(q)
                if res:
                    session['bid']=res[0]['buyer_id']
                    flash("welcome buyer")
                    return redirect(url_for('buyer.buyer_home'))

            if res[0]['usertype']=='auctioner':
                q="SELECT * FROM `auctioneer` WHERE login_id='%s'"%(login_id)
                res=select(q)
                if res:
                    session['aid']=res[0]['auctioner_id']
                    flash("welcome auctioner")
                    return redirect(url_for('auctioner.auctioner_home'))

        else:

            flash("INVALID USERNAME OR PASSWORD")
            
    return render_template('login.html')

@public.route('/seller_register',methods=['get','post'])
def seller_register():
    if "submit" in request.form:

        name=request.form['autioner_name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        pasd=request.form['password']
        q="insert into login values (null,'%s','%s','seller')"%(uname,pasd)
        lid=insert(q)
        q="insert into seller values (null,'%s','%s','%s','%s','%s')"%(lid,name,place,phone,email)
        insert(q) 
        flash("inserted successfully")
        return redirect(url_for('public.login'))
    return render_template('seller_register.html')	


@public.route('/buyer_register',methods=['get','post'])
def buyer_register():
    if "submit" in request.form:
        
        name=request.form['autioner_name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        pasd=request.form['password']
        q="insert into login values (null,'%s','%s','buyer')"%(uname,pasd)
        lid=insert(q)
        q="insert into buyer values (null,'%s','%s','%s','%s','%s')"%(lid,name,place,phone,email)
        insert(q) 
        flash("inserted successfully")
        return redirect(url_for('public.login'))
    return render_template('buyer_register.html')	