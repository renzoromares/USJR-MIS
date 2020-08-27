# Generated by Django 3.0.8 on 2020-08-25 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Id_Number', models.IntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.TextField(max_length=50)),
                ('Last_Name', models.TextField(max_length=50)),
                ('Email', models.TextField(max_length=100)),
                ('Contact', models.BigIntegerField()),
                ('Password', models.CharField(max_length=20)),
                ('Employee_Picture', models.ImageField(null=True, upload_to='pictures')),
            ],
            options={
                'db_table': 'Employee',
            },
        ),
        migrations.CreateModel(
            name='TransacHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Transac_Type', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('Date', models.DateField(null=True)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'History',
            },
        ),
        migrations.CreateModel(
            name='Form',
            fields=[
                ('Form_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Type', models.CharField(max_length=50)),
                ('Date_Requested', models.DateField(null=True)),
                ('Date_Approved', models.DateField(null=True)),
                ('Status', models.CharField(max_length=20)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Form',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_ID', models.AutoField(primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=100)),
                ('College', models.CharField(max_length=100)),
                ('Status_Dept', models.TextField(max_length=100)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Department',
            },
        ),
    ]
