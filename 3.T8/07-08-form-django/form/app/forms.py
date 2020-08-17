from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fielđs = ('code','name','email') 
        # exclude = ['image',] # Dạng tuble không được để 1 phần tử, bắt buộc phải có dấu phẩy

class CustomerForm(forms.Form):
    fullname = forms.CharField(max_length=50,label = 'Họ tên')
    email = forms.EmailField(label = 'Email')
    phone = forms.CharField(max_length=20, label = 'Số ĐT')
    address = forms.CharField(max_length=200, label = 'Địa chỉ',widget=forms.Textarea,required=False)

    def clean_phone(self):
        phone = self.cleaned_data.get('phone','')
        if not phone.isdigit() or phone[0] != '0':
            raise forms.ValidationError('Số điện thoại không hợp lệ')
        return phone