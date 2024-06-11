from flask import*
from database import*

api=Blueprint('api',__name__)

@api.route('/logins')
def logins():
	data={}
	u=request.args['username']
	p=request.args['password']
	q="select * from login where username='%s' and password='%s'"%(u,p)
	res=select(q)
	if res:
		data['data']=res
		data['status']='success'
	else:
		data['status']='faild'
	return str(data)



@api.route('/userregister')
def userregister():
	data={}
	
	f=request.args['fname']
	l=request.args['lname']
	p=request.args['place']

	pho=request.args['phone']
	e=request.args['email']
	
	u=request.args['username']
	p=request.args['password']
	q="select * from login where username='%s' "%(u)
	res=select(q)
	print(q)
	if res:
		data['status']='already'
	else:
		q="insert into login values(null,'%s','%s','user')"%(u,p)
		id=insert(q)
		print(q)
		q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,f,l,p,pho,e)
		insert(q)
		print(q)
		
		data['status']='success'
		
		return str(data)



@api.route('/Viewaution')
def Viewaution():
	data={}
	q="SELECT * FROM bid INNER JOIN `auction` USING (`auction_id`) INNER JOIN seller USING (seller_id) INNER JOIN stock USING (stock_id)  group by auction_id "
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
		data['method']='Viewaution'
	return str(data)

@api.route('/Viewwinner')
def Viewwinner():

	data={}
	aid=request.args['aid']
	q="SELECT * FROM bid where auction_id='%s'  order by amount desc "%(aid)
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
		data['method']='Viewwinner'
	return str(data)


@api.route('/Viewproduct')
def Viewproduct():
	data={}
	q="SELECT * FROM `product` INNER  JOIN `quality` USING (`quality_id`)"
	res=select(q)
	if res:
		data['data']=res
		data['status']="success"
		data['method']='Viewproduct'
	return str(data)



@api.route('/Searchproduct')	
def Searchproduct():
	data={}
	search=request.args['search']+'%'
	q="SELECT * FROM `product` INNER  JOIN `quality` USING (`quality_id`)  where  product like '%s'"%(search)
	res=select(q)
	if res:
		data['status']="success"
		data['data']=res
		data['method']='search'
	else:
		data['status']="failed"
		
	return str(data)



@api.route('/Makeorder')
def Makeorder():
	data={}
	uid=request.args['login_id']
	pid=request.args['pid']
	
	
	t=request.args['total']
	qu=request.args['quantity']

	q="select * from booking where user_id=(select user_id from user where login_id='%s') and status='pending'"%(uid)
	res=select(q)
	print(q)
	if res:
		omid=res[0]['booking_id']
	else:


		q="insert into booking values(null,(select user_id from user where login_id='%s'),'0',curdate(),'pending')"%(uid)
		omid=insert(q)
		print(q)

	q="select * from bookingchild where product_id='%s' and booking_id='%s'"%(pid,omid)
	res=select(q)
	print(q)

	if res:
			odid=res[0]['bookingchild_id']	

			q="update bookingchild set quantity=quantity+'%s' , amount=amount+'%s' where bookingchild_id='%s'"%(qu,t,odid)
			update(q)
			print(q)

	else:
		w="insert into bookingchild values(null,'%s','%s','%s','%s')"%(omid,pid,qu,t)
		insert(w)
		print(w)


	q="update booking set total=total+'%s' where booking_id='%s'"%(t,omid)
	update(q)
	print(q)

	data['status']="success"

	data['data']=res
	return str(data)


@api.route('/Viewmyorder')
def Viewmyorder():
	data={}
	login_id=request.args['login_id']

	q="select * from booking inner join bookingchild using (booking_id) inner join product using (product_id) inner join user  using (user_id) where user_id=(select user_id from user where login_id='%s') "%(login_id)
	res=select(q)
	data['data']=res
	data['status']="success"
	return str(data)



@api.route('/Makepayment')
def Makepayment():
	data={}
	oid=request.args['oid']
	amt=request.args['amt']
	
	

	q="insert into payment values(null,'%s','%s',curdate())"%(oid,amt)
	insert(q)
	print(q)
	q="update booking set status='paid' where booking_id='%s'"%(oid)
	update(q)
	print(q)

	data['status']='success'
	return str(data)


