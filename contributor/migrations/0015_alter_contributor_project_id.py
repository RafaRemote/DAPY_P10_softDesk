# Generated by Django 3.2.8 on 2021-11-04 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_alter_project_title'),
        ('contributor', '0014_alter_contributor_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contributor',
            name='project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributors', to='project.project'),
        ),
    ]