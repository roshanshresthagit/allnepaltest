from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=15) 
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    quiz_file = models.FileField(upload_to='quiz/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)