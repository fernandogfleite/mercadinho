# Generated by Django 3.2.1 on 2021-05-06 18:56

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
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(default='', max_length=100)),
                ('value', models.FloatField()),
                ('category', models.CharField(blank=True, max_length=100)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produtos_idcategory_categorias', to='produtos.categoria')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='produtos_owner_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]