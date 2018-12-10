from django.http import HttpResponse
from .models import *
from django.shortcuts import render,redirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponseRedirect
import string
import random
import requests,json

global_name=None
global_studentid=None
global_ug=None
global_block=None
global_email=None
global_mobileno=None
global_id=None

#To authenicate Faculty,Worker login    

def login1(request):
	global global_id
	if request.method=='POST':
		
		try:
			x = user_details.objects.get(uid=request.POST['uid'])
			print(x.password)
		except(KeyError, user_details.DoesNotExist):
		
			template = loader.get_template('student/login.html')
			context = {
					'IDinvalid':"Invalid Username !",
				}
			return HttpResponse(template.render(context,request))
			
		if (request.POST['log']=='Login'):
			if request.POST['password'] != x.password:
				#PassWord is incorrect
				template = loader.get_template('student/login.html')
				context = {
						'Passwordinvalid':"Incorrect password!",
					}
				return HttpResponse(template.render(context,request))
				

			else:
				#Both UserID and Password are Correct
				k=x.did
				global_id=x.uid
				
				if k==1:
					#To open Faculty home page
					template = loader.get_template('faculty/facultyhome.html')
					context = {
						'current' : x
					}
					return HttpResponse(template.render(context,request))
				elif k==2:
					#To open Manger home page
					template = loader.get_template('manager/BH1.html')
					context = {
						'current' : x 
					}
					return HttpResponse(template.render(context,request))
				elif k==3:
					#To open Security home page
					template = loader.get_template('sworker/attendance.html')
					context = {
						'current' : x 
					}
					return HttpResponse(template.render(context,request))
		#Email is sent when you click forgot password			
		if (request.POST['log']=='Forgot Password'):
			print(x.email_id)
			#Random Password is generated
			paswd=''.join(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits) for _ in range(8))
			print(paswd)
			subject='New Password'
			message='THIS MESSAGE IS SENT TO GIVE YOU TEMPORARY PASSWORD FOR LOGIN. New Password :- '+paswd
			from_email=settings.EMAIL_HOST_USER
			to_list = [x.email_id]
			email1=EmailMessage(subject,message,from_email,to_list)
			email1.send(fail_silently=False)
			#Password is updated in database
			user_details.objects.filter(email_id=x.email_id).update(password=paswd)
			template = loader.get_template('student/login.html')
			context = {
					'Check your Email',
				}
			return HttpResponse(template.render(context,request))
			
def studenthome1(request,token_id):
	global global_studentid
	global global_name
	global global_email
	global global_mobileno
	global global_ug
	
	#get token id from api
	print("This is token id {}".format(token_id))
	payload={'token':token_id,
	'secret':"2528e298230fa89724afb0052609123ce1860d214531ccad33e2e24fdbb2078e8254e2206a79734161e2f8da103b31721ce17b876364859fe09057990beea34d"
	}
	url="https://serene-wildwood-35121.herokuapp.com/oauth/getDetails"
	response=requests.post(url,data=payload)
	data=response.json()
	print("Details from API:",data)
	print("************************",data['student'][0]['Student_ID'])
	global_studentid=data['student'][0]['Student_ID']
	global_name=data['student'][0]['Student_First_Name']
	global_email=data['student'][0]['Student_Email']
	global_mobileno=data['student'][0]['Student_Mobile']
	global_ug=data['student'][0]['Student_Cur_YearofStudy']
	return HttpResponseRedirect('/studenthome')


def managerhome(request):
	return render(request,'manager/managernotifications.html')

def studenthome(request):
	global global_studentid
	gp=student_service_details.objects.all().filter(uid__exact=global_studentid)
	print(gp)
	
	gp1=book_cab_details.objects.all().filter(uid__exact=global_studentid)
	print(gp1)
	
	gp2=laundry_details.objects.all().filter(uid__exact=global_studentid)
	print(gp2)
	
	context={"student_service_detailss":gp,"book_cab_detailss":gp1,"laundry_detailss":gp2}	
	
	return render(request,'student/studenthome.html',context)
    


def login(request):
	return render(request,'student/login.html')
    

def gate_pass(request):
	global global_studentid
	#get data from table and show in html page
	gp=gatepass.objects.all().filter(uid__exact=global_studentid)
	print(gp)
	context={"gatepasss":gp}
	return render(request,'student/gatepass.html',context)
    

