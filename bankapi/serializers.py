from rest_framework import serializers
from bankapi.models import Bank
from bankapi.models import Branches
from bankapi.models import BankBranch


class BankSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank
		fields = (
			'name'
		)

class BranchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Branches
		fields = (
			'ifsc',
			'bank_id',
			'branch',
			'address',
			'city',
			'district',
			'state',
		)

class BankBranchSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank_Branches
		fields = (
			'bank_id',
			'branch',
			'address',
			'city',
			'district',
			'state',
			'bank_name',

		)