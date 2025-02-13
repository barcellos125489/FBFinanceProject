from django.contrib import admin
from users.models import loan, finance, expense, income

admin.site.register(loan)
admin.site.register(expense)
admin.site.register(income)
admin.site.register(finance)


# Register your models here.
