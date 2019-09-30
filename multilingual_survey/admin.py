from django.contrib import admin
from hvad.admin import TranslatableAdmin, TranslatableTabularInline
from multilingual_survey.models import (Survey, Question, Choice)


class QuestionInline(TranslatableTabularInline):
    model = Question


class SurveyAdmin(TranslatableAdmin):
    list_display = ('admin_title',)
    inlines = [QuestionInline]


class ChoiceInline(TranslatableTabularInline):
    model = Choice


class QuestionAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'survey')
    inlines = [ChoiceInline]


class ChoiceAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'question', 'get_survey')


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
