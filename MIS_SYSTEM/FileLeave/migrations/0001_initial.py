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
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_Status', models.CharField(max_length=20)),
                ('Designation', models.CharField(max_length=100)),
                ('Typeof_Leave', models.CharField(max_length=30)),
                ('Date_Start', models.DateField()),
                ('Date_End', models.DateField()),
                ('Period_Days', models.IntegerField()),
                ('Reason', models.TextField(max_length=100)),
                ('Image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('timeSubmitted', models.TimeField(auto_now=True)),
                ('FormID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Form')),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Leave',
            },
        ),
    ]
