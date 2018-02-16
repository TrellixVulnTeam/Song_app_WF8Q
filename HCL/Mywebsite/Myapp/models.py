from django.db import models


class Odc1(models.Model):
    person_id = models.IntegerField(default=1, primary_key=True)
    person_name = models.CharField(max_length=60)
    person_age = models.IntegerField()


def __str__(self):
        return self.person_name


