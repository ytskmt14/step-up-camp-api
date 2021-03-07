from django.db import models

class Contact(models.Model):
    name = models.CharField(
        max_length=50,
        blank=False,
    )
    email = models.EmailField()
    title = models.CharField(
        max_length=50,
        blank=False,
    )
    content = models.TextField(blank=False,)
    created_at = models.DateTimeField(auto_now_add=True,)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

