# Generated by Django 4.0.6 on 2022-08-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('dept_name', models.CharField(blank=True, max_length=50, null=True)),
                ('org_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('mod_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mod_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'modules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('org_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('org_name', models.CharField(blank=True, max_length=50, null=True)),
                ('logo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'organisation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigAutoField(db_column='User_id', primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dept_name', models.CharField(blank=True, max_length=50, null=True)),
                ('org_name', models.CharField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(max_length=50)),
                ('modules', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('password', models.CharField(max_length=50)),
                ('user_name', models.CharField(blank=True, max_length=50, null=True)),
                ('role', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
