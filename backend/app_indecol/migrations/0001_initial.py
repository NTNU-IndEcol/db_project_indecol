# Generated by Django 4.2.6 on 2023-11-15 08:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Cherubini Group', 'Francesco Cherubini Group'), ('Verones Group', 'Francesca Verones Group'), ('Stømman Group', 'Anders Strømman Group'), ('Hertwich Group', 'Edgar Hertwich Group'), ('Müller Group', 'Daniel Müller Group'), ('Pettersen Group', 'Johan Pettersen Group'), ('Ottelin Group', 'Juudit Ottelin Group'), ('IEDL Group', 'Konstantin Stadler Group')], max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('sintef', 'Sintef'), ('equinor', 'Equinor'), ('TK', 'Trondheim Kommune'), ('PUCP', 'Pontificia Universidad Católica del Perú'), ('ETH', 'ETH Zürich'), ('SUA', 'Sokoine University of Agriculture'), ('Government of the Netherlands', 'Government of the Netherlands'), ('Leiden University', 'Leiden University'), ('APRI', 'Africa Prolicy Research Institute'), ('WU', 'Vienna University of Economics and Business'), ('SGS', 'SGS'), ('No External Partners', 'No External Partners')], max_length=50)),
                ('description', models.TextField(max_length=2000)),
                ('url', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('University', 'University'), ('Private sector', 'Private sector'), ('Industry', 'Industry'), ('N/A', 'N/A')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('role', models.CharField(choices=[('Master Student', 'Master Student'), ('PhD', 'PhD'), ('PostDoc', 'PostDoc'), ('Enginner', 'Enginner'), ('Associate Professor', 'Associate Professor'), ('Researcher', 'Researcher'), ('Professor', 'Professor')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
                ('location', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Software', 'Software'), ('Article', 'Article'), ('Website', 'Website'), ('Report', 'Report')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=2000)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('keywords', models.CharField(max_length=100)),
                ('methods', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Master Project', 'Master Project'), ('PhD Project', 'PhD Project'), ('PostDoc Project', 'PostDoc Project'), ('Other type', 'Other type'), ('European Project', 'European Project')], default='-', max_length=50)),
                ('groups', models.ManyToManyField(related_name='groups', to='app_indecol.group')),
                ('partners', models.ManyToManyField(related_name='partners', to='app_indecol.partner')),
                ('persons', models.ManyToManyField(related_name='persons', to='app_indecol.person')),
                ('ressources', models.ManyToManyField(blank=True, to='app_indecol.ressource')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='persons',
            field=models.ManyToManyField(to='app_indecol.person'),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
