# Generated by Django 2.0.4 on 2018-05-03 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('server', '服务器'), ('pc', '个人电脑'), ('switchboard', '交换机'), ('router', '路由器'), ('printer', '打印机'), ('others', '其他')], default='server', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='groups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='组名')),
            ],
        ),
        migrations.CreateModel(
            name='hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(verbose_name='IP地址')),
                ('use_people', models.CharField(default=None, max_length=100, verbose_name='使用人')),
                ('use_begindate', models.DateField(default='2010-01-01', verbose_name='开始使用日期')),
                ('use_enddate', models.DateField(default='2100-01-01', null=True, verbose_name='结束使用日期')),
                ('use_note', models.TextField(default=None, null=True, verbose_name='备注')),
                ('use_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.assets')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passwd', models.CharField(max_length=255, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='邮箱')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='手机号')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='最近修改时间')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app2.groups')),
                ('name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