def sservices(request):
	print("*************************")  
	return render(request,'student/sservices.html')
    
def complaint1(request):
	global global_studentid
	global global_name
	#get data from form and fill in database
	if request.method=='POST':
		stud=complaints()
		stud.uid=global_studentid
		stud.name=global_name
		stud.block="BH2"
		stud.room_no="518"
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		stud.complaint=request.POST['complaint']
		stud.save()
	#get data from table and show in html page	
	gp=complaints.objects.all().filter(uid__exact=global_studentid)
	print(gp)
	context={"complaintss":gp}
	return render(request,'student/complaint.html',context)
	
def complaint(request):
	global global_studentid
	#get data from table and show in html page
	gp=complaints.objects.all().filter(uid__exact=global_studentid)
	#queryset = StoreEvent.objects.filter(stores__user=request.user).order_by('-date')
	print(gp)
	context={"complaintss":gp}
	return render(request,'student/complaint.html',context)
    
def profile(request):
	global global_studentid
	global global_name
	global global_email
	global global_mobileno
	global global_ug
	
	context={"uid":global_studentid,"name":global_name,"email":global_email,"mobileno":global_mobileno,"ug":global_ug}
	
	return render(request,'student/profile.html',context)
    
    
def details(request):
	return render(request,'student/details.html')
    
def facultyhome(request):
	return render(request,'faculty/facultyhome.html')
 
def faculty_serviceshistory(request):
	global total
	
	gp=faculty_service_details.objects.all().filter(uid__exact=global_id).filter(status=0)
	gpc=cooking.objects.all().filter(uid__exact=global_id).filter(status=0)
	gpb=book_cab_details.objects.all().filter(uid__exact=global_id).filter(status=0).filter(block__exact="FB")
	gpl=laundry_details.objects.all().filter(uid__exact=global_id).filter(status=0)			
	gpm=medical_sevices.objects.all().filter(uid__exact=global_id).filter(status=0)			
	gpg=bring_groceries.objects.all().filter(uid__exact=global_id).filter(status=0)			
	gpn=notify_gate.objects.all().filter(uid__exact=global_id).filter(status=0)						
	
	context={"hos":gp,"cook":gpc,"cab":gpb,"laundry":gpl,"medical":gpm,"gro":gpg,"gate":gpn}
	return render(request,'faculty/faculty_serviceshistory.html',context)
 
def faculty_complaints(request):
	global global_id
	#get data from form and fill in database
	if request.method=='POST':
		print("***********************---",global_id)
		x = user_details.objects.all().filter(uid__exact=global_id)
			
		stud=complaints()
		stud.uid=x[0].uid
		stud.name=x[0].name
		stud.block="FB"
		stud.complaint=request.POST['complaint']
		stud.room_no=x[0].room_no
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid
		
		stud.save()
	gp=complaints.objects.all().filter(uid__exact=global_id).filter(status=0)
	print(gp)
	context={"com":gp}
	return render(request,'faculty/faculty_complaints.html',context)
 
def housekeeping(request):
	global global_id
	#get data from form and fill in database
	if request.method=='POST':

		x = user_details.objects.all().filter(uid__exact=global_id)
			
		stud=faculty_service_details()
		stud.uid=x[0].uid
		stud.name=x[0].name
		stud.room_no=x[0].room_no
		stud.date=request.POST['Date']
		stud.tm=request.POST['Time']
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid
		
		stud.save()
		
		
	return render(request,'faculty/facultyhome.html')
		 

def hkstatus(request):
	global global_id
	print("################################--my bad")
	#get data from form and fill in database
	if request.method=='POST':
		x=request.POST['uid']
		a=request.POST['wid']
		b=request.POST['status']
		print("*******************************************",a)
		t = faculty_service_details.objects.get(uid=x)
		print("*******************************************",t.status)
		t.assigned_worker_id = a
		t.status = b  # change field
		t.save() # this will update only
		
	return render(request,'manager/facultybuilding.html')

def cooking1(request):
	global global_id
	#get data from form and fill in database
	if request.method=='POST':

		x = user_details.objects.all().filter(uid__exact=global_id)
			
		stud=cooking()
		stud.uid=x[0].uid
		stud.name=x[0].name
		stud.room_no=x[0].room_no
		stud.date=request.POST['Date']
		stud.tm=request.POST['Time']
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid
		
		stud.save()
	
		
	return render(request,'faculty/facultyhome.html')
		 
