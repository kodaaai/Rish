# Generated by Django 4.0.3 on 2022-07-11 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_alter_class_info_credit_num_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='opinion',
            field=models.CharField(max_length=500, verbose_name='コメント'),
        ),
    ]
