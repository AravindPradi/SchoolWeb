from django.db import models

class JoinForm(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    department = models.CharField(max_length=50, choices=[('commerce', 'Commerce'), ('science', 'Science'), ('computerscience', 'Computerscience')])
    course = models.CharField(max_length=50, choices=[('bcom', 'Bcom'), ('biology', 'Biology'), ('ai', 'Ai')])
    purpose = models.CharField(max_length=20, choices=[('enquiry', 'For Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials_provide = models.ManyToManyField('Material')

class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
