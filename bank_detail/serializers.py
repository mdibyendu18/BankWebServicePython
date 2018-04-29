from rest_framework import serializers
from bank_detail.models import Banks
from bank_detail.models import Branches
from bank_detail.models import Bank_Branches


class BanksSerializer(serializers.ModelSerializer):
	class Meta:
		model = Banks
		fields = (
			'id',
			'name'
		)

class BranchesSerializer(serializers.ModelSerializer):
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

class Bank_BranchesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Bank_Branches
		fields = (
			'ifsc',
			'bank_id',
			'branch',
			'address',
			'city',
			'district',
			'state',
			'bank_name'
		)