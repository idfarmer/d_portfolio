from pyfolio.models import *
from django.contrib import admin


#class PortfolioEntryAdmin(admin.ModelAdmin):
#	fieldsets = [
#		(None, {'fields':['title','slug','columns_to_span', 'description', 'tags']}),
#		('Entry Settings',{'fields':['auto_advance', 'include_on_homepage', 'snap_to_top', 'include_in_footer']}),
#		('Display Toggles',{'fields':['display_title', 'display_client_tag', 'display_medium_tag' , 'display_date']}),
#	]
#	list_display = ('title','columns_to_span','include_on_homepage','snap_to_top','include_in_footer')
#
#class TagAdmin(admin.ModelAdmin):
#	fields = ['kind','title','slug']
#	list_display = ('kind', 'title','slug')

class EntryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['title','slug','image','youtube_embed_code','caption','tags']})
	]

class TagAdmin(admin.ModelAdmin):
	list_display = ('kind', 'title','slug')


admin.site.register(Entry, EntryAdmin)
admin.site.register(TitleSlider)
admin.site.register(Slide)
admin.site.register(Tag, TagAdmin)
admin.site.register(General)
admin.site.register(Footer)



