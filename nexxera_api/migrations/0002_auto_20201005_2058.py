# Generated by Django 3.1.2 on 2020-10-05 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nexxera_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('operation', models.CharField(max_length=64, verbose_name='operation')),
                ('value', models.FloatField(verbose_name='value')),
                ('description', models.CharField(max_length=256, verbose_name='description')),
                ('date', models.DateField(blank=True, null=True, verbose_name='date')),
                ('status', models.BooleanField(blank=True, null=True, verbose_name='status')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_account', to='nexxera_api.account', verbose_name='bank account')),
            ],
            options={
                'index_together': {('account', 'operation', 'value', 'status')},
            },
        ),
        migrations.DeleteModel(
            name='History',
        ),
    ]
