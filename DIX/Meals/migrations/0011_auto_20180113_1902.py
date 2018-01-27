# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meals', '0010_auto_20180113_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meals',
            name='image',
            field=models.ImageField(default=b'/static/jpg/', upload_to=b'/static/jpg/'),
        ),
    ]
