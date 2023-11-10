# Generated by Django 4.2.3 on 2023-11-10 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("vyaparapp", "0010_auto_20231106_0956"),
    ]

    operations = [
        migrations.CreateModel(
            name="PurchaseBill",
            fields=[
                (
                    "billid",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="BILLID"
                    ),
                ),
                ("partyname", models.CharField(max_length=100)),
                ("email", models.CharField(default="", max_length=100)),
                ("billno", models.CharField(max_length=100)),
                ("billdate", models.DateField()),
                ("duedate", models.DateField()),
                ("address", models.CharField(default="", max_length=255)),
                ("supplystate", models.CharField(default="", max_length=100)),
                ("pay_method", models.CharField(default="", max_length=255, null=True)),
                ("cheque_no", models.CharField(default="", max_length=255, null=True)),
                ("upi_no", models.CharField(default="", max_length=255, null=True)),
                ("bank_no", models.CharField(default="", max_length=255, null=True)),
                ("subtotal", models.IntegerField(default=0, null=True)),
                ("igst", models.CharField(default=0, max_length=100, null=True)),
                ("cgst", models.CharField(default=0, max_length=100, null=True)),
                ("sgst", models.CharField(default=0, max_length=100, null=True)),
                ("taxamount", models.CharField(default=0, max_length=100, null=True)),
                ("adjust", models.CharField(default=0, max_length=100, null=True)),
                ("grandtotal", models.FloatField(default=0, null=True)),
                ("advance", models.CharField(blank=True, max_length=255, null=True)),
                ("balance", models.CharField(blank=True, max_length=255, null=True)),
                ("tot_inv_no", models.IntegerField(default=0, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vyaparapp.company",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseBillItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item", models.CharField(max_length=100)),
                ("hsn", models.CharField(max_length=100)),
                ("qty", models.IntegerField(default=0, null=True)),
                ("price", models.CharField(max_length=100)),
                ("total", models.IntegerField(default=0, null=True)),
                ("tax", models.CharField(max_length=100)),
                ("discount", models.CharField(default=0, max_length=100, null=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vyaparapp.company",
                    ),
                ),
                (
                    "purchasebill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vyaparapp.purchasebill",
                    ),
                ),
            ],
        ),
    ]
