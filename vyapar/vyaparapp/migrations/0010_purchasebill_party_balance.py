# Generated by Django 4.2.3 on 2023-11-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vyaparapp", "0009_rename_item_purchasebillitem_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchasebill",
            name="party_balance",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
