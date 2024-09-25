from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    new_price = models.FloatField(null=True)
    old_price = models.FloatField(null=True)
    RATING_CHOICES = [(i, str(i)) for i in range(1, 5)]  # 1, 2, 3,4,5

    rating = models.IntegerField(choices=RATING_CHOICES, default=2)
    is_sale = models.BooleanField(default=False)
    image = models.ImageField(upload_to='post/',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Meta:
    ordering = ['new_price']
class Comments(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='comments', null=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"

