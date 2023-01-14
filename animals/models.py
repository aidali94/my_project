from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=64)
    age = models.PositiveSmallIntegerField()
    description = models.TextField(blank=True)
    kind = models.ForeignKey('AnimalKind', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'Animal with name: {self.name} and kind: {self.kind}'


class AnimalKind(models.Model):
    kind = models.CharField(max_length=32)


class AnimalDetail(models.Model):
    animal = models.OneToOneField('animal.Animal',
                                  primary_key=True,
                                  on_delete=models.CASCADE)
    biography = models.TextField(blank=True)
