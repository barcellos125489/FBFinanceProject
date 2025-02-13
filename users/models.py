from django.db import models
from django.contrib.auth.models import User

class income(models.Model):
    """Every type of income can be defined with the attributes of this class"""
    date_added = models.DateTimeField(auto_now_add=True)
    income_name = models.TextField(max_length=25)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    regular_income = models.BooleanField()

    def __str__(self):
        """returns a string representation of the model"""
        return self.income_name

class loan(models.Model):
    """Every type of loan can be defined with the attributes of this class"""
    date_added = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField()
    loan_name = models.TextField(max_length=25)
    total_value = models.DecimalField(max_digits=10,decimal_places=2)
    value_left = models.DecimalField(max_digits=10,decimal_places=2)
    value_payed = models.DecimalField(max_digits=10,decimal_places=2) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.DecimalField(max_digits=5,decimal_places=4)

    def __str__(self):
        """returns a string representation of the model"""
        return self.loan_name
    
class finance(models.Model):
    """Every type of finance can be defined with the attributes of this class"""
    date_added = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=False)
    finance_name = models.TextField(max_length=25)
    total_value = models.DecimalField(max_digits=10,decimal_places=2)
    value_left = models.DecimalField(max_digits=10,decimal_places=2)
    value_payed = models.DecimalField(max_digits=10,decimal_places=2) 
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    interest = models.DecimalField(max_digits=5,decimal_places=4)

    def __str__(self):
        """returns a string representation of the model"""
        return self.finance_name
    
class expense(models.Model):
    """Every type of expense can be defined with the attributes of this class"""
    date_added = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now_add=False)
    expense_name = models.TextField(max_length=25)
    value = models.DecimalField(max_digits=10,decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    credit = models.BooleanField()
    installments = models.PositiveSmallIntegerField()

    def __str__(self):
        """returns a string representation of the model"""
        return self.expense_name

# Create your models here.
