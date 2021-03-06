# Generated by Django 3.2.9 on 2021-11-10 22:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogInstanceApp',
            fields=[
                ('app_log_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('log_instance_name', models.CharField(max_length=255)),
                ('start_app_time', models.DateTimeField()),
                ('end_app_time', models.DateTimeField(blank=True, default=None, null=True)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id_log', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('url_request', models.CharField(max_length=255, null=True)),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.CharField(max_length=15)),
                ('request_date', models.DateTimeField()),
                ('response_date', models.DateTimeField()),
                ('methods', models.CharField(max_length=10, null=True)),
                ('status_code', models.PositiveSmallIntegerField()),
                ('request_body', models.TextField()),
                ('response_body', models.TextField()),
                ('log_app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logService.loginstanceapp')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='logService.user')),
            ],
        ),
    ]
