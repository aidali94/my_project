# Generated by Django 3.2 on 2023-01-12 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_remove_animal_kind'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnimalKind',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='animals.animalkind'),
        ),
    ]