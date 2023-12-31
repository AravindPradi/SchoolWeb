# Generated by Django 4.2.4 on 2023-11-13 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JoinForm",
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
                ("name", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("dob", models.DateField()),
                ("phone", models.CharField(max_length=15)),
                ("address", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "department",
                    models.CharField(
                        choices=[
                            ("commerce", "Commerce"),
                            ("science", "Science"),
                            ("arts", "Arts"),
                        ],
                        max_length=50,
                    ),
                ),
                ("course", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "purpose",
                    models.CharField(
                        choices=[
                            ("enquiry", "For Enquiry"),
                            ("order", "Place Order"),
                            ("return", "Return"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Material",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(name="Team",),
        migrations.AddField(
            model_name="joinform",
            name="materials_provide",
            field=models.ManyToManyField(to="app.material"),
        ),
    ]
