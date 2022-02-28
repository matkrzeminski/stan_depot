# Generated by Django 3.2.12 on 2022-02-28 17:55

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone
import markdownx.models
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=120, verbose_name='Title')),
                ('hero', models.ImageField(blank=True, upload_to='blog/heroes', verbose_name='Hero')),
                ('thumbnail', models.ImageField(blank=True, editable=False, upload_to='blog/thumbs')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True, verbose_name='Post address')),
                ('content', markdownx.models.MarkdownxField(blank=True, verbose_name='Content')),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'draft')], default='draft', max_length=9, verbose_name='Status')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
