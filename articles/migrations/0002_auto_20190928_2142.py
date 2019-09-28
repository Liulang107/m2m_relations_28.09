# Generated by Django 2.1.1 on 2019-09-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Тематический раздел',
                'verbose_name_plural': 'Тематические разделы',
            },
        ),
        migrations.CreateModel(
            name='ScopeRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(verbose_name='Основной')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='articles.Article')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Scope')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(related_name='articles', through='articles.ScopeRelation', to='articles.Scope'),
        ),
    ]
