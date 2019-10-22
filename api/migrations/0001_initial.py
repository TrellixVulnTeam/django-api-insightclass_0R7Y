# Generated by Django 2.2.2 on 2019-10-15 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128)),
                ('media', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Missao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.TextField()),
                ('foiConcluida', models.BooleanField(default=False)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trofeu',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.TextField()),
                ('categoria', models.CharField(choices=[('Bronze', 'Bronze'), ('Prata', 'Prata'), ('Ouro', 'Ouro'), ('Diamante', 'Diamante'), ('Lenda', 'Lendária')], max_length=8)),
                ('img', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128)),
                ('prazo', models.DateField(null=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
                ('nota', models.DecimalField(decimal_places=2, max_digits=4)),
                ('isFeito', models.BooleanField(default=False)),
                ('tipo', models.CharField(choices=[('WEBAtividade', 'WEB-Atividade'), ('Prova', 'Prova'), ('Teste', 'Teste'), ('Relatório', 'Relatório'), ('Trabalho', 'Trabalho'), ('Outros', 'Outros')], max_length=14)),
                ('categoria', models.CharField(choices=[('G1', 'Grau 1'), ('G2', 'Grau 2')], max_length=2)),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(null=True)),
                ('aula1', models.BooleanField(default=False)),
                ('aula2', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Aluno')),
            ],
        ),
        migrations.CreateModel(
            name='Classificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicao', models.IntegerField()),
                ('pontuacao', models.DecimalField(decimal_places=2, max_digits=6)),
                ('aluno', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Aluno')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='trofeis',
            field=models.ManyToManyField(blank=True, related_name='trofeis', to='api.Trofeu'),
        ),
    ]
