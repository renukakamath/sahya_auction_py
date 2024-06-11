from flask import *
from database import *
import uuid

auctioner=Blueprint('auctioner',__name__)

@auctioner.route('/auctioner_home')
def auctioner_home():
	return render_template('auctioner_home.html')


@auctioner.route('/auctioner_view_request',methods=['get','post'])
def auctioner_view_request():
	data={}
	q="SELECT * FROM auction inner join seller using(seller_id)"
	res=select(q)
	data['user']=res
	
	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']

	else:
		action=None

	if action=='accept':
		q="update auction set status='accept' where auction_id='%s'"%(id)
		update(q)
		flash("accepted sucessfully")
		return redirect(url_for('auctioner.auctioner_manage_auction',id=id))

	if action=='reject':
		q="update auction set status='reject' where auction_id='%s'"%(id)
		update(q)
		flash("rejected!")
		return redirect(url_for('auctioner.auctioner_view_request',id=id))

	# if action=='accept':
	# 	q="select * from stock where Stock_id='%s'"%(sid)
	# 	res=select(q)
	# 	quan=res[0]['Quantity']
	# 	q="SELECT * FROM `price` ORDER BY price_id DESC LIMIT 1"
	# 	res=select(q)
	# 	print(res)
	# 	print(res[0])
	# 	price=res[0]['Price']
	# 	print(price)

	# 	amt=(int(percent)/100)*int(price)
	# 	amt=amt*int(quan)
	# 	print(amt)
	# 	return redirect(url_for('auctioner.auctioner_manage_auction',Stock_id=sid,amt=amt))

	if action=="start":
		q="update auction set status='start' where auction_id='%s'"%(id)
		update(q)
		flash("STARTED..")
		return redirect(url_for('auctioner.auctioner_view_request',id=id))

	if action=="stop":
		q="update auction set status='stop' where auction_id='%s'"%(id)
		update(q)
		flash("STOPPED!")
		return redirect(url_for('auctioner.auctioner_view_request',id=id))

	return render_template("auctioner_view_request.html",data=data)


@auctioner.route('/auctioner_view_auction',methods=['get','post'])
def auctioner_view_auction():
	data={}
	q="SELECT * FROM auction "
	res=select(q)
	data['auction']=res
	return render_template("auctioner_view_auction.html",data=data)



@auctioner.route('/auctioner_manage_auction',methods=['get','post'])
def auctioner_manage_auction():
	data={}
	aid=request.args['id']
	
	# amt=request.args['amt']
	# amt=int(amt)*int(quan)
	# data['amt']=amt
	if 'submit' in request.form:
		
		amt=request.form['amt']
		date=request.form['date']
		time=request.form['time']
		edate=request.form['edate']
		q="update auction set auction_date='%s',end_date='%s',time='%s',amount='%s' where auction_id='%s'" %(date,edate,time,amt,aid)
		update(q)
		q="insert into bid values(NULL,'%s','%s','%s','%s','pending','0')"%(aid,amt,date,time)
		insert(q)
		flash("ACCEPTED")
		
		return redirect(url_for('auctioner.auctioner_view_request'))

	# q="select *from quality"
	# res=select(q)
	# data['quality']=res

	# q="select * from auction inner join quality using(quality_id)"
	# res=select(q)
	# data['auction']=res

	# if 'action' in request.args:
	# 	action=request.args['action']
	# 	id=request.args['id']
	# else:
	# 	action=None

	# if action=="delete":
	# 	q="delete from auction where auction_id='%s'"%(id)
	# 	delete(q)
	# 	return redirect(url_for('auctioner.auctioner_manage_auction'))

	# if action == "update":
	# 	q="select* from auction where auction_id='%s'"%(id)
	# 	res= select(q)
	# 	data['updater'] = res
	# if 'update' in request.form:
	# 	price=request.form['Price_id']
	# 	q= "update price set price = '%s'  where price_id='%s' "%(price,id)
	# 	update(q)
	# 	return redirect(url_for('auctioner.auctioner_manage_price'))

	return render_template("auctioner_manage_auction.html",data=data)


@auctioner.route('/view_bid',methods=['get','post'])
def view_bid():
	data={}
	q="SELECT *,MAX(bid.amount) AS b_amt FROM auction  INNER JOIN bid USING(auction_id)   "
	res=select(q)
	data['auction']=res
	return render_template("view_bid.html",data=data)