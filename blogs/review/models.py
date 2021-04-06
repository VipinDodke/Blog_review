from django.db import models

class Blog_out(models.Model):
    blog_id= models.AutoField
    Blog_name=models.CharField(max_length=200,default='')
    desc=models.CharField(max_length=700,default='')
    post_date=models.DateField()

    def __str__(self):
        return self.Blog_name

class Feedback(models.Model):
    fb_id = models.AutoField
    Name = models.CharField(max_length=200,default='')
    Textarea = models.CharField(max_length=700,default='')
    Blog_id = models.IntegerField(default=0)
    FileTy =models.FileField(blank=True, null=True)
    def __str__(self):
        return self.Name