def getgatepass(request):
	global global_studentid
	global global_name
	#get data from form and fill in database
	if request.method=='POST':
		
		stud=gatepass()
		stud.uid=global_studentid
		stud.name=global_name
		stud.from_date=request.POST['from_date']
		stud.to_date=request.POST['to_date']
		stud.purpose=request.POST['purpose']
		stud.to_palce=request.POST['to_place']
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		print(stud)
		stud.save()
	#get data from table and show in html page
	gp=gatepass.objects.all().filter(uid__exact=global_studentid)
	print(gp)
	context={"gatepasss":gp}	
		
	return render(request,'student/gatepass.html',context)
		

def bh1(request):
	gpl=laundry_details.objects.all().filter(block__exact="BH1").filter(status=0)
	ll=gpl.count()
	gph=student_service_details.objects.all().filter(room_no__exact="BH1").filter(status=0)
	lh=gph.count()
	gp=complaints.objects.all().filter(block__exact="BH1").filter(status=0)
	l=gp.count()
	gpm=medical_sevices.objects.all().filter(block__exact="BH1").filter(status=0)
	lm=gpm.count()
	gpb=book_cab_details.objects.all().filter(block__exact="BH1").filter(status=0)
	lb=gpb.count()
	context={"complaintss":gp,"lenght":l,"house":gph,"lenh":lh,"laundry":gpl,"lenl":ll,"medicalservice":gpm,"lenm":lm,"bookcab":gpb,"lenb":lb}
	return render(request,'manager/BH1.html',context)
	
def bh2(request):
	gpl=laundry_details.objects.all().filter(block__exact="BH2").filter(status=0)
	ll=gpl.count()
	gph=student_service_details.objects.all().filter(room_no__exact="BH2").filter(status=0)
	lh=gph.count()
	gp=complaints.objects.all().filter(block__exact="BH2").filter(status=0)
	l=gp.count()
	gpm=medical_sevices.objects.all().filter(block__exact="BH2").filter(status=0)
	lm=gpm.count()
	gpb=book_cab_details.objects.all().filter(block__exact="BH2").filter(status=0)
	lb=gpb.count()
	context={"complaintss":gp,"lenght":l,"house":gph,"lenh":lh,"laundry":gpl,"lenl":ll,"medicalservice":gpm,"lenm":lm,"bookcab":gpb,"lenb":lb}
	return render(request,'manager/BH2.html',context)

def gh1(request):
	gpl=laundry_details.objects.all().filter(block__exact="GH1").filter(status=0)
	
	ll=gpl.count()
	gph=student_service_details.objects.all().filter(room_no__exact="GH1").filter(status=0)
	lh=gph.count()
	gp=complaints.objects.all().filter(block__exact="GH1").filter(status=0)
	l=gp.count()
	gpm=medical_sevices.objects.all().filter(block__exact="GH1").filter(status=0)
	lm=gpm.count()
	gpb=book_cab_details.objects.all().filter(block__exact="GH1").filter(status=0)
	lb=gpb.count()
	context={"complaintss":gp,"lenght":l,"house":gph,"lenh":lh,"laundry":gpl,"lenl":ll,"medicalservice":gpm,"lenm":lm,"bookcab":gpb,"lenb":lb}
	return render(request,'manager/GH1.html',context)
	
def fbuilding(request):
	gpl=laundry_details.objects.all().filter(block__exact="FB").filter(status=0)
	ll=gpl.count()
	gph=faculty_service_details.objects.all().filter(status=0)
	lh=gph.count()
	gp=complaints.objects.all().filter(block__exact="FB").filter(status=0)
	l=gp.count()
	gpm=medical_sevices.objects.all().filter(block__exact="FB").filter(status=0)
	lm=gpm.count()
	gpb=book_cab_details.objects.all().filter(block__exact="FB").filter(status=0)
	lb=gpb.count()
	gpg=bring_groceries.objects.all().filter(status=0)
	lg=gpg.count()
	gpc=cooking.objects.all().filter(status=0)
	lc=gpc.count()
	context={"complaintss":gp,"lenght":l,"house":gph,"lenh":lh,"laundry":gpl,"lenl":ll,"medicalservice":gpm,"lenm":lm,"bookcab":gpb,"lenb":lb,"groceries":gpg,"lenG":lg,"cooking":gpc,"lenc":lc}
	return render(request,'manager/facultybuilding.html',context)
	
