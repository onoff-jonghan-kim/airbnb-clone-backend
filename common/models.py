from django.db import models

class CommonModel(models.Model):

    """ Common Model Definition """

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True