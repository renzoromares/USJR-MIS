# Generated by Django 3.0.8 on 2020-08-05 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='risograph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Department', models.CharField(max_length=100)),
                ('Time_in', models.TimeField()),
                ('Time_out', models.TimeField()),
                ('Paper_Type', models.CharField(max_length=50)),
                ('No_of_Copies', models.IntegerField()),
                ('Size', models.CharField(max_length=50)),
                ('File', models.ImageField(null=True, upload_to='pictures')),
                ('Acetate', models.CharField(max_length=50)),
                ('Id_Number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.Employee')),
            ],
            options={
                'db_table': 'Risograph',
            },
        ),
    ]
