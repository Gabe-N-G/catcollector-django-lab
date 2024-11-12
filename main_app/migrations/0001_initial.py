# Generated by Django 5.1.3 on 2024-11-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
    ]

# c = Cat(name="Lucky", breed='Black Stray Shorthair', description='Best friend', age=10)
# c = Cat(name="Garfield", breed='Cartoon', description='Hates Mondays, Immortal', age=99)
