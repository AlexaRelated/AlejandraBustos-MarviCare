# Generated by Django 5.0.6 on 2024-06-25 19:50

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='Anonymous', max_length=100),
            preserve_default=False,
        ),
    ]