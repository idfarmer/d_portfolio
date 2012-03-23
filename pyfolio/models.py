from django.db import models
import datetime


class TitleSlider(models.Model):
	
	title = models.CharField(max_length=200)
	tags = models.ManyToManyField("Tag")
	
	def slides(self):
		return Slide.objects.filter(titleslider=self.id)
	
	def __unicode__(self):
		return self.title
	
	class Admin:
		pass

class Entry(models.Model):

	title = models.CharField(max_length=200)
	slug = models.SlugField(max_length=200, unique=True)
	tags = models.ManyToManyField("Tag")
	image = models.ImageField(blank=True, upload_to=".")
	youtube_embed_code = models.TextField(blank=True)
	caption = models.TextField(blank=True)
	include_on_homepage = models.BooleanField()
	time_created = models.DateTimeField(auto_now_add=True)
	time_modified = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.title

	class Admin:
	    pass

#	snap_to_top = models.BooleanField()
#	auto_advance = models.BooleanField()
#	columns_to_span = models.IntegerField()
#	display_title = models.BooleanField(default=True)
#	include_in_footer = models.BooleanField()
#	author = models.CharField(max_length=200, blank=True)
#	display_author = models.BooleanField()
#	display_client_tag = models.BooleanField(default=True)
#	display_medium_tag = models.BooleanField(default=True)
#	display_date = models.BooleanField()
#	def slides(self):
#		return Slide.objects.filter(portfolioentry = self.id)

class Slide(models.Model):
	title = models.CharField(max_length=200)
	title_style = models.TextField(blank=True)
	caption = models.TextField()
	image = models.ImageField(blank=True, upload_to=".")
	titleslider = models.ForeignKey("TitleSlider")
	tags = models.ManyToManyField("Tag")
	tag_style = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.title	
	class Admin:
	    pass

# 	embed_code = models.TextField(blank=True)
	
class Tag(models.Model):
	kind = models.CharField(max_length=50,choices=(("medium", "medium"),("client", "client"),("page", "page")))
	title = models.CharField(max_length=50, unique=True)
	slug = models.SlugField(max_length=50, unique=True)
	def __unicode__(self):
		return self.title
	
	class Admin:
	    pass

class Footer(models.Model):
	title = models.CharField(max_length=200)
	columns_to_span = models.IntegerField()
	caption = models.TextField()
	
	def __unicode__(self):
		return self.title
	
	class Admin:
		pass

class General(models.Model):
	org_name = models.CharField(max_length=50)
	org_logo = models.ImageField(blank=True, upload_to=".")
	def __unicode__(self):
		return self.org_name

	class Admin:
		pass

