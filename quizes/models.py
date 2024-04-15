from django.db import models
import pandas as pd

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=255)
    quiz_file = models.FileField(upload_to='quiz/{name}/',null=False,default='none')


    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name_plural = 'Subjects'
    

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        if self.quiz_file:
            self.extract_quizes()
    
    #extracting quizes from excel fils
    def extract_quizes(self):
        df = pd.read_excel(self.quiz_file.path)
        for index, row in df.iterrows():
            question_text = row['Question']
            choice1 = row['A']
            choice2 = row['B']
            choice3 = row['C']
            choice4 = row['D']
            answer= row['Answer']
            reason = row['reason']

            question = Question.objects.create(subject=self, text=question_text)

            choice1 = Choice.objects.create(question=question,text=choice1,is_correct = answer == 'A')
            choice2 = Choice.objects.create(question=question,text=choice2,is_correct = answer == 'B')
            choice3 = Choice.objects.create(question=question,text=choice3,is_correct = answer == 'C')
            choice4 = Choice.objects.create(question=question,text=choice4,is_correct = answer == 'D')

            reason = Answerreason.objects.create(question=question,text=reason)





class Category(models.Model):
    name = models.CharField(max_length=255) 
    subject = models.ManyToManyField(Subject)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'
    

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self) -> str:
        return self.text[:25]

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:50]}, {self.text[:20]}"

class Answerreason(models.Model):
    question = models.OneToOneField(Question,on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text[:50]
        