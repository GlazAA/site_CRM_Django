from django.db import models


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # CASCADE - удалять записи при удалении Agent. то есть вся строка Lead будет удалена
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    
class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
   

''' 
class Agent(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    lead = models.ForeignKey("Lead", on_delete=models.CASCADE)


class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),

    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    # CASCADE - удалять записи при удалении Agent. то есть вся строка Lead будет удалена
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # проверяет загружен ли файл и его тип
    profile_picture = models.ImageField(blank=True, null=True)
    # сохраняет файлы любого типа
    special_files = models.FileField(blank=True, null=True)


'''

