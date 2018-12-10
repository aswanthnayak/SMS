from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class user_details(models.Model):
	did = models.IntegerField()
	uid = models.CharField(max_length=15,default=None)
	name= models.CharField(max_length=30,default=None)
	mobile_no=models.CharField(max_length=30,default=None)
	password=models.CharField(max_length=15,default=None)
	email_id = models.EmailField(max_length=30,default="abc@gmail.com")
	room_no  = models.CharField(max_length=5,default=None,null=True)
	blood_group = models.CharField(max_length=5,default=None)
	block=models.CharField(max_length=5,default=None)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)

class student_attendance(models.Model):
	uid=models.CharField(max_length=15,default=None)
	block=models.CharField(max_length=5,default=None)
	name= models.CharField(max_length=30,default=None)
	date= models.CharField(max_length=30,default=None)
	room_no  = models.CharField(max_length=5,default=None,null=True)
	presence = models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)

	
class in_out(models.Model):
	uid=models.CharField(max_length=15,default=None)
	
	name= models.CharField(max_length=30,default=None)
	in_time=models.CharField(max_length=30,default=None)
	out_time=models.CharField(max_length=30,default='0')
	purpose=models.CharField(max_length=100,default=None,null=True)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
                
class add_visitor(models.Model):
	
	name= models.CharField(max_length=30,default=None)
	mobile_no=models.CharField(max_length=30,default=None)
	address = models.CharField(max_length=100,default=None)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)

	
class gatepass(models.Model):
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)
	from_date=models.DateTimeField(default=datetime.now())
	to_date=models.DateTimeField(default=datetime.now())
	to_palce=models.CharField(max_length=15,default=None)
	purpose=models.CharField(max_length=100,default=None)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
       
class student_service_details(models.Model):
	#did=models.IntegerField()
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)
	room_no=models.CharField(max_length=10,default='BH1')
	date=models.CharField(max_length=15,default=None)
	tm=models.CharField(max_length=15,default=None)
	assigned_worker_name=models.CharField(max_length=15,default=None,null=True)
	worker_assigned_time=models.DateTimeField(default=datetime.now())
	work_completed_time=models.DateTimeField(default=datetime.now())
	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)

class laundry_details(models.Model):
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)	
	room_no=models.CharField(max_length=10,default=None) 
	date=models.CharField(max_length=15,default=None)
	tm=models.CharField(max_length=15,default=None)
	block=models.CharField(max_length=5,default=None)
	no_of_shirts=models.IntegerField(default=0)
	no_of_trousers=models.IntegerField(default=0)
	no_of_kurties=models.IntegerField(default=0)
	no_of_salvars=models.IntegerField(default=0)
	no_of_leggins=models.IntegerField(default=0)
	others=models.IntegerField(default=0)
	total=models.IntegerField(default=0)
	assigned_worker_name=models.CharField(max_length=15,null=True,default=None)
	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
       
class faculty_service_details(models.Model):
	
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)	
	room_no=models.CharField(max_length=10,default=None,null=True)
	date=models.CharField(max_length=15,default=None)
	tm=models.CharField(max_length=15,default=None)
	assigned_worker_name=models.CharField(max_length=15,default=None,null=True)
	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
      
class cooking(models.Model):
	
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)	
	room_no=models.CharField(max_length=10,default=None,null=True)
	date=models.CharField(max_length=15,default=None)
	tm=models.CharField(max_length=15,default=None)
	assigned_worker_name=models.CharField(max_length=15,default=None,null=True)
	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
      
class book_cab_details(models.Model):
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)	
	from_palce=models.CharField(max_length=15,default=None)
	to_palce=models.CharField(max_length=15,default=None)
	date=models.CharField(max_length=15,default=None)
	tm=models.CharField(max_length=15,default=None)
	block=models.CharField(max_length=5,default=None)
	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)

class notify_gate(models.Model):
	uid=models.CharField(max_length=15,default=None)
	name_of_visitor=models.CharField(max_length=30,default=None)
	mobile_no_of_visior=models.CharField(max_length=30,default=None)
	date_of_arrival=models.DateTimeField(default=datetime.now())
	block=models.CharField(max_length=5,default=None)
	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
      
class bring_groceries(models.Model):
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)	
	room_no=models.CharField(max_length=10,default=None,null=True)
	description=models.CharField(max_length=200,default=None)
	date=models.CharField(max_length=15,default=None)

	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
      
class medical_sevices(models.Model):
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)	
	room_no=models.CharField(max_length=10,default=None,null=True)
	block=models.CharField(max_length=10,default=None)
	
	description=models.CharField(max_length=100,default=None)
	status=models.IntegerField(default=0)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)
      
class complaints(models.Model):
	uid=models.CharField(max_length=15,default=None)
	name=models.CharField(max_length=30,default=None)	
	block=models.CharField(max_length=10,default=None)
	room_no=models.CharField(max_length=10,default=None,null=True)
	status=models.IntegerField(default=0)
	complaint=models.CharField(max_length=200,default=None)
	entry_created_time=models.DateTimeField(default=datetime.now())
	entry_created_by=models.CharField(max_length=30,default=None,null=True)
	entry_last_modified_time=models.DateTimeField(default=datetime.now())
	entry_last_modified_by=models.CharField(max_length=30,default=None,null=True)


      
