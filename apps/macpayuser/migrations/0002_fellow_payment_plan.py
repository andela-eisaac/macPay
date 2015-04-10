# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('macpayuser', '0001_initial'),
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fellow',
            name='payment_plan',
            field=models.ForeignKey(to='payment.PaymentPlan'),
            preserve_default=True,
        ),
    ]