def attendance(request):
	#get data from table and show in html page
	gp1= notify_gate.objects.all().filter(status=0)
	
	gp=gatepass.objects.all()
	print(gp)
	context={"gatepasss":gp,"notifygates":gp1}
	return render(request,'sworker/attendance.html',context)
	
def addvisitor(request):
	varia=add_visitor.objects.all()
	context={"addvis":varia}
	return render(request,'sworker/addvisitor.html',context)

def in_out_details(request):
	if request.method=='POST':
		in_out_var=in_out()
		in_out_var.uid=request.POST['uid']
		in_out_var.name=request.POST['name']
		in_out_var.in_time=request.POST['time']
		in_out_var.purpose=request.POST['purpose']
		in_out_var.entry_created_by=log.objects.all()[0].uid
		in_out_var.last_modified_by=log.objects.all()[0].uid
		in_out_var.save()                
	return render(request,'sworker/attendance.html')
	
def in_out_history(request):
	tmp_var= in_out.objects.all().filter(in_time='0')
	context={"in_out_hstry":tmp_var}
	return render(request,'sworker/in_out1.html',context)

def stuhouse(request):
	global global_studentid
	global global_name
	#get data from form and fill in database
	if request.method=='POST':
		
		stud=student_service_details()
		stud.uid=global_studentid
		stud.name=global_name
		stud.room_no="BH1"
		stud.date=request.POST['date']
		
		stud.tm=request.POST['time']
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		stud.save()
	#get data from table and show in html page	
	gp=student_service_details.objects.all().filter(uid__exact=global_studentid)
	print(gp)
	context={"student_service_detailss":gp}	
	
	return render(request,'student/sservices.html',context)
	
def bookcab(request):
	global global_studentid
	global global_name
	#get data from form and fill in database
	if request.method=='POST':
		stud=book_cab_details()
		stud.uid=global_studentid
		stud.name=global_name		
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		#stud.block=log.objects.all()[0].working_block
		stud.block="GH1"
		stud.from_palce=request.POST['from_palce']
		stud.to_palce=request.POST['to_palce']
		stud.date=request.POST['date']
		
		stud.tm=request.POST['time']
		stud.date1=request.POST['date1']
		
		stud.time1=request.POST['time1']
		
		stud.save()
	#get data from table and show in html page	
	gp=book_cab_details.objects.all().filter(uid__exact=global_studentid)
	print(gp)
	context={"book_cab_detailss":gp}
	return render(request,'student/sservices.html',context)
def bookcab1(request):
	global global_id
	#get data from form and fill in database
	if request.method=='POST':
	
		x = user_details.objects.all().filter(uid__exact=global_id)	
		stud=book_cab_details()
		stud.uid=x[0].uid
		stud.name=x[0].name
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid

		stud.block="FB"
		stud.from_palce=request.POST['from_palce']
		stud.to_palce=request.POST['to_palce']
		stud.date=request.POST['date']
		
		stud.tm=request.POST['time']
		
		stud.save()
	
	return render(request,'faculty/facultyhome.html')

		
def laundry(request):
	global global_studentid

	#get data from form and fill in database
	if request.method=='POST':
		
		stud=laundry_details()
		stud.uid=global_studentid
		stud.name=global_name		
		stud.room_no=request.POST['room_no']
		stud.date=request.POST['date']
		stud.block=request.POST['block']
		stud.tm=request.POST['time']
		stud.no_of_trousers=request.POST['trousers']
		stud.no_of_shirts=request.POST['shirts']
		stud.no_of_kurties=request.POST['kurties']
		stud.no_of_salvars=request.POST['salvars']
		stud.no_of_leggins=request.POST['leggins']
		stud.other=request.POST['other']
		stud.total=stud.no_of_trousers+stud.no_of_shirts+stud.no_of_kurties+stud.no_of_salvars+stud.no_of_leggins+stud.other
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		stud.save()
	#get data from table and show in html page	
	gp=laundry_details.objects.all().filter(uid__exact=global_studentid)
	print(gp)
	context={"laundry_detailss":gp}	
	
	return render(request,'student/sservices.html',context)

