# Generated by Django 3.0.3 on 2020-03-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('userName', models.CharField(max_length=100)),
                ('emailAddress', models.CharField(max_length=100)),
                ('instituition', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('discipline', models.CharField(max_length=100)),
                ('userType', models.CharField(choices=[('Author', 'Author'), ('Editor', 'Editor'), ('Reviewer', 'Reviewer')], max_length=100)),
            ],
        ),
    ]
