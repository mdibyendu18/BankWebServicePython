from bank_detail.models import Banks
from bank_detail.models import Branches
from bank_detail.models import Bank_Branches
from bank_detail.serializers import BanksSerializer
from bank_detail.serializers import BranchesSerializer
from bank_detail.serializers import Bank_BranchesSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import Http404
from rest_framework import status


class BankBranchView(generics.ListAPIView):
	serializer_class = Bank_BranchesSerializer
	name = 'bank-branch-detail'
	def get_queryset(self):
		city = self.kwargs.get('city')
		bank_name = self.kwargs.get('bank_name')

		branch = Bank_Branches.objects.filter(
			city__istartswith=city,
			city__icontains=city,
			bank_name__icontains=bank_name,
			bank_name__istartswith=bank_name
		).order_by('bank_id')

		if branch.exists():
			return branch
		else:
			raise Http404

class BranchView(generics.RetrieveAPIView):
	serializer_class = BranchesSerializer
	name = 'branch-detail'

	def get_object(self):
		ifsc = self.kwargs.get('ifsc')
		try: 
			 return Branches.objects.get(ifsc__icontains=ifsc)
		except Branches.DoesNotExist:
			raise Http404


