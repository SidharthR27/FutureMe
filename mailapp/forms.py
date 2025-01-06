from django import forms
from .models import FutureMail

class FutureMailForm(forms.ModelForm):
    class Meta:
        model = FutureMail
        fields = ['name','email', 'message', 'send_whatsapp', 'mobile_number']
    
    def clean(self):
        cleaned_data = super().clean()
        send_whatsapp = cleaned_data.get('send_whatsapp')
        mobile_number = cleaned_data.get('mobile_number')
        
        # Validate mobile number if WhatsApp is selected
        if send_whatsapp and not mobile_number:
            raise forms.ValidationError("Please provide a mobile number if you want a WhatsApp message.")
        return cleaned_data
