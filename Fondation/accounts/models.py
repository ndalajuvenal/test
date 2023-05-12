from django.db import models
from django.contrib.auth.models import User

# Create your models here.
Genre = [
    ('M', 'Masculin'),
    ('F', 'Feminin'),
]
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    birthday=models.DateField()
    phone=models.IntegerField()
    photo = models.ImageField(blank=True, null=True, upload_to='profile_pics',default='default.png')
    genre = models.CharField(max_length=10, choices=Genre, default='M')

    def __str__(self):
        return  f'{self.user.username} Profile'
 
