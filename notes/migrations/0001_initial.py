# Generated by Django 4.0.4 on 2022-05-24 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignants',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idens', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=80)),
                ('prenom', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=5)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('groupe', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Examens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idex', models.CharField(max_length=4)),
                ('titre', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('coefficient', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('examen', models.CharField(max_length=30)),
                ('etudiant', models.CharField(max_length=40)),
                ('note', models.CharField(max_length=30)),
                ('appreciation', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Ressouces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_ressource', models.CharField(max_length=30)),
                ('nom_ressource', models.CharField(max_length=60)),
                ('descriptif', models.CharField(max_length=30)),
                ('coefficient', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=30)),
                ('nom', models.CharField(max_length=50)),
                ('semestre', models.CharField(max_length=10)),
                ('ects', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enseignants', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.enseignants')),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.etudiant')),
                ('examens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.examens')),
                ('notes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.notes')),
                ('ressources', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.ressouces')),
                ('ue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notes.ue')),
            ],
        ),
    ]
