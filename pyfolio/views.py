from pyfolio.models import PortfolioEntry
from django.http import HttpResponse

def home(request):
	everything = PortfolioEntry.objects.all()
	output = ', '.([p.title for p in everything])
	return HttpResponse(output)


