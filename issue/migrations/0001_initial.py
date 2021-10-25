# Generated by Django 3.2.8 on 2021-10-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('tag', models.CharField(choices=[('BUG', 'bug'), ('IMPROVEMENT', 'improvement'), ('TASK', 'task')], default=None, max_length=100)),
                ('priority', models.CharField(choices=[('LOW', 'low'), ('AVERAGE', 'average'), ('HIGH', 'high')], default=None, max_length=100)),
                ('status', models.CharField(choices=[('TO_DO', 'to_do'), ('IN_PROGRESS', 'in_progress'), ('DONE', 'done')], default=None, max_length=100)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
