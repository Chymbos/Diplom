# Generated by Django 3.1 on 2020-09-28 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Товар на складе',
                'verbose_name_plural': 'Товары на складе',
            },
        ),
    ]
