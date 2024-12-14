from django.db import models

class CenterType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class EntertainmentCenter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    center_type = models.ForeignKey(
        CenterType, on_delete=models.SET_NULL, null=True, related_name='entertainment'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class CenterType(models.Model):
        name = models.CharField(max_length=255)
        description = models.TextField()

        def __str__(self):
            return self.name
