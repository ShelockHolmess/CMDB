# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.admin import User
# Create your models here.
class groups(models.Model):
    name = models.CharField('组名',max_length=100)
    def __unicode__(self):
        return self.name
class users(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    passwd = models.CharField('密码',max_length=255,null=False)
    email = models.EmailField('邮箱',null=True)
    phone = models.CharField('手机号',max_length=11,null=True)
    create_date = models.DateTimeField('创建时间', auto_now_add=True)
    update_date = models.DateTimeField('最近修改时间', auto_now=True)
    group = models.ForeignKey('groups',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class assets(models.Model): #资产
    choice = (
        ( 'server','服务器'),
        ('pc','个人电脑'),
        ('switchboard','交换机'),
        ('router','路由器'),
        ('printer','打印机'),
        ('others','其他')
    )
    name = models.CharField(choices=choice,default='server',max_length=100)
    def __str__(self):
        return self.name
class hosts(models.Model):
    ip = models.GenericIPAddressField('IP地址')
    use_people = models.CharField('使用人',max_length=100,default=None,null=False)
    use_place = models.ForeignKey('assets',on_delete=models.CASCADE)
    use_begindate = models.DateField('开始使用日期',default='2010-01-01',null=False)
    use_enddate = models.DateField('结束使用日期',default='2100-01-01',null=True)
    use_note = models.TextField('备注',default=None,null=True)
    def __str__(self):
        return self.ip
