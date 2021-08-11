from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Pollster admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInLine]


admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
