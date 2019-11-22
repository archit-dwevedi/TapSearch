from django.db import models

# Create your models here.




class Paragraph(models.Model):
    text=models.TextField(null=True,blank=True)


    def __str__(self):
        return " ".join(self.text.strip().split(" ")[:2])
    


class InvertedMap(models.Model):
    word=models.CharField(max_length=255)
    paragraphs=models.ManyToManyField(Paragraph,blank=True)

    def __str__(self):
        return self.word
