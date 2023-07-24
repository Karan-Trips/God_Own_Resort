from django.shortcuts import render,HttpResponseRedirect
import datetime
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import json as simplejson
from datetime import date
from datetime import datetime
import datetime
import webbrowser
import math, random 
import mysql.connector

def sendsms(ph,msg):
    sendToPhoneNumber= "+91"+ph
    userid = "2000022557"
    passwd = "54321@lcc"
    url = "http://enterprise.smsgupshup.com/GatewayAPI/rest?method=SendMessage&send_to" + sendToPhoneNumber + "&msg=" + msg + "&userid=" + userid + "&password=" + passwd + "&v=1.1&msg_type=TEXT&auth_scheme=PLAIN"
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)

def generateOTP() :   
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
        print(i)
    return OTP 

# Create your views here.

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='resort'
)


c = db.cursor()

def AdminHome(request):
    return render(request,'AdminHome.html') 

def CommonHome(request):
    return render(request,'CommonHome.html')

def CustomerHome(request):
    return render(request,'CustomerHome.html')

def ResortHome(request):
    return render(request,'ResortHome.html')

def SignIn(request):  
    request.session['username']=""
    request.session['NAME']=""
    request.session['cid']=""
    request.session['rid']=""
    msg=""
    if request.POST:
        email = request.POST.get("Username")
        password = request.POST.get("Password")
        c.execute("select * from login where uname='"+str( email )+"' and pass='"+str( password )+"'")
        ds = c.fetchone()
        request.session['username']=email
        if ds is not None:
            if ds[2] == 'Admin':
                return HttpResponseRedirect('/AdminHome/')
            elif ds[2] == 'Customer':
                c.execute("select * from cust_reg where email='"+str(email)+"' and password='"+str(password)+"'")
                ds = c.fetchone()
                request.session['cid'] = ds[0]
                request.session['curid'] = ds[0]
                request.session['NAME'] = ds[1]
                return HttpResponseRedirect('/CustomerHome/')
            elif ds[2] == 'Resort':
                c.execute("select * from resort_reg where email='"+str(email)+"' and password='"+str(password)+"'")
                ds = c.fetchone()
                request.session['curid'] = ds[0]
                request.session['rid'] = ds[0]
                print(ds[0])
                request.session['NAME'] = ds[1]
                return HttpResponseRedirect('/ResortHome/')
        else:
            msg="Incorrect Username or Password"
        
    return render(request,'Signin.html',{"msg":msg}) 

def CustomerSignUp(request):
    msg = ""
    if request.POST:
        cname = request.POST.get("name")
        address = request.POST.get("adrs")
        cntry = request.POST.get("cntry")
        state = request.POST.get("state")
        fon = request.POST.get("fon")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        type= "Customer"
        qry="insert into cust_reg(cname,address,country,state,phone,email,password) values('"+str( cname )+"','"+str( address )+"','"+str( cntry )+"','"+str( state )+"','"+str( fon )+"','"+str( email )+"','"+str( password )+"')"
        qr ="insert into login values('"+str( email )+"','"+str( password )+"','"+str( type )+"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        msg = "Registartion Completed Successfully."
    return render(request,'CustomerSignUp.html',{"msg":msg})

def ResortSignUp(request):
    msg = ""
    c.execute("select * from district")
    dist = c.fetchall()
    c.execute("select * from category")
    cat = c.fetchall()
    if request.POST:
        name = request.POST.get("name")
        adrs = request.POST.get("adrs")
        distr = request.POST.get("dist")
        loc = request.POST.get("loc")
        fon = request.POST.get("fon")
        ono = request.POST.get("ono")
        email = request.POST.get("email")
        cat = request.POST.get("cat")
        if request.FILES.get("file"):
            myfile=request.FILES.get("file")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
        passw = request.POST.get("pass")
        type= "Resort"
        qry="insert into resort_reg(name,address,district,location,mobile,officeno,email,category,rimage,password,r_status) values('"+str( name )+"','"+str( adrs )+"','"+str( distr )+"','"+str( loc )+"','"+str( fon )+"','"+str( ono )+"','"+str( email )+"','"+str(cat)+"','"+str(uploaded_file_url)+"','"+str(passw)+"','Registered')"
        qr ="insert into login values('"+str( email )+"','"+str( passw )+"','"+str( type )+"')"
        c.execute(qry)
        c.execute(qr)
        db.commit()
        msg = "Registration Completed Successfully."
    return render(request,'ResortSignUp.html',{"msg":msg,"dist":dist,"cat":cat})

def AdminAddCategory(request):
    msg=""
    if request.POST:
        na = request.POST.get("cat")
        qry="insert into categories(catname) values('"+str( na )+"')"
        c.execute(qry)
        db.commit()
        msg = "Category Added Successfully."
    c.execute("select * from categories")
    data=c.fetchall() 
    return render(request,'AdminAddCategory.html',{"data":data,"msg":msg})

