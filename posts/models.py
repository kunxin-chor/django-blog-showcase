from django.db import models
from accounts.models import MyUser
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.title
        
    def get_excerpt(self):
        if self.title is not None and self.content is not None:
            return self.title + " - " + self.content[0:25]
        return "N/A"
        
    @staticmethod
    def search(title):
        if title is None:
            title = ""
        results = Post.objects.filter(title=title)
        return results
        
        