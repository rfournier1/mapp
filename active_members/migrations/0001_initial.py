# Generated by Django 2.1.3 on 2018-11-01 18:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.datetime_safe


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BDESecurityGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom du groupe sur AD')),
            ],
        ),
        migrations.CreateModel(
            name='INSASecurityGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nom du groupe sur AD')),
            ],
        ),
        migrations.CreateModel(
            name='LedMailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=255, verbose_name='Adresse Email de la Mailing')),
                ('type', models.CharField(choices=[('S', 'Sous-Equipe'), ('R', 'Resps')], default='S', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhesion_id', models.IntegerField(blank=True, null=True, unique=True, verbose_name='ID sur Adhésion')),
                ('last_name', models.CharField(max_length=255, verbose_name='Nom')),
                ('first_name', models.CharField(max_length=255, verbose_name='Prénom')),
                ('insa_email', models.EmailField(max_length=255, unique=True, verbose_name='Email INSA')),
                ('insa_username', models.CharField(blank=True, max_length=20, null=True, verbose_name='Login INSA')),
                ('office365_email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email BdE')),
                ('genre', models.CharField(choices=[('H', 'Homme'), ('F', 'Femme'), ('I', 'Indéfini/Inconnu')], default='I', max_length=1)),
                ('birthdate', models.DateField(blank=True, default=django.utils.datetime_safe.date.today, verbose_name='Date de naissance')),
                ('promo', models.IntegerField(verbose_name='Promo INSA')),
            ],
        ),
        migrations.CreateModel(
            name='SubTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Nom de l'équipe")),
                ('mailing', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subTeams', to='active_members.LedMailing')),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name="Nom de l'équipe")),
                ('type', models.CharField(choices=[('M', 'Manifs'), ('A', 'Animations'), ('S', 'Services'), ('T', 'Transversal')], max_length=1, verbose_name="Type d'équipe")),
                ('is_ma', models.BooleanField(default=True, verbose_name='Considère le membre comme actif ?')),
                ('resp_mailing', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team', to='active_members.LedMailing')),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.Member')),
                ('responsable_bde_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.BDESecurityGroup')),
                ('responsable_insa_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.INSASecurityGroup')),
                ('team_bde_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.BDESecurityGroup')),
                ('team_insa_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='active_members.INSASecurityGroup')),
            ],
        ),
        migrations.AddField(
            model_name='subteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subTeams', to='active_members.Team'),
        ),
        migrations.AddField(
            model_name='member',
            name='teams',
            field=models.ManyToManyField(blank=True, related_name='members', to='active_members.SubTeam'),
        ),
    ]