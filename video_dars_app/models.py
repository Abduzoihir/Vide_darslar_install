from django.db import models

class Card(models.Model):
    image=models.ImageField(upload_to='card/image/')
    title=models.CharField(max_length=150,unique=True)
    subtitle=models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Mavzu(models.Model):
    title=models.CharField(max_length=150)
    card=models.ForeignKey(Card,on_delete=models.CASCADE,related_name='mavzular')

    def __str__(self):
        return self.title
    
class Video(models.Model):
    image=models.ImageField(upload_to='video/image/')
    video=models.FileField(upload_to='video/videos/')
    title=models.CharField(max_length=150)
    mavzu=models.ForeignKey(Mavzu,on_delete=models.CASCADE,related_name='videolar')

    def __str__(self):
        return self.title
    
class test(models.Model):
    title=models.CharField(max_length=150)
    video=models.TextField()

    def __str__(self):
        return self.title
