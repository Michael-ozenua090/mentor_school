# Generated by Django 4.1 on 2022-10-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_score_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Lecturer'), (2, 'Student')], default=2),
        ),
    ]
