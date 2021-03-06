# Generated by Django 4.0.1 on 2022-02-01 17:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserContacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=25)),
                ('nickname', models.CharField(blank=True, max_length=25)),
                ('gender', models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'Female')], max_length=1)),
                ('address', models.CharField(blank=True, max_length=125)),
                ('phone_number', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foruser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['firstname', 'lastname'],
            },
        ),
    ]
