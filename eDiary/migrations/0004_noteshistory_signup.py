# Generated by Django 3.1.1 on 2022-05-27 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eDiary', '0003_notes_signup'),
    ]

    operations = [
        migrations.AddField(
            model_name='noteshistory',
            name='signup',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eDiary.signup'),
        ),
    ]