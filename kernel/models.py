from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    floor = models.
    height = models.IntegerField()
    
class Jog(models.Model):
    type_run = models.IntegerField()

# Карта пользователя
class UserCard(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    time_start = models.IntegerField()
    time_finish = models.IntegerField()
    distance = models.IntegerField()
    weight = models.integerField()
    comment = models.TextField(blank=True)
    type_run = models.ForeignKey(Jog, on_delete=models.PROTECT)


# Обобщенные данные
class TotalInformation(models.Model):
    total_time = 
    totla_distance = 
    total_calorie_expenditure =
    total_number_runs =
    type_run = models.ForeignKey(Jog, on_delete=models.PROTECT)


# Данные за год
class YearlyData(models.Model):
    time_start = models.IntegerField()
    time_finish = models.IntegerField()
    distance = models.IntegerField()
    calories = models.IntegerField()
    number_runs = models.IntegerField()
    type_run = models.ForeignKey(Jog, on_delete=models.PROTECT)


# Данные за месяц
class MonthlyData(models.Model):
    time_start = models.IntegerField()
    time_finish = models.IntegerField()
    distance = models.IntegerField()
    calories = models.IntegerField()
    number_runs = models.IntegerField()
    type_run = models.ForeignKey(Jog, on_delete=models.PROTECT)

# Данные за неделю
class WeeklyData(models.Model):
    time_start = models.IntegerField()
    time_finish = models.IntegerField()
    distance = models.IntegerField()
    calories = models.IntegerField()
    number_runs = models.IntegerField()
    type_run = models.ForeignKey(Jog, on_delete=models.PROTECT)

# Данные за день
class DataPay(models.Model):
    time_start = models.IntegerField()
    time_finish = models.IntegerField()
    distance = models.IntegerField()
    calories = models.IntegerField()
    number_runs = models.IntegerField()
    type_run = models.ForeignKey(Jog, on_delete=models.PROTECT)






    

