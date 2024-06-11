from flask import *
from database import *
import uuid

seller=Blueprint('seller',__name__)


@seller.route('/seller_home')
def seller_home():
	return render_template('seller_home.html')


@seller.route('/view_auction')
def view_auction():    
    data={}
    q="select * from auction"
    res=select(q)
    data['auct']=res
    return render_template('view_auction.html',data=data) 	


@seller.route('/fertilizers',methods=['get','post'])
def fertilizers():   
    data={}
    q="select * from fertilizer"
    res=select(q)
    print(q)
    print(res)
    data['fer']=res 

    return render_template('fertilizers.html', data=data)


@seller.route('/seller_request',methods=['get','post'])
def seller_request():
    data={}
    q="select * from auction  where seller_id='%s'"%(session['sid'])
    res=select(q)
    data['fer']=res

    s="select * from quality inner join stock using(quality_id)"
    res1=select(s)
    data['quality']=res1
    if "submit" in request.form:
        quality=request.form['fertilizer']
        product=request.form['details']
        stock=request.form['stock']
        i=request.files['image']
        img='static/'+str(uuid.uuid4())+i.filename
        i.save(img)
        # weight=request.form['price']
        # details=request.form['stock']
        # rate=request.form['amt']
        q="insert into auction values (null,'%s','%s','%s','0','0','0','0','0','pending','%s','%s')"%(session['sid'],quality,product,stock,img)
        insert(q)
        flash("inserted successfully")
        return redirect(url_for('seller.seller_request'))

    return render_template('seller_request.html', data=data)


@seller.route('/view_quality',methods=['get','post'])
def view_quality():    
    data={}
    q="select * from quality"
    res=select(q)
    data['qua']=res

    if "submit" in request.form:

         
        quality=request.form['quality']
        percent=request.form['percent']

        q="select * from quality where quality='%s'"%(quality)
        res=select(q)
        if res:
            flash("alredy added..!")
        else:
            q="insert into quality values (null,'%s','%s')"%(quality,percent)
            insert(q)
            flash("inserted successfully")
            return redirect(url_for('seller.view_quality'))

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
        return redirect(url_for('seller.view_quality'))
 

    if action=="delete":
        q="delete from quality where quality_id='%s'"%(id)
        delete(q)
        flash("deleted successfully")
        return redirect(url_for('seller.view_quality'))

    return render_template('view_quality.html',data=data)


@seller.route('/manage_stock',methods=['get','post'])
def manage_stock():    
    data={}
    q="select * from stock inner join quality using(quality_id) where seller_id='%s'"%(session['sid'])
    res=select(q)
    data['pros']=res

    q="select * from quality "
    data['qty']=select(q)
    if "submit" in request.form:
        name=request.form['qty']
        place=request.form['stock']
        q="insert into stock values (null,'%s','%s','%s')"%(name,session['sid'],place)
        insert(q) 
        flash("inserted successfully")
        return redirect(url_for('seller.manage_stock'))

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None

    if action=="update":
        q="select * from stock where stock_id='%s'"%(id)
        res=select(q)
        data['up']=res

    if 'update'in request.form:
        place=request.form['stock']
        q="update stock set stock='%s' where stock_id='%s'"%(place,id)
        update(q)
        flash("updated successfully")
        return redirect(url_for('seller.manage_stock'))
    
    return render_template('admin_manage_stock.html',data=data)

@seller.route('/seller_book_product',methods=['get','post'])
def seller_book_product():
    data={}
    # sid=request.args['sid']
    fid=request.args['fid']
    amt=request.args['amt']
    qua=request.args['sid']
    print("+++++++++++")
    qua=qua.split('kg')[0]
    print(qua)
    data['qua']=qua
    data['amt']=amt
    if 'submit' in request.form:
        quantity=request.form['quantity']
        amount=request.form['total_amount']
        q="insert into bookfertilizer values(null,'%s','%s','%s','%s',curdate(),'booked')"%(session['sid'],fid,quantity,amount)
        id=insert(q)
        
        return redirect(url_for('seller.seller_view_booking_details',amount=amount,qua=quantity,bid=id))
    return render_template("seller_book_product.html",data=data)

@seller.route('/seller_view_product')
def seller_view_product():
    data={}
    q="select * from product  inner join quality using(quality_id) "
    res=select(q)
    data['request']=res
    return render_template("seller_view_product.html",data=data)

@seller.route('/seller_view_booking_details',methods=['get','post'])  
def seller_view_booking_details():
    amount=request.args['amount']
    qua=request.args['qua']
    bid=request.args['bid']
    if 'submit' in request.form:

        q="insert into payment values(null,'%s','%s',curdate())"%(bid,amount)
        insert(q)
        q="update bookfertilizer set status='paid' where bookfertilizer_id='%s'"%(bid)
        update(q)
        flash("booked sucessfully")
        return redirect(url_for('seller.fertilizers'))
    
    return render_template("seller_view_booking_details.html",amount=amount)


@seller.route('/seller_view_booking')
def seller_view_booking():
    data={}
    q="SELECT * FROM bookfertilizer INNER JOIN payment ON payment.booking_id=bookfertilizer.bookfertilizer_id INNER JOIN fertilizer USING(fertilizer_id) "
    res=select(q)
    data['request']=res
    return render_template("seller_view_booking.html",data=data)