from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from Member.models import Account
# Create your views here.


def LoginPage(request):
    
    if(request.POST):
        AccObj = Account.objects.get(acc = request.POST['lbsv'])
    
        if AccObj :
            if AccObj.pwd == request.POST['jpu']: 
		request.session['lbsv'] = request.POST['lbsv']        
                return HttpResponseRedirect("../")
            else :
                return render_to_response('LoginRegis.html',RequestContext(request,locals()))
            
        else :
            return render_to_response('LoginRegis.html',RequestContext(request,locals()))
           
    
    else:
        
	   return render_to_response('LoginRegis.html',RequestContext(request,locals()))


def Logout(request):
    if request.session['lbsv'] :
        del request.session['lbsv']
        return HttpResponseRedirect('../')


def Register(request):
	if 'lbsv' in request.POST and 'jpu' in request.POST:
		acc = request.POST['lbsv'] 
		pwd = request.POST['jpu']
		exist = 0 	
	
		check_db = Account.objects.filter(acc = acc)
		if check_db :
			exist = 100
		else :
			a = Account( acc = acc,
				     pwd = pwd,
				     online = 0)
			a.save()
		return render_to_response('Register.html',RequestContext(request,locals()))


def Update():

	for e in Account.objects.filter(online = 0) :
		aid = e.id
		Account.objects.filter(id = aid).update(online = 1)
