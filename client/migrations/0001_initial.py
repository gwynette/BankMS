# Generated by Django 3.2.16 on 2022-11-06 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_num', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=19)),
                ('account_type', models.CharField(choices=[('C', 'Chequing'), ('S', 'Saving')], default='C', max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
