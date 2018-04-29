from bankapi.models import Bank
from bankapi.models import Branches
from bankapi.models import Bank_Branches
from bankapi.serializers import BanksSerializer
from bankapi.serializers import BranchesSerializer
from bankapi.serializers import Bank_BranchesSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse




# Create your views here.
class BankBranchView(generics.RetrieveUpdateDestroyAPIView):
	pass

class BranchView(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = BranchSerializer
	name = 'branch-detail'

	def get_object(self):
		ifsc = self.kwargs.get('ifsc')
		return Branches.objects.get(ifsc=ifsc)


