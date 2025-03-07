from django.db import models

class Thread(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def _str_(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    picture = models.FileField(upload_to='post_pictures/')
    description = models.TextField()
    author = models.CharField(max_length=100)
    thread = models.ForeignKey(Thread, related_name='posts', on_delete=models.CASCADE)

    def _str_(self):
        return self.title
