# Generated by Django 3.2.8 on 2021-10-24 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contributor', '0002_contributor_project_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributor',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to=settings.AUTH_USER_MODEL),
        ),
    ]
