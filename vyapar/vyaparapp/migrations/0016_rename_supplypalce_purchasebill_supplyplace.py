# Generated by Django 4.2.3 on 2023-11-17 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vyaparapp", "0015_remove_purchasebillitem_hsn_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="purchasebill", old_name="supplypalce", new_name="supplyplace",
        ),
    ]
