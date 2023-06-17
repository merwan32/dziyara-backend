from django.contrib.auth.models import User
from django.db import models




class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    wilaya = models.ForeignKey('Wilaya', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Wilaya(models.Model):
    wilaya_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkingDayTime(models.Model):
    day = models.CharField(max_length=255, choices=[
        ('SATURDAY', 'Saturday'),
        ('SUNDAY', 'Sunday'),
        ('MONDAY', 'Monday'),
        ('TUESDAY', 'Tuesday'),
        ('WEDNESDAY', 'Wednesday'),
        ('THURSDAY', 'Thursday'),
        ('FRIDAY', 'Friday'),
    ])
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
        return f"{self.day} from {self.opening_time} to {self.closing_time}"



class TransportMean(models.Model):
    mean_name = models.CharField(max_length=255)
    icon = models.ImageField()

    def __str__(self):
        return self.mean_name


class TouristicSite(models.Model):
    site_name = models.CharField(max_length=255)
    site_type = models.CharField(max_length=255, choices=[
        ('Lieu Naturel','Lieu Naturel'),
        ('Monument Historique','Monument Historique'),
        ('Site Religieux','Site Religieux'),
        ('Centre de Loisir','Centre de Loisir'),
        ('Hébergement','Hébergement')
    ])
    description = models.CharField(max_length=255)
    current_stars = models.FloatField(default=0)
    picture = models.ImageField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    wilaya = models.ForeignKey(Wilaya, on_delete=models.CASCADE)
    Working_Time = models.ManyToManyField(WorkingDayTime, related_name='WorkingDayTime')
    Transport_Mean = models.ManyToManyField(TransportMean, related_name='TransportMean')

    
    def save(self, *args, **kwargs):
        if self.agent.wilaya != self.wilaya:
            raise ValueError("Agent can only add tourist sites in their wilaya.")
        super().save(*args, **kwargs)


    def __str__(self):
        return self.site_name



class SiteEvaluation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(TouristicSite, on_delete=models.CASCADE)
    stars = models.IntegerField()
    created_at = models.DateField()

class UserComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    site = models.ForeignKey(TouristicSite, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='event_images/')

    def __str__(self):
        return self.name