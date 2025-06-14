# Generated by Django 5.1.6 on 2025-06-05 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Temat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=100)),
                ('poziom', models.CharField(choices=[('P', 'Początkujący'), ('Ś', 'Średniozaawansowany'), ('Z', 'Zaawansowany')], max_length=1)),
                ('osiagniecia', models.TextField()),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notatka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tresc', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('temat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nauka.temat')),
            ],
        ),
    ]
