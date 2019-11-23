from django.db import models
import random
import os
# Create your models here.


def get_filename_ext(filepath):
	base_name=os.path.basename(filepath)
	name ,ext=os.path.splitext(base_name)
	return name ,ext

def upload_image_path(instance,filename):
	new_filename=random.randint(1,13516546431654)
	name ,ext=get_filename_ext(filename)
	final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
	return "static/uploads5/{final_filename}".format(
		new_filename=new_filename,
		final_filename=final_filename
		)
class FileUpload(models.Model):
    file=models.FileField(upload_to=upload_image_path,null=True,blank=True)
    defa=models.BooleanField(default=True)

class Paragraph(models.Model):
	text=models.TextField(null=True,blank=True)
	document=models.ForeignKey(FileUpload,on_delete=models.CASCADE,null=True,blank=True)
	doc=models.FileField(upload_to=upload_image_path,null=True,blank=True)
	def __str__(self):
		return " ".join(self.text.strip().split(" ")[:2])
    


class InvertedMap(models.Model):
    word=models.CharField(max_length=255)
    paragraphs=models.ManyToManyField(Paragraph,blank=True)

    def __str__(self):
        return self.word





