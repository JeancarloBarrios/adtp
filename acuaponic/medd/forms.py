from django import forms 

class InputForm(forms.Form):
    request.POST.get('slug', 'none')
    med_qty = forms.IntegerField(label = 'Medicine Qty:', max_length = 5)
