#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.utils.timezone import now
from datetime import datetime
from django.utils import timezone

#from django.core.urlresolvers import reverse
from django.urls import reverse


class Hdb(models.Model):
    ntext =models.CharField(max_length=20, null=True, blank =True)
    name_m =models.CharField(max_length=20, default ="")
    todayptno = models.IntegerField(default="",null=True, blank =True)
    gongdan = models.IntegerField(default="0", null=True, blank =True)
    jongham = models.IntegerField(default="0", null=True, blank =True)
    vaccine = models.IntegerField(default="0", null=True, blank =True)
    cashincome = models.IntegerField(default="0", null=True, blank =True)
    creditincome = models.IntegerField(default="0", null=True, blank =True)
    misu = models.IntegerField(default="0", null=True, blank =True)
    totalincome = models.IntegerField(default="0", null=True, blank =True)
    jichulcash = models.IntegerField(default="0", null=True, blank =True)
    cashremain = models.IntegerField(default="0", null=True, blank =True)
    cashsije = models.IntegerField(default="0", null=True, blank =True)
    
    jichulclass = models.CharField(max_length=120,default="없음", null=True, blank =True)
    jichulclass2 = models.CharField(max_length=120,default="", null=True, blank =True)
    jichulclass3 = models.CharField(max_length=120,default="", null=True, blank =True)
    jichulclass4 = models.CharField(max_length=120,default="", null=True, blank =True)
    jichulclass5 = models.CharField(max_length=120,default="", null=True, blank =True)
    jichulcontents =models.CharField(max_length=150,default="없음", null=True, blank =True)
    jichulcontents2 =models.CharField(max_length=120,default="", null=True, blank =True)
    jichulcontents3 = models.CharField(max_length=120,default="", null=True, blank =True)
    jichulcontents4 =models.CharField(max_length=120,default="", null=True, blank =True)
    jichulcontents5 = models.CharField(max_length=120,default="", null=True, blank =True)
    jichulmoney = models.IntegerField(default="0", null=True, blank =True)
    jichulmoney2 = models.IntegerField(default="", null=True, blank =True)
    jichulmoney3 = models.IntegerField(default="", null=True, blank =True)
    jichulmoney4 = models.IntegerField(default="", null=True, blank =True)
    jichulmoney5 = models.IntegerField(default="", null=True, blank =True)
    bigo  = models.CharField(max_length=100,default="-", null=True, blank =True)
    bigo2 = models.CharField(max_length=120,default="", null=True, blank =True)
    bigo3 = models.CharField(max_length=120,default="", null=True, blank =True)
    bigo4 = models.CharField(max_length=120,default="", null=True, blank =True)
    bigo5 = models.CharField(max_length=120,default="", null=True, blank =True)
    
    jichulsum = models.IntegerField(default="0", null=True, blank =True)
    guneu= models.CharField(max_length=200,default="없음", null=True, blank =True)
    guneu2= models.CharField(max_length=190,default="", null=True, blank =True)
    guneu3= models.CharField(max_length=190,default="", null=True, blank =True)
    guneu4= models.CharField(max_length=190,default="", null=True, blank =True)
    guneu5= models.CharField(max_length=190,default="", null=True, blank =True)
    
    dutyonoff = models.CharField(max_length=100,default="무", null=True, blank =True)
    dutyonoff2 = models.CharField(max_length=110,default="", null=True, blank =True)
    dutyonoff3 = models.CharField(max_length=110,default="", null=True, blank =True)
    dutyonoff4 = models.CharField(max_length=110,default="", null=True, blank =True)
    dutyonoff5 = models.CharField(max_length=110,default="", null=True, blank =True)
    
    created_date = models.DateTimeField(default=timezone.now)
    comments = models.CharField(max_length=100, default="없음", null=True, blank =True)
    
    def __str__(self):
        return self.ntext
        
    def get_absolute_url(self):
        
        #return reverse('dbbase:detail', args=[self.id])
        return reverse('detail', kwargs={'pk': self.pk})
        
   # @property
   # def sum_jichulmoney(self):
   #     if self.jichulmoney == "none":
   #         self.jichulmoney = 0
    #        sumjichul= self.jichulmoney 
            
    #    else:
   #         if self.jichulmoney2 =="none":
  #              self.jichulmoney2 =0
   #             sumjichul= self.jichulmoney + self.jichulmoney2
  #          else:
   #             if self.jichulmoney3 =="none":
  #                  self.jichulmoney3 =0
   #                 sumjichul= self.jichulmoney + self.jichulmoney2+ self.jichulmoney3
   #             else:
   #                 if self.jichulmoney4 =="none":
    #                    self.jichulmoney4 =0
   #                     sumjichul= self.jichulmoney + self.jichulmoney2+ self.jichulmoney3+ self.jichulmoney4
    #                else:
    #                    if self.jichulmoney5 =="none":
    #                        self.jichulmoney5 =0
     #                       sumjichul= self.jichulmoney + self.jichulmoney2+ self.jichulmoney3+ self.jichulmoney4+ self.jichulmoney5
     #                   else:
     #                       sumjichul= self.jichulmoney + self.jichulmoney2+ self.jichulmoney3+ self.jichulmoney4+ self.jichulmoney5
                    #sumjichul= self.jichulmoney + self.jichulmoney2 + self.jichulmoney3
            #sumjichul= self.jichulmoney + self.jichulmoney2 + self.jichulmoney3 
     #   return sumjichul
        
    @property   
    def sumdue(self)  :
        sd = self.cashincome - self.sum_jichul 
        #- self.jichulmoney
        
        return sd
    
    @property 
    def testsum(self):
        ts =self.jichulmoney + self.jichulmoney2
        return ts
        
    @property 
    def sumincome(self):
        ti =self.cashincome + self.creditincome + self.misu
        return ti
        
    @property
    def sum_jichul(self):
        j1= int(0 if self.jichulmoney is None else self.jichulmoney)
        j2= int(0 if self.jichulmoney2 is None else self.jichulmoney2)
        j3= int(0 if self.jichulmoney3 is None else self.jichulmoney3)
        j4= int(0 if self.jichulmoney4 is None else self.jichulmoney4)
        j5= int(0 if self.jichulmoney5 is None else self.jichulmoney5)
        
        sumjichul=  j1 + j2+ j3 +j4 + j5
        
        
        return sumjichul