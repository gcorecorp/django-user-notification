# Generated by Django 3.2.12 on 2022-07-28 03:41

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
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='Title')),
                ('mark', models.CharField(blank=True, db_index=True, max_length=64, null=True, verbose_name='Message Mark')),
                ('msg_type', models.CharField(db_index=True, max_length=64, verbose_name='Message Type')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('render_kwargs', models.JSONField(blank=True, null=True, verbose_name='Render Kwargs')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
            options={
                'verbose_name': 'Message',
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='MessageTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Template Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('code', models.CharField(max_length=4, unique=True, verbose_name='Template Code')),
                ('title', models.CharField(blank=True, max_length=64, null=True, verbose_name='Message Title')),
                ('content', models.TextField(verbose_name='Template Content')),
                ('backend_kwargs', models.JSONField(blank=True, null=True, verbose_name='Backend Kwargs')),
                ('message_kwargs', models.JSONField(blank=True, null=True, verbose_name='Message Kwargs')),
            ],
            options={
                'verbose_name': 'Message Template',
                'db_table': 'message_template',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_read', models.BooleanField(default=False, verbose_name='Read Or Not')),
                ('is_ignored', models.BooleanField(default=False, verbose_name='Ignored Or Not')),
                ('push_state', models.PositiveIntegerField(choices=[(0, 'Pending'), (1, 'Success'), (2, 'Failure')], default=0)),
                ('notify_kwargs', models.JSONField(blank=True, null=True, verbose_name='Notify Kwargs')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='notification.message', verbose_name='Message')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Receiver')),
            ],
            options={
                'verbose_name': 'Notification',
                'db_table': 'notification',
            },
        ),
        migrations.AddField(
            model_name='message',
            name='template',
            field=models.ForeignKey(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='notification.messagetemplate', verbose_name='Template'),
        ),
    ]
