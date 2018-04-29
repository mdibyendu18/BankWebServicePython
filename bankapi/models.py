from django.db import models

# Create your models here.
class Bank(models.Model):
	name = models.CharField(max_length=49)


class Branches(models.Model):
	ifsc = models.CharField(max_length=11, primary_key=True)
	bank_id = models.ForeignKey(Bank)
	branch = models.CharField(max_length=74)
	address = models.CharField(max_length=195)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=26)


class BankBranch(models.Model):
	ifsc = models.BigIntegerField()
	bank_id = models.ForeignKey(Bank)
	branch = models.CharField(max_length=74)
	address = models.CharField(max_length=195)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=26)
	bank_name = models.CharField(max_length=49)

	class Meta:
		managed = False
		db_table = 'bank_branches'