def AdminRemoveCategory(request):
    if request.GET:
        a = request.GET.get('id')
        c.execute("delete from categories where catid = '"+str(a)+"'")
        db.commit()
        return HttpResponseRedirect("/AdminAddCategory/")
    return render(request,'AdminRemoveCategory.html')

def Admin_View_Customers(request):
    data = ""
    c.execute("select * from cust_reg")
    data=c.fetchall() 
    return render (request,"AdminViewCustomers.html",{"data":data})

def AdminViewResorts(request):
    data = ""
    c.execute("select * from resort_reg inner join district on resort_reg.district = district.did inner join category on resort_reg.category=category.catid where r_status = 'Registered'")
    data=c.fetchall() 
    if request.GET:
        rid = request.GET.get("id")
        st = request.GET.get("st")
        if st == 'Accept':
            c.execute("update resort_reg set r_status = '"+str(st)+"' where rid = '"+str(rid)+"'")
            db.commit()
            return HttpResponseRedirect("/AdminViewResorts/")
        else:
            c.execute("delete from resort_reg where rid = '"+str(rid)+"'")
            db.commit()
            return HttpResponseRedirect("/AdminViewResorts/")
    return render (request,"AdminViewResorts.html",{"data":data})

def AdminViewApprovedResorts(request):
    data = ""
    c.execute("select * from resort_reg inner join district on resort_reg.district = district.did inner join category on resort_reg.category=category.catid where r_status = 'Accept'")
    data=c.fetchall() 
    return render (request,"AdminViewApprovedResorts.html",{"data":data})

def AdminViewFeedback(request):
    data = ""
    c.execute("select * from cust_reg inner join feedback on cust_reg.cid = feedback.cid")
    data=c.fetchall() 
    return render (request,"AdminViewFeedback.html",{"data":data})
    
def ResortAddAccommodation(request):
    msg=""
    rid = request.session['rid']
    if request.POST:
        na = request.POST.get("room")
        de = request.POST.get("desc")
        ch = request.POST.get("price")
        if request.FILES.get("image"):
            myfile=request.FILES.get("image")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
        qry="insert into accomodation(rid,acname,descr,charge,image) values('"+str(rid)+"','"+str( na )+"','"+str(de)+"','"+str(ch)+"','"+str(uploaded_file_url)+"')"
        print(qry)
        c.execute(qry)
        db.commit()
        msg = "Details Added Successfully."
    return render(request,'ResortAddAccommodation.html',{"msg":msg})

def ResortAddDining(request):
    msg=""
    rid = request.session['rid']
    if request.POST:
        na = request.POST.get("room")
        de = request.POST.get("desc")
        ch = request.POST.get("price")
        if request.FILES.get("image"):
            myfile=request.FILES.get("image")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
        qry="insert into dining(rid,dname,ddesc,damt,image) values('"+str(rid)+"','"+str( na )+"','"+str(de)+"','"+str(ch)+"','"+str(uploaded_file_url)+"')"
        c.execute(qry)
        db.commit()
        msg = "Details Added Successfully."
    return render(request,'ResortAddDining.html',{"msg":msg})

def ResortAddHalls(request):
    msg=""
    rid = request.session['rid']
    if request.POST:
        na = request.POST.get("room")
        ti = request.POST.get("cap")
        ch = request.POST.get("area")
        amt = request.POST.get("amt")
        if request.FILES.get("image"):
            myfile=request.FILES.get("image")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
        qry="insert into hall(rid,hname,hcap,harea,hamt,himage) values('"+str(rid)+"','"+str( na )+"','"+str(ti)+"','"+str(ch)+"','"+str(amt)+"','"+str(uploaded_file_url)+"')"
        c.execute(qry)
        db.commit()
        msg = "Details Added Successfully."
    return render(request,'ResortAddHalls.html',{"msg":msg})

def ResortAddFacilities(request):
    msg=""
    rid = request.session['rid']
    if request.POST:
        na = request.POST.get("fname")
        if request.FILES.get("image"):
            myfile=request.FILES.get("image")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
        qry="insert into facility(rid,fname,fimage) values('"+str(rid)+"','"+str( na )+"','"+str(uploaded_file_url)+"')"
        c.execute(qry)
        db.commit()
        msg = "Details Added Successfully."
    return render(request,'ResortAddFacilities.html',{"msg":msg})

def ResortAddPackage(request):
    msg=""
    rid = request.session['rid']
    if request.POST:
        na = request.POST.get("pname")
        de = request.POST.get("desc")
        det = request.POST.get("details")
        day = request.POST.get("days")
        am = request.POST.get("price")
        if request.FILES.get("image"):
            myfile=request.FILES.get("image")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
        qry="insert into package(rid,pname,pdesc,details,night,amount,image) values('"+str(rid)+"','"+str( na )+"','"+str(de)+"','"+str(det)+"','"+str(day)+"','"+str(am)+"','"+str(uploaded_file_url)+"')"
        print(qry)
        c.execute(qry)
        db.commit()
        msg = "Details Added Successfully."
    return render(request,'ResortAddPackage.html',{"msg":msg})

