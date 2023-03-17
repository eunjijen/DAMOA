# Generated by Django 4.1.7 on 2023-03-16 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_board_event_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="SummerNoteAttachment",
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
                (
                    "name",
                    models.CharField(
                        blank=True,
                        help_text="Defaults to filename, if left blank",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("uploaded", models.DateTimeField(auto_now_add=True)),
                ("file", models.FileField(upload_to="attachments/")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="board",
            name="event_date",
            field=models.DateTimeField(blank=True, null=True, verbose_name="모임일"),
        ),
    ]