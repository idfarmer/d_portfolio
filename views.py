from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.views.generic import list_detail
from pyfolio.models import *

#def home(request):
#	slider = TitleSlider.objects.all()
#	slide = Slide.objects.all()
#	entry = Entry.objects.all()
#	tag = Tag.objects.all()
#	footer = Footer.objects.all()
#	general = General.objects.all()
#	
#	return render_to_response('home.html', locals())

def show_tag(request, tag_title):

	t_title = get_object_or_404(Tag, title__iexact=tag_title)
	
	titleslider = TitleSlider.objects.filter(tags__title__iexact=tag_title)
	slide = Slide.objects.all()
	entry = Entry.objects.filter(tags__title__iexact=tag_title)
	tag = Tag.objects.all()
	footer = Footer.objects.all()
	general = General.objects.all()
	
	return list_detail.object_list(
			request,
			queryset = Entry.objects.filter(tags__title__iexact=tag_title),
			template_name = 'home.html',
			template_object_name = 'tag',
			extra_context = {'tag_title':str(t_title),'tag': tag, 'titleslider':titleslider, 'entry': entry, 'slide':slide, 'footer':footer, 'general':general}
	)
	