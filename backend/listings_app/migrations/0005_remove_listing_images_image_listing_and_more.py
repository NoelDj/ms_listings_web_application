# Generated by Django 4.1.7 on 2024-01-23 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings_app', '0004_alter_image_src'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='images',
        ),
        migrations.AddField(
            model_name='image',
            name='listing',
            field=models.ForeignKey(default=49, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='listings_app.listing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='fileattachment',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='listings_app.listing'),
        ),
    ]