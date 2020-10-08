# Generated by Django 3.1.2 on 2020-10-08 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nexxera_api', '0002_auto_20201005_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacted_account', to='nexxera_api.account', verbose_name='bank account'),
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_balance', models.FloatField(verbose_name='last balance')),
                ('new_balance', models.FloatField(verbose_name='balance')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_account', to='nexxera_api.account', verbose_name='bank account')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history_transaction', to='nexxera_api.account', verbose_name='transaction')),
            ],
            options={
                'index_together': {('account', 'transaction', 'last_balance', 'new_balance')},
            },
        ),
    ]
