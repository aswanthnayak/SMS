from django.urls import path,re_path
from django.conf.urls import include,url             
from . import views
from .views import *


urlpatterns = [

	url(r'^login1$',views.login1,name="login1"),
	url(r'^callback/(?P<token_id>.+)$',views.studenthome1,name="studenthome1"),
	url(r'^managernotifications',views.managerhome,name="managerhome"),
	url(r'^studenthome',views.studenthome),
	url(r'^login',views.login),
	path('', views.login, name='login'),		
	url(r'^gatepass',views.gate_pass),
	url(r'^sservices',views.sservices),
	url(r'^complaint1$',views.complaint1,name="complaint1"),	
	url(r'^complaint',views.complaint),
	url(r'^profile',views.profile),
	url(r'^details',views.details),
	
	#Faculty Pages
	url(r'^facultyhome',views.facultyhome),
	url(r'^faculty_serviceshistory',views.faculty_serviceshistory),
	url(r'^faculty_complaints',views.faculty_complaints),
	url(r'^complaint2$',views.faculty_complaints,name="complaint2"),	
	url(r'^housekeeping$',views.housekeeping,name="housekeeping"),
	#API Home Page
	url(r'^hkstatus$',views.hkstatus,name="hkstatus"),

	url(r'^cooking1$',views.cooking1,name="cooking1"),	
	url(r'^getgatepass$',views.getgatepass,name="getgatepass"),
	
	#For Forms


	
	#Manager Pages

	url(r'^BH1',views.bh1),
	url(r'^BH2',views.bh2),
	url(r'^GH1',views.gh1),
	url(r'^facultybuilding',views.fbuilding),
	
	url(r'^attendance',views.attendance),
	url(r'^addvisitor',views.addvisitor),
	
	url(r'^in_out$',views.in_out_details,name="in_out"),
	url(r'^in_out1',views.in_out_history),
	
	url(r'^stuhouse$',views.stuhouse,name="stuhouse"),		
	
	url(r'^bookcab$',views.bookcab,name="bookcab"),
	url(r'^bookcab1$',views.bookcab1,name="bookcab1"),
		
	url(r'^laundry$',views.laundry,name="laundry"),
	url(r'^laundry1$',views.laundry1,name="laundry1"),
	
	url(r'^groceries$',views.groceries,name="groceries"),	
			
	url(r'^notifygates$',views.notifygates,name="notifygates"),
	url(r'^notifygates1$',views.notifygates1,name="notifygates1"),	
		
	url(r'^addvisitor1$',views.addvisitor1,name="addvisitor1"),

	url(r'^medical$',views.medicalservice,name="medical"),
	url(r'^medical1$',views.medicalservice1,name="medical1"),	
	#
	url(r'^searchby_date$',views.searchby_date,name="searchby_date"),	




	
]

