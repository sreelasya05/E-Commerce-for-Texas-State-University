from django.db import models


# Create your models here.
class students(models.Model):
    name = models.CharField(max_length=100);
    email = models.CharField(max_length=100);
    phone = models.CharField(max_length=100);
    gender = models.CharField(max_length=100);
    userid=models.CharField(max_length=100);
    password = models.CharField(max_length=100);
    question = models.CharField(max_length=100);
    answer = models.CharField(max_length=1000);
    year = models.CharField(max_length=100);
    department = models.CharField(max_length=1000);
    intrests = models.CharField(max_length=1000);


class categories(models.Model):
    name = models.CharField(max_length=100);    

class userrequests(models.Model):
    userid = models.CharField(max_length=100);
    name = models.CharField(max_length=100);
    prodtype = models.CharField(max_length=100);    
    description = models.CharField(max_length=1000);
    
class feedback(models.Model):
    userid = models.CharField(max_length=100);
    name = models.CharField(max_length=100);
    feedback = models.CharField(max_length=1000);


class friends(models.Model):
    e_mail=models.CharField(max_length=149);
    frnd_e=models.CharField(max_length=149);
    frnd_n=models.CharField(max_length=149);


class chat(models.Model):
    name=models.CharField(max_length=100);
    email=models.CharField(max_length=100);
    chatbw=models.CharField(max_length=100);
    message=models.CharField(max_length=100);


class missing(models.Model):
    userid = models.CharField(max_length=100);
    keywords = models.CharField(max_length=100);
    

class products(models.Model):
    cat_id=models.CharField(max_length=10);
    cat_name=models.CharField(max_length=100);
    prod_name=models.CharField(max_length=100);
    description=models.CharField(max_length=5000);
    cost=models.FloatField(max_length=100);
    photo = models.CharField(max_length=500);
    availability=models.IntegerField();
    sid=models.CharField(max_length=500);
    email=models.CharField(max_length=500);
    name=models.CharField(max_length=500);
    keywords=models.CharField(max_length=1000);
    stz=models.CharField(max_length=500);
    

class cart(models.Model):
    userid=models.CharField(max_length=100);
    pid=models.CharField(max_length=10);
    prod_name=models.CharField(max_length=100);
    unit_cost=models.FloatField(max_length=100);
    tot_cost=models.FloatField(max_length=100);
    quantity=models.IntegerField();
    photo = models.CharField(max_length=500);
    sid=models.CharField(max_length=100);    

class orders(models.Model):
    oid=models.IntegerField();
    userid=models.CharField(max_length=100);
    pid=models.CharField(max_length=10);
    prod_name=models.CharField(max_length=100);
    unit_cost=models.FloatField(max_length=100);
    tot_cost=models.FloatField(max_length=100);
    photo = models.CharField(max_length=500);
    quantity=models.IntegerField();
    sid=models.CharField(max_length=100);


class likes(models.Model):
    pid = models.CharField(max_length=100);
    userid = models.CharField(max_length=100);
    feedback = models.CharField(max_length=100);

    






