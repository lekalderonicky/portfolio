from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ('title', 'created_at', 'thumbnail')
	search_fields = ('title',)
	readonly_fields = ('thumbnail',)

	def thumbnail(self, obj):
		if obj.image:
			return f"<img src='{obj.image.url}' style='max-height:60px; max-width:120px;' />"
		return '-'
	thumbnail.allow_tags = True
	thumbnail.short_description = 'Image'
