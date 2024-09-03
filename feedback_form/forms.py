from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    voice_recording = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Feedback
        fields = [
            'name', 'phone_number', 'email', 'branch', 'value_for_money',
            'packaging', 'quality', 'display', 'variety', 'comments',
            'employee_name_and_id', 'date_of_birth', 'anniversary', 'voice_recording'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Enter your phone number'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email address'}),
            'comments': forms.Textarea(attrs={'placeholder': 'Enter your comments here', 'rows': 3}),
            'date_of_birth': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
            'anniversary': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
            'branch': forms.Select(
                attrs={'aria-label': 'Please select a branch'},
                choices=[('', 'Please Select')] + Feedback.BRANCH_CHOICES
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set RadioSelect widget for certain fields
        for field_name in ['value_for_money', 'packaging', 'quality', 'display', 'variety']:
            self.fields[field_name].widget = forms.RadioSelect()
            self.fields[field_name].choices = Feedback.FEEDBACK_CHOICES

        # Ensure fields are rendered as radio buttons in a row
        self.fields['value_for_money'].widget.attrs.update({'class': 'inline-radio'})
        self.fields['packaging'].widget.attrs.update({'class': 'inline-radio'})
        self.fields['quality'].widget.attrs.update({'class': 'inline-radio'})
        self.fields['display'].widget.attrs.update({'class': 'inline-radio'})
        self.fields['variety'].widget.attrs.update({'class': 'inline-radio'})
        
        
        self.fields['phone_number'].validators.append(self.validate_phone_number)

    def validate_phone_number(self, value):
        # Remove any non-digit characters
        value = ''.join(filter(str.isdigit, value))
        if len(value) != 10:
            raise forms.ValidationError('Phone number must be exactly 10 digits.')