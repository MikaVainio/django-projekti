# Generated by Django 3.2.7 on 2021-10-25 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todomanager', '0004_tehtava_tehty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nimi', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='tehtava',
            name='kategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='todomanager.kategoria'),
        ),
    ]
