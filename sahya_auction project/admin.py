from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():



	return render_template('admin_home.html')

@admin.route('/view_quality',methods=['get','post'])
def view_quality():    
    data={}
    q="select * from quality"
    res=select(q)
    data['qua']=res

    if "submit" in request.form:

         
        quality=request.form['quality']
        percent=request.form['percent']

        
        q="insert into quality values (null,'%s','%s')"%(quality,percent)
        insert(q)
        flash("inserted successfully")
        return redirect(url_for('admin.view_quality'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=="update":
        q="select * from quality where quality_id='%s'"%(id)
        res=select(q)
        data['up']=res
        
    if 'update'in request.form:
        quality=request.form['quality']
        percent=request.form['percent']
        q="update quality set quality='%s',percent='%s' where quality_id='%s'"%(quality,percent,id)
        update(q)
        flash("updated successfully")
        return redirect(url_for('admin.view_quality'))
 

    if action=="delete":
        q="delete from quality where quality_id='%s'"%(id)
        delete(q)
        flash("deleted successfully")
        return redirect(url_for('admin.view_quality'))

    return render_template('view_quality.html',data=data)
	    
@admin.route('/view_farmer',methods=['get','post'])
def view_farmer():    
    data={}
    q="select * from farmer inner join login using(login_id)"
    res=select(q)
    data['sel']=res
    # if "submit" in request.form:

    #     seller_id=request.form['seller_id']
    #     login_id=request.form['login_id']   
    #     fname=request.form['fname']
    #     place=request.form['place']
    #     phone=request.form['phone']
    #     email=request.form['email']

    #     print(seller_id,login_id,fname,place,phone,email)
    #     q="insert into seller values (null,'%s','%s','%s')"%(seller_id,login_id,fname,place,phone,email)
    #     insert(q)
    #     return redirect(url_for('admin.view_farmer'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=="accept":
        q="update login set usertype='farmer'  where login_id='%s'"%(id)
        update(q)
        return redirect(url_for('admin.view_farmer'))

    if action=="reject":
        q="update login set usertype='reject'  where login_id='%s'"%(id)
        update(q)
        return redirect(url_for('admin.view_farmer'))
        
    # if 'edit'in request.form:
    #     quality=request.form['quality']
    #     percent=request.form['percent']
    #     q="update seller set quality='%s',percent='%s' where quality_id='%s'"%(quality,percent)
    #     update(q)
    #     return redirect(url_for('admin.view_farmer'))
    return render_template('view_farmer.html',data=data)


@admin.route('/admin_view_seller',methods=['get','post'])
def admin_view_seller():    
    data={}
    q="select * from seller inner join login using(login_id)"
    res=select(q)
    data['sel']=res
    # if "submit" in request.form:

    #     seller_id=request.form['seller_id']
    #     login_id=request.form['login_id']   
    #     fname=request.form['fname']
    #     place=request.form['place']
    #     phone=request.form['phone']
    #     email=request.form['email']

    #     print(seller_id,login_id,fname,place,phone,email)
    #     q="insert into seller values (null,'%s','%s','%s')"%(seller_id,login_id,fname,place,phone,email)
    #     insert(q)
    #     return redirect(url_for('admin.view_farmer'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=="accept":
        q="update login set usertype='seller'  where login_id='%s'"%(id)
        update(q)
        return redirect(url_for('admin.admin_view_seller'))

    if action=="reject":
        q="update login set usertype='block'  where login_id='%s'"%(id)
        update(q)
        return redirect(url_for('admin.admin_view_seller'))
        
    # if 'edit'in request.form:
    #     quality=request.form['quality']
    #     percent=request.form['percent']
    #     q="update seller set quality='%s',percent='%s' where quality_id='%s'"%(quality,percent)
    #     update(q)
    #     return redirect(url_for('admin.view_farmer'))
    return render_template('admin_view_seller.html',data=data)

@admin.route('/auctioneer',methods=['get','post'])
def auctioneer():    
    data={}
    q="select * from auctioneer inner join login using(login_id)"
    res=select(q)
    data['aur']=res
    if "submit" in request.form:
        name=request.form['autioner_name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        uname=request.form['uname']
        pasd=request.form['password']

        q="insert into login values (null,'%s','%s','auctioner')"%(uname,pasd)
        lid=insert(q)

  
        q="insert into auctioneer values (null,'%s','%s','%s','%s','%s')"%(lid,name,place,phone,email)
        insert(q) 
        flash("inserted successfully")
        return redirect(url_for('admin.auctioneer'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=="update":
        q="select * from auctioneer where auctioner_id='%s'"%(id)
        res=select(q)
        data['up']=res

    if 'update'in request.form:
        name=request.form['autioner_name']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']  
        q="update auctioneer set auctioner_name='%s',place='%s',phone='%s',email='%s' where auctioner_id='%s'"%(name,place,phone,email,id)
        update(q)
        flash("updated successfully")
        return redirect(url_for('admin.auctioneer'))
    
    return render_template('auctioneer.html',data=data)


@admin.route('/manage_products',methods=['get','post'])
def manage_products():
    data={}
    q="select * from product inner join quality using(quality_id)"
    res=select(q)
    data['pros']=res

    s="select * from quality"
    res1=select(s)
    data['quality']=res1
    if "submit" in request.form:
        quality=request.form['qty']
        product=request.form['product']
        weight=request.form['weight']
        details=request.form['details']
        rate=request.form['rate']
        stock=request.form['stock']
        
        i=request.files['image']
        img='static/'+str(uuid.uuid4())+i.filename
        i.save(img) 
        q="insert into product values (null,'%s','%s','%s','%s','%s','%s','%s')"%(quality,product,weight,details,rate,stock,img)
        insert(q)
        flash("inserted successfully")
        return redirect(url_for('admin.manage_products'))
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
       
    else:
        action=None

    if action=="update":
        q="select * from product where product_id='%s'"%(id)
        res=select(q)
        data['up']=res
        
    if 'update'in request.form:
        
        product=request.form['product']
        weight=request.form['weight']
        details=request.form['details']
        rate=request.form['rate']
        stock=request.form['stock']
        i=request.files['image']
        img='static/'+str(uuid.uuid4())+i.filename
        i.save(img)
        q="update product set product='%s',weight='%s',details='%s',rate='%s',stock='%s',imag='%s' where product_id='%s'"%(product,weight,details,rate,stock,img,id)
        update(q)
        flash("inserted successfully")
        return redirect(url_for('admin.manage_products'))
        
    if action=="delete":
        q="delete from product where product_id='%s'"%(id)
        delete(q)
        flash("deleted successfully")
        return redirect(url_for('admin.manage_products'))
          
    
    return render_template('manage_products.html',data=data)    
        
@admin.route('/admin_manage_fertilizer',methods=['get','post'])
def admin_manage_fertilizer():
    data={}
    q="select * from fertilizer"
    res=select(q)
    data['fer']=res
    if "submit" in request.form:
       
        fertilizer=request.form['fertilizer']
        details=request.form['details']
        price=request.form['price']
        stock=request.form['stock']
        i=request.files['image']
        img='static/'+str(uuid.uuid4())+i.filename
        i.save(img)
        
        q="insert into fertilizer values (null,'%s','%s','%s','%s','%s')"%(fertilizer,details,price,stock,img)
        insert(q)
        flash("inserted successfully")
        return redirect(url_for('admin.admin_manage_fertilizer'))
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None

    if action=="update":
        q="select * from fertilizer where fertilizer_id='%s'"%(id)
        res=select(q)
        data['up']=res
        
    if 'update'in request.form:
        fertilizer=request.form['fertilizer']
        details=request.form['details']
        price=request.form['price']
        stock=request.form['stock']
        i=request.files['image']
        img='static/'+str(uuid.uuid4())+i.filename
        i.save(img)
        q="update fertilizer set fertilizer='%s',details='%s',price='%s',stock='%s',image='%s' where fertilizer_id='%s'"%(fertilizer,details,price,stock,img,id)
        update(q)
        flash("updated successfully")
        return redirect(url_for('admin.admin_manage_fertilizer'))
 

    if action=="delete":
        q="delete from fertilizer where fertilizer_id='%s'"%(id)
        delete(q)
        flash("deleted successfully")
        return redirect(url_for('admin.admin_manage_fertilizer'))
          
    return render_template('admin_manage_fertilizer.html',data=data)  

@admin.route('/product_admin_header')
def product_admin_header(): 
    data={}
    
    return render_template('product_admin_header.html',data=data) 


@admin.route('/fertilizer_admin_header')
def fertilizer_admin_header():
    data={}
    
    return render_template('fertilizer_admin_header.html',data=data) 

@admin.route('/view_product_booking')
def view_product_booking():    
    data={}
    q="select * from bookingchild_id"
    res=select(q)
    data['bokpro']=res
    return render_template('view_product_booking.html',data=data) 

@admin.route('/view_fertilizer_booking')
def view_fertilizer_booking():    
    data={}
    q="select * from bookfertilizer"
    res=select(q)
    data['bokfer']=res
    return render_template('view_fertilizer_booking.html',data=data) 


@admin.route('/view_rating',methods=['get','post'])
def view_rating():
    data={}
    q="select * from rating"
    res=select(q)
    data['rat']=res
    return render_template('view_rating.html',data=data)


@admin.route('/view_complaint')
def view_complaint():
    data={}
    q="select * from complaint"
    res=select(q)
    data['complt']=res
    return render_template('view_complaint.html',data=data) 

@admin.route('/sent_reply',methods=['get','post'])
def sent_reply():
    data={}
    
 
    if "submit" in request.form:
        c=request.form['comment']
        id=request.args['id']
        q="update complaint set reply='%s' where complaint_id='%s'"%(c,id)
        print(q)
        update(q)
        return render_template(url_for('admin.view_complaint'))
    
    return render_template('sent_reply.html',data=data)

@admin.route('/admin_view_auction',methods=['get','post'])
def admin_view_auction():
    data={}
    q="select * from auction inner join products using(product_id)"
    res=select(q)
    data['auction']=res

    return render_template("admin_view_request.html",data=data)


@admin.route('/admincomplaint',methods=['get','post'])
def admincomplaint():
    data={}
    q="SELECT * FROM complaint inner join buyer on buyer.login_id=complaint.user_id"
    res=select(q)
    data['comp']=res

    return render_template("admin_view_complaint.html",data=data)

@admin.route('/admin_reply',methods=['get','post'])
def admin_replay():
    id=request.args['id']
    data={}
    q="select * from complaint where complaint_id='%s'"%(id)
    res=select(q)
    data['rep']=res     
        
    if 'submit' in request.form:
        re=request.form['replay']
        q="UPDATE complaint SET reply='%s' WHERE complaint_id='%s'"%(re,id)
        update(q)
        return redirect(url_for('admin.admincomplaint',id=id))

    return render_template("admin_reply.html",data=data)