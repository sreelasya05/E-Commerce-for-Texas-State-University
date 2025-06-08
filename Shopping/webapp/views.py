from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import *
from django.db.models import F
from django.db.models import Q
from itertools import chain

# Create your views here.
def home(request):
    request.session["msg"] = ''
    return render(request, 'index.html')


# Create your views here.
def alogin(request):
    return render(request, 'admin.html')


def adminlogin(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']

        if uid == 'admin' and pwd == 'admin':
            request.session['adminid'] = 'admin'
            return render(request, 'admin_home.html')

        else:
            return render(request, 'admin.html', {'msg': "Login Fail"})

    else:
        return render(request, 'admin.html')


def adminhomedef(request):
    if "adminid" in request.session:
        uid = request.session["adminid"]
        return render(request, 'admin_home.html')

    else:
        return render(request, 'admin.html')


def adminlogoutdef(request):
    try:
        del request.session['adminid']
    except:
        pass
    return render(request, 'admin.html')



def userlogindef(request):
    return render(request, 'user.html')


def signupdef(request):
    return render(request, 'signup.html')


def usignupactiondef(request):
    userid = request.POST['userid']
    email = request.POST['mail']
    pwd = request.POST['pwd']
    ph = request.POST['ph']
    gen = request.POST['gen']
    name = request.POST['name']
    que = request.POST['que']
    ans = request.POST['ans']

    d = students.objects.filter(userid__exact=userid).count()
    if d > 0:
        return render(request, 'signup.html', {'msg': "User ID is already registered"})

    if email.endswith('.edu')==False:
        return render(request, 'signup.html', {'msg': "Email should ends with .EDU"})


    else:
        d = students(name=name, email=email, password=pwd, phone=ph, gender=gen, userid=userid, question=que, answer=ans)
        d.save()
        d = categories.objects.all()
        return render(request, 'signup2.html', {'data':d,'uid': userid })


def usignupaction2def(request):
    userid = request.POST['userid']
    dept = request.POST['dept']
    year = request.POST['year']
    intrests = request.POST.getlist('intrests')
    s=""


    for i in intrests:
        s+=i+";"


    print(s,'<<<<<<<<<<<<<<<')
    students.objects.filter(userid = userid).update(department = dept, year = year, intrests=s)
    return render(request, 'signup.html', {'msg': "Registration is completed !!"})

    

def userloginactiondef(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        pwd = request.POST['pwd']
        d = students.objects.filter(userid__exact=uid).filter(password__exact=pwd).count()

        if d > 0:
            d = students.objects.filter(userid__exact=uid)
            request.session['userid'] = uid
            request.session['email'] = d[0].email
            request.session['name'] = d[0].name
            request.session['userid'] = d[0].userid
            c = categories.objects.all()


            d1=students.objects.filter(userid__exact=uid)
            I=d1[0].intrests
            I= I.split(';')
            print(I,':::::::::::::::::::')
            rec1=products.objects.filter(cat_name__in=I).filter(availability__gte=1).order_by('-id')[:5:1]
            print(rec1,"???????????????????????")



            d1=missing.objects.filter(userid__exact=uid)
            l1=[]

            for d11 in d1:
                print(d11.keywords,'^^^^^^^^^^^^^^^^^')
                rc1=products.objects.filter(keywords__icontains=d11.keywords).filter(availability__gte=1)
                l1.append(rc1)
            rec2=chain(l1)
            print(rec2)

            rec2=list(rec2)

            for r in rec2:
                for r1 in r:
                    print(r1.name)

            rec3=products.objects.all().filter(availability__gte=1).order_by('-id')[:5:1]



            return render(request, 'user_home.html', {'data': d[0], 'cat':c, 'rec1':rec1, 'rec2':rec2, 'rec3':rec3 })
        else:
            return render(request, 'user.html', {'msg': "Login Fail"})

    else:
        return render(request, 'user.html')


def forget(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        print('>>>>>>>>>', uid)
        d = students.objects.filter(userid__exact=uid).count()

        if d>0:
            d = students.objects.filter(userid__exact=uid)
            return render(request, 'forget2.html', {'data': d[0]})
        else:
            return render(request, 'forget.html', {'msg': 'User ID not available'})

        
    else:
        return render(request, 'forget.html')



def forget2(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        ans = request.POST['ans']
        
        d = students.objects.filter(userid__exact=uid).filter(answer__exact=ans).count()
        if d > 0:
            d = students.objects.filter(userid__exact=uid)
            return render(request, 'forget3.html', {'data': d[0]})
        else:
            return render(request, 'forget.html', {'msg': 'Verification failed'})

        
    else:
        return render(request, 'forget.html')




def forget3(request):
    userid = request.POST['uid']
    password = request.POST['password']
    students.objects.filter(userid = userid).update(password = password)
    return render(request, 'user.html', {'msg': "Password updated !!"})

    


def userhomedef(request):
    if "userid" in request.session:
        uid = request.session["userid"]
        d = students.objects.filter(userid__exact=uid)
        c = categories.objects.all()

        msg = request.session["msg"]
        request.session["msg"] = ''
        d1=students.objects.filter(userid__exact=uid)
        I=d1[0].intrests
        print(I,'*******************')
        I= I.split(';')
        rec1=products.objects.filter(cat_name__in=I).filter(availability__gte=1).order_by('-id')[:5:1]

        d1=missing.objects.filter(userid__exact=uid)
        l1=[]

        for d11 in d1:
            print(d11.keywords,'^^^^^^^^^^^^^^^^^')
            rc1=products.objects.filter(keywords__icontains=d11.keywords).filter(availability__gte=1)
            l1.append(rc1)
        rec2=chain(l1)
        print(rec2)

        rec2=list(rec2)

        for r in rec2:
            for r1 in r:
                print(r1.name)

        rec3=products.objects.filter(availability__gte=1).order_by('-id')[:5:1]                

                
        



        return render(request, 'user_home.html', {'data': d[0], 'cat':c, 'msg':msg,'rec1':rec1,'rec2':rec2,'rec3':rec3})

    else:
        return render(request, 'user.html')


def userlogoutdef(request):
    try:
        del request.session['userid']
    except:
        pass
    return render(request, 'user.html')



def addcategory(request):
    d = categories.objects.all()
    c = categories.objects.all()
    return render(request, 'addcat.html', {'data': d, 'cat':c})


def addcataction(request):
    if request.method == 'POST':
        name = request.POST['name']
        d = categories.objects.filter(name__exact=name).count()
        if d > 0:
            d = categories.objects.all()
            return render(request, 'addcat.html', {'data': d, 'msg': "Duplicate Data"})

            
        else:
   
            d = categories(name=name)
            d.save()
    
            return redirect('addcategory')




def additem(request):
    
    d1=categories.objects.all()
    

    return render(request, 'additem.html',{'cat': d1})
 


def additemaction(request):
    if request.method == 'POST':
        userid = request.session['userid']
        sname = request.session['name']
        cat = request.POST['cat']
        desc = request.POST['desc']
        keywords = request.POST['keywords']
        stz = request.POST['stz']

        cat = cat.split("|")
        catname = cat[0]
        cid = cat[1]
        
        name = request.POST['name']
        cost = request.POST['cost']
        ava = request.POST['ava']
        image = request.FILES['itemimage']

        d = products(cat_id=cid, cat_name=catname, prod_name=name, description=desc, keywords=keywords, cost=cost, photo=image, availability=ava, sid=userid, stz=stz, name=sname)

        d.save()

    d1 = categories.objects.all()
    c = categories.objects.all()

    return render(request, 'additem.html', {'cat': d1, 'msg': 'Product Added !!','cat':c})



def uviewproducts(request, cid):
    if "userid" in request.session:
        cat = cid

        d = products.objects.filter(cat_id=cat).filter(availability__gte=1)
        pid=0
        for d1 in d:
            pid=d1.id
            break

        c = categories.objects.all()

        return render(request, 'uviewproducts.html', {'prod': d, 'cat': c, 'pid':pid})
    else:
        return redirect('userlogout')



def viewsingle(request, pid):
    if "userid" in request.session:
        pid = pid
        import random as r
        no = r.randint(1, 7)


        from .Dates import get
        ddate = get(no)

        d = products.objects.filter(id=pid)
        c = categories.objects.all()
        print(d[0].prod_name)


        l1=likes.objects.filter(feedback='like').filter(pid=pid).count()
        l2=likes.objects.filter(feedback='dislike').filter(pid=pid).count()
        l3=l1+l2

        return render(request, 'viewsingle.html', {'d': d[0], 'cat': c, 'l1':l1,'l2':l2,'l3':l3,})
    


    else:
        return redirect('userogout')



   
   
def addtocart(request):
    qua = request.POST['qua']
    userid = request.session['userid']
    pid = request.POST['pid']
    sid = request.POST['sid']
    
    d = products.objects.filter(id=pid)

    d2 = cart(userid=userid, pid=pid, prod_name=d[0].prod_name, unit_cost=float(d[0].cost), sid=sid, tot_cost=float(d[0].cost) * float(qua), photo=d[0].photo, quantity=qua)
    d2.save()
    request.session["msg"] = 'Product Added to Cart !!'
    return redirect('userhome')


def cartview(request):
    if "userid" in request.session:
        userid = request.session["userid"]

        d = cart.objects.filter(userid=userid)
        c = categories.objects.all()

        return render(request, 'cartview.html', {'cat': c, 'cart': d})
    else:
        return redirect('userlogout')


def cartdelete(request, op):
    if request.method == 'GET':

        pid = op
        d = cart.objects.filter(id=pid)
        print(d[0])
        d.delete()

        return redirect('cartview')
    else:
        pass





def payment(request):
    if request.method == 'POST':
        userid = request.session["userid"]

        d = cart.objects.filter(userid=userid)
        from .RandomGen import get
        oid = int(get())
        for d1 in d:
            d2 = orders(oid=oid, userid=userid, pid=d1.pid, prod_name=d1.prod_name, unit_cost=d1.unit_cost,
                        tot_cost=d1.tot_cost, photo=d1.photo,  quantity=d1.quantity, sid=d1.sid)
            d2.save()
            products.objects.filter(id=d1.pid).update(availability=F('availability') - d1.quantity)

        

        request.session["msg"] = 'Purchase Completed !!'
        
        d = cart.objects.filter(userid=userid)
        d.delete()
        
        
        
        return redirect('userhome')
    else:
        userid = request.session["userid"]
        d = cart.objects.filter(userid=userid)
        tot = 0.0
        b = True

        for d1 in d:
            tot = tot + d1.tot_cost
        c = categories.objects.all()



        return render(request, 'buy.html', {'tot': tot,'cat': c, 'b': b})




def vieworders(request):
    if "userid" in request.session:

        sid=request.session['userid']
        o = orders.objects.filter(sid=sid)
        c = categories.objects.all()
    
        return render(request, 'vieworders.html', {'o': o, 'cat': c})
    else:
        return redirect('userlogout')


def uvieworders(request):
    if "userid" in request.session:

        userid = request.session["userid"]

        d = orders.objects.filter(userid=userid).order_by('-id')
        c = categories.objects.all()

        return render(request, 'uvieworders.html', {'o': d, 'cat': c})
    else:
        return redirect('userlogout')


def viewalerts(request):
    if "userid" in request.session:
        userid = request.session["userid"]

        d = userrequests.objects.exclude(userid=userid)
        c = categories.objects.all()

        return render(request, 'viewalerts.html', {'cat': c, 'data': d})
    else:
        return redirect('userlogout')



def addrequest(request):
    if request.method == 'POST':
        desc = request.POST['desc']
        type = request.POST['type']
        userid = request.session["userid"]
        name = request.session["name"]
        d = userrequests(prodtype=type, description=desc, name=name, userid=userid)
        d.save()
        request.session["msg"] = 'Request Posted Successfully !!'
        return redirect('userhome')
    else:
        c = categories.objects.all()
        return render(request, 'addrequest.html', {'cat': c})



def addfeedback(request):
    if request.method == 'POST':
        feed = request.POST['feed']
        userid = request.session["userid"]
        name = request.session["name"]
        d = feedback(feedback=feed, name=name, userid=userid)
        d.save()
        request.session["msg"] = 'Feedback  Posted Successfully !!'
        return redirect('userhome')
    else:
        c = categories.objects.all()
        return render(request, 'addfeedback.html', {'cat': c})


def viewfeedback(request):
    if "adminid" in request.session:
        d = feedback.objects.all()

        return render(request, 'viewfeedback.html', { 'data': d})
    else:
        return redirect('userlogout')



def searchproducts(request):
    if "userid" in request.session:
        keys = request.POST['keys']
        userid = request.session["userid"]

        d = products.objects.filter(keywords__icontains=keys).filter(availability__gte=1).count()

        if d>0:
            d = products.objects.filter(keywords__icontains=keys).filter(availability__gte=1)
            c = categories.objects.all()
            return render(request, 'uviewproducts.html', {'prod': d, 'cat': c, 'msg':"Search Results"})
        else:
            d=missing(userid=userid, keywords=keys)
            d.save()
            request.session["msg"] = 'No products found !!'
            return redirect('userhome')
    else:
        return redirect('userlogout')




def chatpagestart(request):
    if request.method == 'POST':
        
        femail = request.POST['email']
        uid=request.session["email"]

        d=students.objects.filter(email = femail).count()
        if d>0 and femail!=uid:
            d=students.objects.filter(email = femail)
            name=d[0].name
            fname=name
            d1=friends(e_mail=uid, frnd_e=femail, frnd_n=fname)
            d1.save()
            d1=friends(e_mail=femail, frnd_e=uid, frnd_n=request.session["name"])
            d1.save()
            

        d=friends.objects.filter(e_mail__exact=uid)
        return render(request, 'chatpagestart.html',{'data': d})

    else:
        uid=request.session["email"]
        d=friends.objects.filter(e_mail__exact=uid)
        return render(request, 'chatpagestart.html',{'data': d})
        
def chatload(request):
    uid=request.session["email"]
    remail=request.GET["remail"]
    request.session["r_email"]=remail

    s1=uid+remail
    s2=remail+uid
    d = chat.objects.filter(Q(chatbw__icontains=s1)|Q(chatbw__icontains=s2)).all()
    return render(request, 'chat.html',{'data': d})
 

def chataction(request):
    message=request.POST['message']
    uemail=request.session["email"]
    remail=request.session["r_email"]
    uname=request.session["name"]
    s1=uemail+remail
    s2=remail+uemail
    d=chat(name=uname,email=uemail,chatbw=uemail+remail,message=message)
    d.save()
    d = chat.objects.filter(Q(chatbw__icontains=s1)|Q(chatbw__icontains=s2)).all()

    return render(request, 'chat.html',{'data': d})
    

def postlikes(request):
    pid=request.GET['pid']
    like=request.GET["like"]
    cat_name=request.GET["cat_name"]

    userid=request.session["userid"]
    d=likes(userid=userid,pid=pid,feedback=like)
    d.save()

    if like=='like':
        d=students.objects.filter(userid__exact=userid)
        for d1 in d:
            i=d1.intrests
            i=i.split(';')
            i.append(cat_name)
            i=set(i)
            s=''
            for i1 in i:
                s=s+i1+";"
            students.objects.filter(userid__exact = userid).update(intrests = s)


    d = products.objects.filter(id=pid)
    c = categories.objects.all()
    print(d[0].prod_name)





    l1=likes.objects.filter(feedback='like').filter(pid=pid).count()
    l2=likes.objects.filter(feedback='dislike').filter(pid=pid).count()
    l3=l1+l2





    return render(request, 'viewsingle.html', {'d': d[0], 'cat': c, 'l1':l1,'l2':l2,'l3':l3,})
    