def ResortAddAyurvedha(request):
    msg=""
    rid = request.session['rid']
    if request.POST:
        na = request.POST.get("pname")
        de = request.POST.get("desc")
        am = request.POST.get("price")
        days = request.POST.get("days")
        if request.FILES.get("image"):
            myfile=request.FILES.get("image")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            uploaded_file_url = fs.url(filename)
        qry="insert into ayurvedha(rid,aname,adesc,amount,days,image) values('"+str(rid)+"','"+str( na )+"','"+str(de)+"','"+str(am)+"','"+str(days)+"','"+str(uploaded_file_url)+"')"
        c.execute(qry)
        db.commit()
        msg = "Details Added Successfully."
    return render(request,'ResortAddAyurvedha.html',{"msg":msg})

def ResortAddHomepage(request):
    msg=""
    rid = request.session['rid']
    if request.POST:
        na = request.POST.get("at")
        if request.FILES.get("af"):
            myfile=request.FILES.get("af")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            af = fs.url(filename)
        de = request.POST.get("dt")
        if request.FILES.get("df"):
            myfile=request.FILES.get("df")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            df = fs.url(filename)
        ti = request.POST.get("ht")
        if request.FILES.get("hf"):
            myfile=request.FILES.get("hf")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            hf = fs.url(filename)
        ayt = request.POST.get("ayt")
        if request.FILES.get("ayf"):
            myfile=request.FILES.get("ayf")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            ayuf = fs.url(filename)
        pat = request.POST.get("pat")
        if request.FILES.get("paf"):
            myfile=request.FILES.get("paf")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            pacf = fs.url(filename)
        ch = request.POST.get("pt")
        if request.FILES.get("pf"):
            myfile=request.FILES.get("pf")
            fs=FileSystemStorage()
            filename=fs.save(myfile.name , myfile)
            pf = fs.url(filename)
        qry="insert into homepage(rid,accotitle,aimage,dintitle,dimage,haltitle,himage,aytitle,ayimage,packtitle,packimage,patitle,pimage) values('"+str(rid)+"','"+str( na )+"','"+str(af)+"','"+str(de)+"','"+str(df)+"','"+str(ti)+"','"+str(hf)+"','"+str(ayt)+"','"+str(ayuf)+"','"+str(pat)+"','"+str(pacf)+"','"+str(ch)+"','"+str(pf)+"')"
        c.execute(qry)
        db.commit()
        msg = "Details Added Successfully."
    return render(request,'ResortAddHomepage.html',{"msg":msg})

def ResortViewAccoBooking(request):
    rid = request.session["curid"]
    c.execute("select * from accomodation inner join acco_booking on accomodation.acid = acco_booking.roomid inner join cust_reg on cust_reg.cid = acco_booking.cid where accomodation.rid = '"+str(rid)+"' and acco_booking.status = 'Booked'")
    data = c.fetchall()
    if request.GET:
        reid = request.GET.get('id')
        st = request.GET.get('st')
        fo = request.GET.get('fo')
        if st == 'Accept':
            c.execute("update acco_booking set status='Accept' where abid = '"+str(reid)+"'")
            db.commit()
            msg ="Greetings.. Your Accommodation Booking was successfully approved"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewAccoBooking/')
        else:
            c.execute("delete from acco_booking where abid = '"+str(reid)+"'")
            db.commit()
            msg ="Sorry.. Your Accommodation Booking was rejected"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewAccoBooking/')
    return render(request,"ResortViewAccoBooking.html",{"data":data})

def ResortViewDiningBooking(request):
    rid = request.session["curid"]
    c.execute("select * from dining inner join dining_booking on dining.dinid = dining_booking.rest inner join cust_reg on cust_reg.cid = dining_booking.cid where dining.rid = '"+str(rid)+"' and dining_booking.status = 'Booked'")
    data = c.fetchall()
    if request.GET:
        reid = request.GET.get('id')
        st = request.GET.get('st')
        fo = request.GET.get('fo')
        if st == 'Accept':
            c.execute("update dining_booking set status='Accept' where dbid = '"+str(reid)+"'")
            db.commit()
            msg ="Greetings.. Your Restaurant Booking was successfully approved"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewDiningBooking/')
        else:
            c.execute("delete from dining_booking where dbid = '"+str(reid)+"'")
            db.commit()
            msg ="Sorry.. Your Restaurant Booking was rejected"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewDiningBooking/')
    return render(request,"ResortViewDiningBooking.html",{"data":data})

def ResortViewEventBooking(request):
    rid = request.session["curid"]
    c.execute("select * from hall inner join hall_booking on hall.hid = hall_booking.hid inner join cust_reg on cust_reg.cid = hall_booking.cid where hall.rid = '"+str(rid)+"' and hall_booking.status = 'Booked'")
    data = c.fetchall()
    if request.GET:
        reid = request.GET.get('id')
        st = request.GET.get('st')
        fo = request.GET.get('fo')
        if st == 'Accept':
            c.execute("update hall_booking set status='Accept' where hbid = '"+str(reid)+"'")
            db.commit()
            msg ="Greetings.. Your Accommodation Booking was successfully approved"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewEventBooking/')
        else:
            c.execute("delete from hall_booking where hbid = '"+str(reid)+"'")
            db.commit()
            msg ="Sorry.. Your Accommodation Booking was rejected"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewEventBooking/')
    return render(request,"ResortViewEventBooking.html",{"data":data})

