# Generated by Django 3.0.3 on 2021-04-25 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobfair_app', '0005_auto_20210425_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='jobfair_app.Project'),
        ),
    ]