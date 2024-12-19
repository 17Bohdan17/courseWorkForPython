from django.db import models

# Модель для типу центру
class CenterType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Модель для розважального центру
class EntertainmentCenter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    center_type = models.ForeignKey('CenterType', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Модель для відвідувача
class Visitor(models.Model):
    username = models.CharField(max_length=255, verbose_name="Ім'я відвідувача")
    email = models.EmailField(verbose_name="Електронна пошта")

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    entertainment_center = models.ForeignKey(
        'EntertainmentCenter',
        on_delete=models.CASCADE
    )
    description = models.TextField()

    def __str__(self):
        return self.name



    # Властивість, яка повертає ID центру
    @property
    def center_id(self):
        return self.center.id

    def __str__(self):
        return f"{self.username} ({self.email})"


