# Generated by Django 5.0.4 on 2024-04-14 08:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='quiz_file',
            field=models.FileField(default='none', upload_to='quiz/{self.name}/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.subject')),
            ],
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizes.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answerreason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('question', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quizes.question')),
            ],
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
