from django import forms
from .models import Tasks
from django.forms import ModelForm
    
    
class TasksForm(forms.ModelForm):
	class Meta():
		model = Tasks
		fields = ['title','due']
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','label':'Title'}),
            'due': forms.DateTimeInput(attrs={'due':'Due_Date','class': 'form-control','type':'date'})
            }



class UpdateForm(forms.ModelForm):
	class Meta():
		model = Tasks
		fields = ['title','due','complete']
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'due':forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
           }