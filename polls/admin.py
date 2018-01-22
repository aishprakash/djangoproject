from django.contrib import admin

# Register your models here.

from .models import Choice,Question

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,{'fields': ['question_text']}),
	('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


'''
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,               {'fields': ['question_text']}),
	('Date information', {'fields': ['pub_date']}),
	]

admin.site.register(Question, QuestionAdmin)
'''
'''
class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)


#admin.site.register(Question)
'''