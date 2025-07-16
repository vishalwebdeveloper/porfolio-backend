from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='image')
    video = models.FileField(upload_to='portfolio_videos/', blank=True, null=True)
    github_link = models.URLField()
    live_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
    