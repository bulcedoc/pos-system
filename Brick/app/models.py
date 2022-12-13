from django.db import models
import uuid
class Products(models.Model):
    p_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name="id")
    p_name = models.CharField(max_length=200)
    p_price = models.IntegerField()
    p_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.p_name

    