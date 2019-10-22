# Generated by Django 2.2.2 on 2019-10-15 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='missao',
            name='foiConcluida',
        ),
        migrations.AddField(
            model_name='missao',
            name='categoria',
            field=models.CharField(choices=[('Concluída', 'Concluída'), ('Inconcluída', 'Inconcluída')], default=2, max_length=12),
            preserve_default=False,
        ),
    ]