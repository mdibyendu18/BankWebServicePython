from django.db import models

# Create your models here.
class Banks(models.Model):
	id = models.BigIntegerField(primary_key=True, db_column='id')
	name = models.CharField(max_length=49)

	class Meta:
		managed = False
		db_table = 'banks'


class Branches(models.Model):
	ifsc = models.CharField(max_length=11, primary_key=True)
	bank_id = models.ForeignKey(Banks, db_column='bank_id')
	branch = models.CharField(max_length=74)
	address = models.CharField(max_length=195)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=26)

	class Meta:
		managed = False
		db_table = 'branches'



class Bank_Branches(models.Model):
	ifsc = models.CharField(max_length=11, primary_key=True)
	bank_id = models.ForeignKey(Banks, db_column='bank_id')
	branch = models.CharField(max_length=74)
	address = models.CharField(max_length=195)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=26)
	bank_name = models.CharField(max_length=49)

	def __str__(self):
		return "{}{}{}".format(self.ifsc, self.bank_name, self.branch)

	class Meta:
		managed = False
		db_table = 'bank_branches'
