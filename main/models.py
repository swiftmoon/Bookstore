from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField()
    author = models.CharField(max_length=30, default='admin')
    email = models.EmailField(blank=True)
    describe = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Books'
        ordering = ('-created',)

    def __str__(self):
        return self.name
