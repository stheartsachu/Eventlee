from django import forms
from ApplicationAdmin.models import Events
class ApplicationAdminForm(forms.ModelForm):
    class Meta():
        model = Events
        exclude = ['eventname', 'eventcategory', 'eventdescription', 'eventdate', 'eventtime', 'eventlocation' ]