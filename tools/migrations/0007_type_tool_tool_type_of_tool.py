# Generated by Django 4.2.3 on 2023-07-21 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0006_rename_amont_coinbaseprocess_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='type_tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='tool',
            name='type_of_tool',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tools.type_tool'),
            preserve_default=False,
        ),
    ]
