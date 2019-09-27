#!/usr/bin/python
# -*- coding: <encoding name> -*-
from django import forms

from .models import Hdb
from django.forms import widgets
from django.contrib.auth.models import User


class Tform(forms.ModelForm):
    #ntext=forms.CharField(widget=forms.TextInput(
	#			attrs={ #'wrapper_class':'form-control is-valid'
	#				'class': 'form-control is-valid'
	#				}
	#				))
    class Meta:
        model = Hdb
        fields = ('__all__')
        
    #    
        def __init__( self, *args, **kwargs ):
            Tform.__init__( *args, **kwargs )
            
            for myField in self.fields:
                self.fields[myField].widget.attrs['class'] = 'form-control is-valid'
        #        self.fields['ntext'].widget.attrs['placeholder'] = 
        #    self.field[ 'my_field' ].widget.attrs.update( {
        #    'class': 'form-control' } )
        
        
class SearchForm(forms.Form): 
    word = forms.CharField(label='Search Word')
    
class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput()
        
      
        for field in self.fields:
            self.fields[field].widget.attrs['placeholder'] = None
            del self.fields[field].widget.attrs['placeholder']
