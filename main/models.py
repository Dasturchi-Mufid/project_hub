from django.db import models

class Head(models.Model):
    logo = models.ImageField(upload_to='logo')
    img = models.ImageField(upload_to='banners/')
    description = models.TextField()


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True,null=True)


class Team(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='team/')
    major = models.CharField(max_length=255)


class Message(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    body = models.TextField()
    is_active = models.BooleanField(default=False)


class Resume(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    cv = models.FileField(upload_to='cv')
    is_active = models.BooleanField(default=False)


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    work_day = models.CharField(max_length=1)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    task = models.TextField()
    technology = models.CharField(max_length=255)
    
