# Generated by Django 4.1.7 on 2024-02-05 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings_app', '0008_alter_comment_text_alter_fileattachment_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