def ResortViewPackageBooking(request):
    rid = request.session["curid"]
    c.execute("select * from package inner join package_booking on package.pid = package_booking.pid inner join cust_reg on cust_reg.cid = package_booking.cid where package.rid = '"+str(rid)+"' and package_booking.status = 'Booked'")
    data = c.fetchall()
    if request.GET:
        reid = request.GET.get('id')
        st = request.GET.get('st')
        fo = request.GET.get('fo')
        if st == 'Accept':
            c.execute("update package_booking set status='Accept' where pbid = '"+str(reid)+"'")
            db.commit()
            msg ="Greetings.. Your Package Booking was successfully approved"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewPackageBooking/')
        else:
            c.execute("delete from package_booking where pbid = '"+str(reid)+"'")
            db.commit()
            msg ="Sorry.. Your Package Booking was rejected"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewPackageBooking/')
    return render(request,"ResortViewPackageBooking.html",{"data":data})

def ResortViewAyurBooking(request):
    rid = request.session["curid"]
    c.execute("select * from ayurvedha inner join ayur_booking on ayurvedha.aid = ayur_booking.aid inner join cust_reg on cust_reg.cid = ayur_booking.cid where ayurvedha.rid = '"+str(rid)+"' and ayur_booking.status = 'Booked'")
    data = c.fetchall()
    if request.GET:
        reid = request.GET.get('id')
        st = request.GET.get('st')
        fo = request.GET.get('fo')
        if st == 'Accept':
            c.execute("update ayur_booking set status='Accept' where aybid = '"+str(reid)+"'")
            db.commit()
            msg ="Greetings.. Your Ayurvedha Booking was successfully approved"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewAyurBooking/')
        else:
            c.execute("delete from ayur_booking where aybid = '"+str(reid)+"'")
            db.commit()
            msg ="Sorry.. Your Ayurvedha Booking was rejected"
            sendsms(fo,msg)
            return HttpResponseRedirect('/ResortViewAyurBooking/')
    return render(request,"ResortViewAyurBooking.html",{"data":data})

def CustomerSearchResorts(request):
    c.execute("select * from district")
    dist = c.fetchall()
    c.execute("select * from category")
    cat = c.fetchall()
    data=""
    if 'distb' in request.POST:
        di = request.POST.get('dist')
        c.execute("select * from resort_reg where district = '"+str(di)+"'")
        data = c.fetchall()
    if 'catb' in request.POST:
        di = request.POST.get('cat')
        c.execute("select * from resort_reg where category = '"+str(di)+"'")
        data = c.fetchall()
    if request.GET:
        return HttpResponseRedirect("/CustomerViewResortHome/")
    return render(request,'CustomerSearchResorts.html',{"dist":dist,"cat":cat,"data":data})

