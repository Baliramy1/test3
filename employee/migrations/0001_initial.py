# Generated by Django 3.2.4 on 2022-03-03 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('subject', models.CharField(choices=[('WFH', 'WFH'), ('Leave', 'Leave'), ('Casual', 'Casual'), ('Hafe Day', 'Hafe Day')], default=False, max_length=33)),
            ],
        ),
    ]
