# Generated by Django 3.2.3 on 2021-06-02 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='indentifyshoppingcar',
            name='price',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='indentifyshoppingcar',
            name='shoppingcar',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='produtos.shoppingcar'),
        ),
    ]
