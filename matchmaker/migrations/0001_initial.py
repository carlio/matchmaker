# Generated by Django 2.0.6 on 2018-06-28 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Instrument",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("label", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name="Market",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("side_a", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="markets_by_side_a", to="matchmaker.Instrument")),
                ("side_b", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="markets_by_side_b", to="matchmaker.Instrument")),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("placed_at", models.DateTimeField(auto_now_add=True)),
                ("side", models.SmallIntegerField(choices=[(1, "buy"), (2, "sell")])),
                ("price", models.DecimalField(decimal_places=5, max_digits=10)),
                ("total_quantity", models.DecimalField(decimal_places=5, max_digits=10)),
                ("filled_quantity", models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ("market", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="matchmaker.Market")),
            ],
        ),
    ]
