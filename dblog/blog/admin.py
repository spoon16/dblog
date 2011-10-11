from blog.models import Entry
from django.contrib import admin
from datetime import datetime

class EntryAdmin(admin.ModelAdmin):
  fields = ( 'title', 'slug', 'state', 'body', 'created', 'last_updated', 'author', )
  readonly_fields = ( 'last_updated', )
  date_heirarchy = 'created'
  ordering = ( '-created', )
  list_display = ( 'title', 'slug', 'state', 'author', 'created', )
  list_filter = ( 'state', 'author', )
  prepopulated_fields = { 'slug': ('title', ), }
  search_fields = ( 'title', 'body', )

  def get_readonly_fields(self, request, obj=None):
    if not request.user.is_superuser:
      return self.readonly_fields + ( 'created', 'author', )
    return self.readonly_fields

  def save_model(self, request, obj, form, change):
    dt = datetime.now()
    if not change:
      obj.created = dt
      obj.author = request.user
    obj.last_updated = dt
    obj.save()

admin.site.register(Entry, EntryAdmin)
