# Generated by Django 4.0.2 on 2022-04-02 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drgmik', '0006_alter_image_article_fk_alter_paragraph_article_fk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='article_fk',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='article_fk',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='paragraph',
            old_name='article_fk',
            new_name='article',
        ),
        migrations.RemoveField(
            model_name='article',
            name='cover_img_fk',
        ),
        migrations.AddField(
            model_name='article',
            name='cover_img',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cover_img_fk', to='drgmik.image'),
            preserve_default=False,
        ),
    ]
