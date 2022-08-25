# Generated by Django 3.0.8 on 2022-04-05 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Instruction',
                'verbose_name_plural': '2.Instruction',
            },
        ),
        migrations.CreateModel(
            name='SiteFaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': '4.FAQ',
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=255)),
                ('site_phone', models.CharField(max_length=20)),
                ('site_email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'SiteInfo',
                'verbose_name_plural': '1.SiteInfo',
            },
        ),
        migrations.CreateModel(
            name='InstructionList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('instruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instructions', to='settings.Instruction')),
            ],
            options={
                'verbose_name': 'Instruction',
                'verbose_name_plural': '3. Instruction',
            },
        ),
    ]