def laundry1(request):
	global global_id
	
	#get data from form and fill in database
	if request.method=='POST':
		
		x = user_details.objects.all().filter(uid__exact=global_id)			
		stud=laundry_details()
		stud.uid=x[0].uid
		stud.name=x[0].name
		stud.room_no=request.POST['room_no']
		stud.date=request.POST['date']
		stud.block="FB"
		stud.tm=request.POST['time']
		stud.no_of_trousers=request.POST['trousers']
		stud.no_of_shirts=request.POST['shirts']
		stud.no_of_kurties=request.POST['kurties']
		stud.no_of_salvars=request.POST['salvars']
		stud.no_of_leggins=request.POST['leggins']
		stud.other=request.POST['other']
		stud.total=stud.no_of_trousers+stud.no_of_shirts+stud.no_of_kurties+stud.no_of_salvars+stud.no_of_leggins+stud.other
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid
		stud.save()
	#get data from table and show in html page	
		
	
	return render(request,'faculty/facultyhome.html')
def groceries(request):
	global global_id
	#get data from form and fill in database
	if request.method=='POST':
		
		x = user_details.objects.all().filter(uid__exact=global_id)			
		stud=bring_groceries()
		stud.uid=x[0].uid
		stud.name=x[0].name
		stud.room_no=x[0].room_no
		stud.date=request.POST['date']
		
		stud.description=request.POST['items']
		
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid
		stud.save()
	#get data from table and show in html page	
		
	
	return render(request,'faculty/facultyhome.html')


def notifygates(request):
	global global_studentid
	#get data from form and fill in database
	if request.method=='POST':
		
		stud=notify_gate()
		stud.uid=global_studentid
		stud.name_of_visitor=request.POST['name']
		stud.date_of_arrival=request.POST['date']
		stud.block="BH1"
		stud.mobile_no_of_visior=request.POST['mobno']
		
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		stud.save()
	#get data from table and show in html page	
	
	
	return render(request,'student/sservices.html')
def notifygates1(request):
	global global_id
	#get data from form and fill in database
	if request.method=='POST':
		
		x = user_details.objects.all().filter(uid__exact=global_id)	
		stud=notify_gate()
		stud.uid=x[0].uid
		stud.name_of_visitor=request.POST['name']
		stud.date_of_arrival=request.POST['date']
		stud.block="FB"
		stud.mobile_no_of_visior=request.POST['mobno']
		
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid
		stud.save()
	#get data from table and show in html page	
	
	
	return render(request,'faculty/facultyhome.html')
	
def addvisitor1(request):
	global global_studentid
	#get data from form and fill in database
	if request.method=='POST':
		
		stud=add_visitor()
		#stud.uid=global_studentid
		stud.name=request.POST['name']
		stud.mobile_no=request.POST['mobile_no']
		stud.purpose=request.POST['purpose']
		stud.address=request.POST['address']
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		stud.save()
	#get data from table and show in html page	
	'''gp=add_visitor.objects.all()
	print(gp)
	context={"add_visitors":gp}'''	
	varia= add_visitor.objects.all()
	context={"addvis":varia}
	return render(request,'sworker/addvisitor.html',context)

def medicalservice(request):
	global global_studentid
	#get data from form and fill in database
	if request.method=='POST':
		
		stud=medical_sevices()
		stud.uid=global_studentid
		stud.name=global_name
		stud.description=request.POST['description']
		stud.room_no='201'
		stud.block='BH1'
		stud.entry_created_by=global_studentid
		stud.last_modified_by=global_studentid
		stud.save()
	
	return render(request,'student/sservices.html')
     

	
def medicalservice1(request):
	global global_id
	#get data from form and fill in database
	if request.method=='POST':
				
		x = user_details.objects.all().filter(uid__exact=global_id)	
		
		stud=medical_sevices()
		stud.uid=x[0].uid
		stud.name=x[0].name
		stud.description=request.POST['description']
		stud.room_no=x[0].room_no
		stud.block=x[0].block
		stud.entry_created_by=x[0].uid
		stud.last_modified_by=x[0].uid
		stud.save()
	
	return render(request,'faculty/facultyhome.html')
	
	
def searchby_date(request):
	global global_studentid
	if request.method=='POST':
		
		
		stud_date=request.POST['date']
		
	gp1=laundry_details.objects.all().filter(uid__exact=global_studentid).filter(date__exact=stud_date)
	gp=student_service_details.objects.all().filter(uid__exact=global_studentid).filter(date__exact=stud_date)
	context={"laundry_detailss ":gp1,"student_service_detailss":gp}
	return render(request,'student/studenthome.html',context)
		
