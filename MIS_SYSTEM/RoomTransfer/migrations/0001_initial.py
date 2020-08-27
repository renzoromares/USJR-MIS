# Generated by Django 3.0.8 on 2020-08-27 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=50)),
                ('Date_Notify', models.DateField()),
                ('Subject', models.CharField(max_length=50)),
                ('Offer_Code', models.CharField(max_length=50)),
                ('Time_Day', models.CharField(max_length=50)),
                ('Room_From', models.CharField(max_length=50)),
                ('Room_To', models.CharField(max_length=50)),
                ('Date_Effective', models.DateField(null=True)),
                ('Reason', models.TextField(max_length=150)),
                ('timeSubmitted', models.TimeField(auto_now=True)),
                ('FormID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Form')),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'RoomTransfer',
            },
        ),
    ]
