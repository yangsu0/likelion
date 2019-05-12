from django.db import models

# Create your models here.
class Comment(models.Model):
    content=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
