from flask import *
from database import *
import uuid
import datetime

buyer=Blueprint('buyer',__name__)

@buyer.route('/buyer_home')
def buyer_home():
	return render_template('buyer_home.html')

@buyer.route('/buyer_view_auction',methods=['get','post'])
def buyer_view_auction():
	data={}
	q="SELECT * FROM auction "
	res=select(q)
	data['auction']=res
	return render_template("buyer_view_auction.html",data=data)

@buyer.route('/buyercomplaint',methods=['get','post'])
def buyercomplaint():
	id=session['bid']
	data={}
	q="select * from complaint where user_id='%s'"%(session['login_id'])
	res=select(q)
	data['comp']=res
	
	if 'submit' in request.form:
		comp=request.form['complaint']
		q="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['login_id'],comp)
		id=insert(q)
		return redirect(url_for('buyer.buyercomplaint'))

	return render_template("buyer_send_complaint.html",data=data)


# @buyer.route('/buyer_make_bid',methods=['get','post'])
# def buyer_make_bid():
# 	data={}
# 	current_time = datetime.datetime.now()
# 	bid=session['bid']
# 	id=request.args['id']
# 	amt=request.args['amount']
# 	data['am']=amt

# 	if 'submit' in request.form:
		
# 		amount=request.form['amt']
# 		q="insert into bid values(null,'%s','%s',curdate(),current_time,'0','%s')"%(id,amount,bid)
# 		insert(q)
# 		flash("inserted successfully")
# 		return redirect(url_for('buyer.buyer_view_auction',amount=amt,id=id))

# 	return render_template("buyer_make_bid.html",data=data)

@buyer.route('/buyer_make_bid',methods=['get','post'])	
def buyer_make_bid():
	bid=session['bid']
	aid=request.args['aid']
	data={}
	q="select max(amount) as amts from bid where auction_id='%s' order by(amount)"%(aid)
	res=select(q)
	data['minamt']=res[0]['amts']
	q="SELECT * FROM bid inner join buyer using(buyer_id) where auction_id='%s' and buyer_id='%s' order by(amount) desc"%(aid,session['bid'])
	res=select(q)
	data['bid']=res

	q="select * from auction inner join bid using (auction_id) where auction.status='start'"
	re=select(q)
	if re:
		if 'submit' in request.form:
			myamt=request.form['myamt']
			# q="insert into bid values(NULL,'%s','%s','%s',NOW())"%(bid,aid,myamt)
			# insert(q)
			q="insert into bid values(null,'%s','%s',curdate(),current_time,'0','%s')"%(aid,myamt,bid)
			insert(q)
			flash("Successfully Added..!")
			return(redirect(url_for('buyer.buyer_make_bid',aid=aid)))
	else:
		flash("Sorry timeout..!")

	
	return render_template("buyer_make_bid.html",data=data)

@buyer.route('/buyer_view_bid_assigned',methods=['get','post'])	
def buyer_view_bid_assigned():
	data={}
	bid=session['bid']
	data['bid']=bid
	q="SELECT * FROM `auction`INNER JOIN seller USING (seller_id) INNER JOIN stock USING(`stock_id`)  INNER JOIN quality USING(quality_id) WHERE  auction.status='stop'"
	res=select(q)
	data['auction']=res

	

	if 'action' in request.args:
		aid=request.args['aid']
		q="SELECT * FROM bid inner join buyer using(buyer_id) where auction_id='%s' order by(amount) desc"%(aid)
		res=select(q)
		if res:
			data['assigned']=res[0]
	if 'action2' in request.args:
		amt=request.args['amt']
		aid=request.args['aid']
		q="select * from auction where auction_id='%s'"%(aid)
		res=select(q)
		wt=res[0]['weight']
		total=int(wt)*int(amt)
		data['total']=total
		q="select * from auctionpayment where auction_id='%s'"%(aid)
		res=select(q)
		if res:
			flash("ALREADY PAID")
		else:
			data['amt']=amt
			
	if 'pay' in request.form:
		amt=request.args['amt']

		q="insert into auctionpayment values(NULL,'%s','%s',NOW())"%(aid,amt)
		insert(q)
		# q="insert into cargo_status values(NULL,'%s','pending',NOW()"%(boid)
		# insert(q)
		q="update auction set status='paid' where auction_id='%s'"%(aid)
		update(q)
		flash("PAYMENT SUCESS")

		return redirect(url_for('buyer.buyer_view_bid_assigned'))
		
	return render_template("buyer_view_bid_assigned.html",data=data)


@buyer.route('/buyer_view_bill',methods=['get','post'])	
def buyer_view_bill():
	data={}
	amt=request.args['amt']
	data['amt']=amt
	aid=request.args['aid']
	q="SELECT * FROM `auction`INNER JOIN seller USING(seller_id) INNER JOIN stock USING(`stock_id`)  INNER JOIN quality USING(quality_id) WHERE auction_id='%s'"%(aid)
	res=select(q)
	data['auction']=res
		
	return render_template("buyer_view_bill.html",data=data)
