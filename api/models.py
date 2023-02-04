from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
    )

    name = models.TextField()
    price = models.FloatField()
    currency_code = models.CharField(max_length=5)
    image_url = models.TextField()
    url_site = models.TextField()
    marketplace = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return "{}".format(self.id)
