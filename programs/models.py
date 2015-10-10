from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Institution(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)
    #gradrates are associated keys
    #numberOfLabs comes from counting courses
    #offerings should count courses
    USNewsRank = models.IntegerField(blank=True,null=True)

    def avg_grads(self):
        list = [rate.count for rate in self.gradrate_set.all()]
        if len(list)==0:
            return ""
        return sum(list)/len(list)

    class Meta:
        ordering = ['name']

class Instructor(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200)
    institution = models.ForeignKey(Institution)
    email = models.EmailField(max_length=200)
    def get_absolute_url(self):
        return reverse('instructor_detail', kwargs={'pk': self.pk})


class Course(models.Model):
    def __str__(self):
        return self.name

    FIRST_TERM_SOPH = 'FS'
    INT_METHODS = 'INT'
    ELECTIVE = 'EL'
    ADVLAB = 'ADV'
    LEVEL_CHOICES = (
        (FIRST_TERM_SOPH, 'First term or sophomore'),
        (INT_METHODS, 'Intermediate methods'),
        (ELECTIVE, 'Elective lab courses'),
        (ADVLAB, 'Advanced Lab')
    )
    level = models.CharField(max_length=3,
                             choices=LEVEL_CHOICES,
                             default=FIRST_TERM_SOPH)

    name = models.CharField(max_length=100)
    instructor = models.ForeignKey(Instructor)

class GradRate(models.Model):
    institution = models.ForeignKey(Institution)
    year = models.IntegerField()
    count = models.IntegerField()
