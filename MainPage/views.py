from django.shortcuts import render_to_response
from django.template import RequestContext
from Member.models import Account
from Product.models import Product
# Create your views here.

def Home(request):

	member = Account.objects.filter(online = 1)
	tmp = []
    	account = {}

   	product = []
	if 'lbsv' in request.session:
		account_login = request.session['lbsv']
	else:
		account_login = ''

	
	for e in member:
		tmp.append(Product.objects.filter(owner = e.id))
    
   	for t_element in tmp:
        	for t_ele_element in t_element:
			account = Account.objects.get(id = t_ele_element.owner)
			
	            	product.append(t_ele_element)
	

	
	
	return render_to_response('index.html',RequestContext(request,locals()))


