from django.db import models
from django.urls import reverse


class Material(models.Model):
    mill = models.ForeignKey('Mill', on_delete=models.SET_NULL, null=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.SET_NULL, null=True)

    description = models.CharField(max_length=50)
    date_received = models.DateField(null=True, blank=True)
    date_sold = models.DateField(null=True, blank=True)
    po = models.CharField(max_length=20)

    heat1 = models.CharField(max_length=20, blank=True)
    heat2 = models.CharField(max_length=20, blank=True)
    heat3 = models.CharField(max_length=20, blank=True)
    heat4 = models.CharField(max_length=20, blank=True)
    heat5 = models.CharField(max_length=20, blank=True)

    udf2 = models.CharField(max_length=20, blank=True)
    udf3 = models.CharField(max_length=20, blank=True)

    SOURCE = (
        ('f', 'Foreign'),
        ('d', 'Domestic'),
    )
    status = models.CharField(max_length=1, choices=SOURCE,
                              blank=True, default='d')

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('material-detail', args=[str(self.id)])


class Mill(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return '({0}) {1}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('mill-detail', args=[str(self.id)])


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=5)

    def __str__(self):
        return '({0}) {1}'.format(self.id, self.name)

    def get_absolute_url(self):
        return reverse('vendor-detail', args=[str(self.id)])
