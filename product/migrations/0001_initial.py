# Generated by Django 5.0.4 on 2024-04-09 06:44

import django.db.models.deletion
import django_ckeditor_5.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', django_ckeditor_5.fields.CKEditor5Field()),
                ('category', models.ImageField(upload_to='images')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.CharField(choices=[('in stock', 'В наличии'), ('out_of_stock', 'Нет в наличии')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
