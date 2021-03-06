# Generated by Django 2.1.2 on 2019-04-30 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190430_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_subscription_id', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=True)),
                ('user_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.UserMembership')),
            ],
        ),
    ]