def CustomerViewResortHome(request):
    rid = request.GET.get('id')
    request.session["curid"] = rid
    c.execute("select * from homepage where rid = '"+str(rid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortHome.html",{"data":data})

def CustomerViewResortAccommodation(request):
    rid = request.session["curid"]
    request.session['crid'] = rid
    print(rid)
    c.execute("select * from accomodation where rid = '"+str(rid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortAccommodation.html",{"data":data})

def CustomerViewResortAccoDetails(request):
    aid = request.GET.get('id')
    c.execute("select * from accomodation where acid = '"+str(aid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortAccoDetails.html",{"data":data})

def CustomerBookResortAccommodation(request):
    aid = request.GET.get('id')
    import datetime
    ct = str(datetime.date.today())
    request.session['acid'] = aid
    msg=""
    c.execute("select * from accomodation where acid = '"+str(aid)+"'")
    data = c.fetchall()
    if data:
        acname = data[0][2]
        amount = data[0][4]
    if request.POST:
        rid = request.session['rid']
        cid = request.session['cid']
        roomid = request.session['acid']
        cin = request.POST.get('checkin')
        cout = request.POST.get('checkout')
        import datetime
        d1 = datetime.datetime.strptime(cin, "%Y-%m-%d")
        d2 = datetime.datetime.strptime(cout, "%Y-%m-%d")
        difference= abs((d2 - d1).days)
        totam = difference*int(amount)
        num = request.POST.get('num')
        c.execute("insert into acco_booking(rid,cid,roomid,checkin,checkout,numroom,totamt,status)values('"+str(rid)+"','"+str(cid)+"','"+str(roomid)+"','"+str(cin)+"','"+str(cout)+"','"+str(num)+"','"+str(totam)+"','Booked')")
        db.commit()
        msg="Booking completed successfully. Please wait for the confirmation"
    return render(request,"CustomerBookResortAccommodation.html",{"data":data,"acname":acname,'ct':ct,"msg":msg})

def CustomerViewResortDining(request):
    did = request.session["curid"]
    c.execute("select * from dining where rid = '"+str(did)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortDining.html",{"data":data})

def CustomerViewResortDiningDetails(request):
    aid = request.GET.get('id')
    request.session['did'] =aid
    c.execute("select * from dining where dinid = '"+str(aid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortDiningDetails.html",{"data":data})

def CustomerBookResortDining(request):
    aid = request.GET.get('id')
    msg=""
    ct = str(datetime.date.today())
    c.execute("select * from dining where dinid = '"+str(aid)+"'")
    data = c.fetchall()
    if data:
        diname = data[0][2]
        amount = data[0][4]
    if request.POST:
        rid = request.session['rid']
        cid = request.session['cid']
        did = request.session['did']
        cin = request.POST.get('checkin')
        guest = request.POST.get('guest')
        time = request.POST.get('time')
        totam = int(guest)*int(amount)
        c.execute("insert into dining_booking(rid,cid,rest,guest,bdate,dbook,time,amount,status)values('"+str(rid)+"','"+str(cid)+"','"+str(did)+"','"+str(guest)+"','"+str(cin)+"','"+str(ct)+"','"+str(time)+"','"+str(totam)+"','Booked')")
        db.commit()
        msg="Booking completed successfully. Please wait for the confirmation"
    return render(request,"CustomerBookResortDining.html",{"data":data,'ct':ct,"diname":diname,"msg":msg})

def CustomerViewResortEvents(request):
    did = request.session["curid"]
    c.execute("select * from hall where rid = '"+str(did)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortEvents.html",{"data":data})

def CustomerViewResortEventsDetails(request):
    aid = request.GET.get('id')
    request.session['hid'] =aid
    c.execute("select * from hall where hid = '"+str(aid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortEventsDetails.html",{"data":data})

def CustomerBookResortEvents(request):
    aid = request.GET.get('id')
    msg=""
    ct = str(datetime.date.today())
    c.execute("select * from hall where hid = '"+str(aid)+"'")
    data = c.fetchall()
    if data:
        hname = data[0][2]
        amount = data[0][5]
    if request.POST:
        rid = request.session['rid']
        cid = request.session['cid']
        hid = request.session['hid']
        cin = request.POST.get('checkin')
        c.execute("insert into hall_booking(rid,cid,hid,bdate,dbook,amount,status)values('"+str(rid)+"','"+str(cid)+"','"+str(hid)+"','"+str(cin)+"','"+str(ct)+"','"+str(amount)+"','Booked')")
        db.commit()
        msg="Booking completed successfully. Please wait for the confirmation"
    return render(request,"CustomerBookResortEvents.html",{"data":data,'ct':ct,"hname":hname,"msg":msg})

def CustomerViewResortAyurvedha(request):
    rid = request.session["curid"]
    request.session['rid'] = rid
    c.execute("select * from ayurvedha where rid = '"+str(rid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortAyurvedha.html",{"data":data})

def CustomerViewResortAyurDetails(request):
    aid = request.GET.get('id')
    c.execute("select * from ayurvedha where aid = '"+str(aid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortAyurDetails.html",{"data":data})

def CustomerBookResortAyurvedha(request):
    aid = request.GET.get('id')
    import datetime
    ct = str(datetime.date.today())
    request.session['ayid'] = aid
    msg=""
    c.execute("select * from ayurvedha where aid = '"+str(aid)+"'")
    data = c.fetchall()
    if data:
        ayname = data[0][2]
    if request.POST:

        rid = request.session['rid']
        cid = request.session['cid']
        roomid = request.session['ayid']
        cin = request.POST.get('checkin')
        c.execute("insert into ayur_booking(rid,cid,aid,checkin,dbook,status)values('"+str(rid)+"','"+str(cid)+"','"+str(roomid)+"','"+str(cin)+"','"+str(ct)+"','Booked')")
        db.commit()
        msg="Booking completed successfully. Please wait for the confirmation"
    return render(request,"CustomerBookResortAyurvedha.html",{"data":data,"ayname":ayname,'ct':ct,"msg":msg})

def CustomerViewResortPackage(request):
    rid = request.session["curid"]
    request.session['crid'] = rid
    c.execute("select * from package where rid = '"+str(rid)+"'")
    data = c.fetchall()
    print(data)
    return render(request,"CustomerViewResortPackage.html",{"data":data})

def CustomerViewResortPackageDetails(request):
    aid = request.GET.get('id')
    c.execute("select * from package where pid = '"+str(aid)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortPackageDetails.html",{"data":data})

def CustomerBookResortPackage(request):
    aid = request.GET.get('id')
    import datetime
    ct = str(datetime.date.today())
    request.session['pcid'] = aid
    msg=""
    c.execute("select * from package where pid = '"+str(aid)+"'")
    data = c.fetchall()
    if data:
        pcname = data[0][2]
    if request.POST:
        rid = request.session['crid']
        cid = request.session['cid']
        roomid = request.session['pcid']
        cin = request.POST.get('checkin')
        c.execute("insert into package_booking(rid,cid,pid,cdate,dbook,status)values('"+str(rid)+"','"+str(cid)+"','"+str(roomid)+"','"+str(cin)+"','"+str(ct)+"','Booked')")
        db.commit()
        msg="Booking completed successfully. Please wait for the confirmation"
    return render(request,"CustomerBookResortPackage.html",{"data":data,"acname":pcname,'ct':ct,"msg":msg})

def CustomerViewResortFacilities(request):
    did = request.session["curid"]
    c.execute("select * from facility where rid = '"+str(did)+"'")
    data = c.fetchall()
    return render(request,"CustomerViewResortFacilities.html",{"data":data})

def CustomerViewPaymentNotification(request):
    if request.POST:
        ser = request.POST.get('ser')
        if ser == 'Accommodation':
            return HttpResponseRedirect("/CustomerViewAccoPayment/")
        if ser == 'Restaurant':
            return HttpResponseRedirect("/CustomerViewDiningPayment/")
        if ser == 'Events':
            return HttpResponseRedirect("/CustomerViewEventPayment/")
        if ser == 'Package':
            return HttpResponseRedirect("/CustomerViewPackagePayment/")
        if ser == 'Ayurvedha':
            return HttpResponseRedirect("/CustomerViewAyurPayment/")
    return render(request,"CustomerViewPaymentNotification.html")

def CustomerViewAccoPayment(request):
    cid = request.session["cid"]
    c.execute("select * from accomodation inner join acco_booking on accomodation.acid = acco_booking.roomid inner join cust_reg on cust_reg.cid = acco_booking.cid where cust_reg.cid = '"+str(cid)+"' and acco_booking.status = 'Accept'")
    data = c.fetchall()
    if request.GET:
        abid= request.GET.get('id')
        st = request.GET.get('st')
        am = request.GET.get('am')
        request.session["pay"] = am
        if st == 'Paid':
            c.execute("update acco_booking set status = 'Paid' where abid = '"+str(abid)+"'")
            db.commit()
            return HttpResponseRedirect("/payment1/")
        else:
            c.execute("delete from acco_booking where pbid = '"+str(abid)+"'")
            db.commit()
            return HttpResponseRedirect("/CustomerViewAccoPayment/")
    return render(request,"CustomerViewAccoPayment.html",{"data":data})

def CustomerViewDiningPayment(request):
    cid = request.session["cid"]
    c.execute("select * from dining inner join dining_booking on dining.dinid = dining_booking.rest inner join cust_reg on cust_reg.cid = dining_booking.cid where cust_reg.cid = '"+str(cid)+"' and dining_booking.status = 'Accept'")
    data = c.fetchall()
    if request.GET:
        dbid= request.GET.get('id')
        st = request.GET.get('st')
        am = request.GET.get('am')
        request.session["pay"] = am
        if st == 'Paid':
            c.execute("update dining_booking set status = 'Paid' where dbid = '"+str(dbid)+"'")
            db.commit()
            return HttpResponseRedirect("/payment1/")
        else:
            c.execute("delete from dining_booking where dbid = '"+str(dbid)+"'")
            db.commit()
            return HttpResponseRedirect("/CustomerViewDiningPayment/")
    return render(request,"CustomerViewDiningPayment.html",{"data":data})

def CustomerViewEventPayment(request):
    cid = request.session["cid"]
    c.execute("select * from hall inner join hall_booking on hall.hid = hall_booking.hid inner join cust_reg on cust_reg.cid = hall_booking.cid where cust_reg.cid = '"+str(cid)+"' and hall_booking.status = 'Accept'")
    data = c.fetchall()
    if request.GET:
        hbid= request.GET.get('id')
        st = request.GET.get('st')
        am = request.GET.get('am')
        request.session["pay"] = am
        if st == 'Paid':
            c.execute("update hall_booking set status = 'Paid' where hbid = '"+str(hbid)+"'")
            db.commit()
            return HttpResponseRedirect("/payment1/")
        else:
            c.execute("delete from hall_booking where hbid = '"+str(hbid)+"'")
            db.commit()
            return HttpResponseRedirect("/CustomerViewEventPayment/")
    return render(request,"CustomerViewEventPayment.html",{"data":data})

def CustomerViewPackagePayment(request):
    cid = request.session["cid"]
    c.execute("select * from package inner join package_booking on package.pid = package_booking.pid inner join cust_reg on cust_reg.cid = package_booking.cid where cust_reg.cid = '"+str(cid)+"' and package_booking.status = 'Accept'")
    data = c.fetchall()
    if request.GET:
        pbid= request.GET.get('id')
        st = request.GET.get('st')
        am = request.GET.get('am')
        request.session["pay"] = am
        if st == 'Paid':
            c.execute("update package_booking set status = 'Paid' where pbid = '"+str(pbid)+"'")
            db.commit()
            return HttpResponseRedirect("/payment1/")
        else:
            c.execute("delete from package_booking where pbid = '"+str(pbid)+"'")
            db.commit()
            return HttpResponseRedirect("/CustomerViewPackagePayment/")
    return render(request,"CustomerViewPackagePayment.html",{"data":data})

def CustomerViewAyurPayment(request):
    cid = request.session["cid"]
    c.execute("select * from ayurvedha inner join ayur_booking on ayurvedha.aid = ayur_booking.aid inner join cust_reg on cust_reg.cid = ayur_booking.cid where cust_reg.cid = '"+str(cid)+"' and ayur_booking.status = 'Accept'")
    data = c.fetchall()
    if request.GET:
        ayurid= request.GET.get('id')
        st = request.GET.get('st')
        am = request.GET.get('am')
        request.session["pay"] = am
        if st == 'Paid':
            c.execute("update ayur_booking set status = 'Paid' where aybid = '"+str(ayurid)+"'")
            db.commit()
            return HttpResponseRedirect("/payment1/")
        else:
            c.execute("delete from ayur_booking where aybid = '"+str(ayurid)+"'")
            db.commit()
            return HttpResponseRedirect("/CustomerViewAyurPayment/")
    return render(request,"CustomerViewAyurPayment.html",{"data":data})

def CustomerAddFeedback(request):
    msg=""
    cid = request.session['cid']  
    if request.POST:
        a=request.POST.get("room")
        b = date.today()
        c.execute("insert into feedback(cid,feedback,fdate) values('"+str(cid)+"','"+str(a)+"','"+str(b)+"')")
        db.commit()
        msg = "Feedback Added Successfully."
    return render(request,"CustomerAddFeedback.html",{"msg":msg})

def payment1(request):
    if request.POST:
        card=request.POST.get("test")
        request.session["card"]=card
        cardno=request.POST.get("cardno")
        request.session["card_no"]=cardno
        pinno=request.POST.get("pinno")
        request.session["pinno"]=pinno
        return HttpResponseRedirect("/payment2")
    return render(request,"payment1.html")

def payment2(request):
    cno=request.session["card_no"]
    amount=request.session["pay"]
    if request.POST:
        return HttpResponseRedirect("/payment3")
    return render(request,"payment2.html",{"cno":cno,"amount":amount})

def payment3(request):
    return render(request,"payment3.html")

def payment4(request):
    return render(request,"payment4.html")

def payment5(request):
    cno=request.session["card_no"]
    today = date.today()
    name =  request.session['NAME'] 
    amount = request.session["pay"]
    return render(request,"payment5.html",{"cno":cno,"today":today,"name":name,"amount":amount})




#Updations  13-07-2021#
# Accomadation##
def resortviewaccomadation(request):
    print(request.session['rid'])
    x="select * from  accomodation where rid='"+str(request.session['rid'])+"'"
    c.execute(x)
    data = c.fetchall()
    print(data)
    if request.GET.get("delete"):
        delete=request.GET.get("delete")
        x="delete from accomodation where acid='"+str(delete)+"'"
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/rcv")
    
        #return render(request,"rcvupdate.html",{"data":d1})
        #return HttpResponseRedirect("/rvaupdate")

        
    return render(request,"resortviewaccomadation.html",{"data":data})

def rvaupdate(request):
    if request.GET.get("update"):
        update=request.GET.get("update")
        request.session["update"]=update
        x="select * from accomodation where acid='"+str(update)+"'"
        c.execute(x)
        print("*"*50)
        d1=c.fetchone()
        print(d1)
        print("*"*50)
        a=request.session["update"]
    if request.POST:
        print("helloooooooooooooooooooooooooooooooooooooo")
        na = request.POST.get("room")
        de = request.POST.get("desc")
        ch = request.POST.get("price")
        print(na,de,ch)
        x="update accomodation set acname='"+str(na)+"',descr='"+str(de)+"',charge='"+str(ch)+"' where acid='"+str(a)+"'"
        print(x)
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/rcv")
    return render(request,"rcvupdate.html",{"data":d1})

#----------accomadation--------#
# dinining
def resortviewdining(request):
    print(request.session['rid'])
    x="select * from  dining where rid='"+str(request.session['rid'])+"'"
    c.execute(x)
    data = c.fetchall()
    print(data)
    if request.GET.get("delete"):
        delete=request.GET.get("delete")
        x="delete from dining where dinid='"+str(delete)+"'"
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewdining")
    
        #return render(request,"rcvupdate.html",{"data":d1})
        #return HttpResponseRedirect("/rvaupdate")

        
    return render(request,"rvdining.html",{"data":data})

def rvdupdate(request):
    if request.GET.get("update"):
        update=request.GET.get("update")
        request.session["update"]=update
        x="select * from dining where dinid='"+str(update)+"'"
        c.execute(x)
        print("*"*50)
        d1=c.fetchone()
        print(d1)
        print("*"*50)
        a=request.session["update"]
    if request.POST:
        print("helloooooooooooooooooooooooooooooooooooooo")
        na = request.POST.get("room")
        de = request.POST.get("desc")
        ch = request.POST.get("price")
        print(na,de,ch)
        x="update dining set dname='"+str(na)+"',ddesc='"+str(de)+"',damt='"+str(ch)+"' where dinid='"+str(a)+"'"
        print(x)
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewdining")
    return render(request,"rvdupdate.html",{"data":d1})
#########################dining Ended############################
# Ayurvedha
def resortviewayur(request):
    print(request.session['rid'])
    x="select * from  ayurvedha where rid='"+str(request.session['rid'])+"'"
    c.execute(x)
    data = c.fetchall()
    print(data)
    if request.GET.get("delete"):
        delete=request.GET.get("delete")
        x="delete from ayurvedha where aid='"+str(delete)+"'"
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewayur")
    
        #return render(request,"rcvupdate.html",{"data":d1})
        #return HttpResponseRedirect("/rvaupdate")

        
    return render(request,"resortviewayur.html",{"data":data})

def rvayurupdate(request):
    if request.GET.get("update"):
        update=request.GET.get("update")
        request.session["update"]=update
        x="select * from ayurvedha where aid='"+str(update)+"'"
        c.execute(x)
        print("*"*50)
        d1=c.fetchone()
        print(d1)
        print("*"*50)
        a=request.session["update"]
    if request.POST:
        print("helloooooooooooooooooooooooooooooooooooooo")
        na = request.POST.get("room")
        de = request.POST.get("desc")
        ch = request.POST.get("price")
        d = request.POST.get("days")

        print(na,de,ch)
        x="update ayurvedha set aname='"+str(na)+"',adesc='"+str(de)+"',amount='"+str(ch)+"',days='"+str(d)+"' where aid='"+str(a)+"'"
        print(x)
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewayur")
    return render(request,"rvayurupdate.html",{"data":d1})

#############################ayurended####################


# Ayurvedha
def resortviewhall(request):
    print(request.session['rid'])
    x="select * from  hall where rid='"+str(request.session['rid'])+"'"
    c.execute(x)
    data = c.fetchall()
    print(data)
    if request.GET.get("delete"):
        delete=request.GET.get("delete")
        x="delete from hall where hid='"+str(delete)+"'"
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewhall")
    
        #return render(request,"rcvupdate.html",{"data":d1})
        #return HttpResponseRedirect("/rvaupdate")

        
    return render(request,"resortviewhall.html",{"data":data})

def rvhallupdate(request):
    if request.GET.get("update"):
        update=request.GET.get("update")
        request.session["update"]=update
        x="select * from hall where hid='"+str(update)+"'"
        c.execute(x)
        print("*"*50)
        d1=c.fetchone()
        print(d1)
        print("*"*50)
        a=request.session["update"]
    if request.POST:
        print("helloooooooooooooooooooooooooooooooooooooo")
        na = request.POST.get("room")
        de = request.POST.get("desc")
        ch = request.POST.get("price")
        d = request.POST.get("days")

        print(na,de,ch)
        x="update hall set hname='"+str(na)+"',hcap='"+str(de)+"',harea='"+str(ch)+"',hamt='"+str(d)+"' where hid='"+str(a)+"'"
        print(x)
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewhall")
    return render(request,"rvhallupdate.html",{"data":d1})

#############################ayurended####################
#ended#

# Ayurvedha
def resortviewpackage(request):
    print(request.session['rid'])
    x="select * from  package where rid='"+str(request.session['rid'])+"'"
    c.execute(x)
    data = c.fetchall()
    print(data)
    if request.GET.get("delete"):
        delete=request.GET.get("delete")
        x="delete from package where pid='"+str(delete)+"'"
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewpackage")
    
        #return render(request,"rcvupdate.html",{"data":d1})
        #return HttpResponseRedirect("/rvaupdate")

        
    return render(request,"resortviewpackage.html",{"data":data})

def rvpackageupdate(request):
    if request.GET.get("update"):
        update=request.GET.get("update")
        request.session["update"]=update
        x="select * from package where pid='"+str(update)+"'"
        c.execute(x)
        print("*"*50)
        d1=c.fetchone()
        print(d1)
        print("*"*50)
        a=request.session["update"]
    if request.POST:
        print("helloooooooooooooooooooooooooooooooooooooo")
        na = request.POST.get("room")
        de = request.POST.get("desc")
        ch = request.POST.get("price")
        d = request.POST.get("days")

        print(na,de,ch)
        x="update package set pname='"+str(na)+"',pdesc='"+str(de)+"',details='"+str(ch)+"',amount='"+str(d)+"' where pid='"+str(a)+"'"
        print(x)
        c.execute(x)
        db.commit()
        return HttpResponseRedirect("/resortviewpackage")
    return render(request,"rvpackageupdate.html",{"data":d1})
