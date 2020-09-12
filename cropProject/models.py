from django.db import models

class UserImage(models.Model):
    unique_together =(('username','filename'))
    userName = models.CharField( max_length=50)
    fileName = models.CharField(max_length=100)
        


    def __str__(self):
        return self.userName + self.fileName


