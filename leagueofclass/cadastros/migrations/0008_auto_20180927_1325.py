# Generated by Django 2.1.1 on 2018-09-27 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0007_auto_20180927_0339'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disciplinas',
            options={'verbose_name_plural': 'Disciplinas'},
        ),
        migrations.AlterModelOptions(
            name='notas',
            options={'verbose_name_plural': 'Notas'},
        ),
        migrations.AlterModelOptions(
            name='pessoa',
            options={'verbose_name_plural': 'Pessoas'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name_plural': 'Professores'},
        ),
    ]