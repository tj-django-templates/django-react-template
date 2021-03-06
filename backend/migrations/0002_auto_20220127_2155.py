# Generated by Django 4.0.1 on 2022-01-27 21:55
from os.path import basename
from random import randint
from urllib.parse import urlparse

from django.db import migrations

PRODUCT_URLS = [
    "https://ergosource.com/wp-content/uploads/2018/04/AdjustTable_Top_Maple-450x450.png",
    "https://m.media-amazon.com/images/I/61Mw7-qF5xL._AC_SY450_.jpg",
    "https://i5.walmartimages.com/asr/f3cdb5dd-2673-44a9-87c9-64250dba4082.7c6120ab98b4701293d8595b359a6e24.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF",
    "https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_25/3486004/b1c74804-64ff-41bf-aa64-3af94567575d-1-60517d19ec1aa9a58fb3fdb28d42910e-60d370b4aa255.jpeg",
    "https://www.notinjersey.com/wp-content/uploads/2019/11/e0bfb1a4-bb91-410f-9515-c65e99a8f7a6_1.5a2c9fb01325781dae3a94a2aec18411.jpeg",
    "https://m.media-amazon.com/images/I/41eIJYGaW+S._AC_SS450_.jpg",
    "https://imageresizer.furnituredealer.net/img/remote/images.furnituredealer.net/img/products%2Faspenhome%2Fcolor%2Fplatinum%20br_i251-303-1-b1.jpg?width=450&height=450&scale=both&trim.threshold=80"
]


def forwards_func(apps, schema_editor):
    Product = apps.get_model('backend', 'Product')

    Product.objects.bulk_create(
        [
            Product(
                name=f"Product {index}",
                image=product_url,
                price=randint(1, 5) * 10,
            )
            for index, product_url in enumerate(PRODUCT_URLS)
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, migrations.RunPython.noop),
    ]
