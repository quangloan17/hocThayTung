from django import forms
from core.models import *


class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].queryset = Language.objects.none()

        if 'language' in self.data:
            self.fields['language'].queryset = Language.objects.all()

        elif self.instance.pk:
            self.fields['language'].queryset = Language.objects.all().filter(pk=self.instance.language.pk)

class KhachHangForm(forms.ModelForm):

    class Meta:
        model = Khachhang
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = Khachhang.objects.none()

        if 'name' in self.data:
            self.fields['name'].queryset = Khachhang.objects.all()

        elif self.instance.pk:
            self.fields['name'].queryset = Khachhang.objects.all().filter(pk=self.instance.name.pk)


class DonHangForm(forms.ModelForm):

    class Meta:
        model = Donhang
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].queryset = Donhang.objects.none()

        if 'name' in self.data:
            self.fields['name'].queryset = Donhang.objects.all()

        elif self.instance.pk:
            self.fields['name'].queryset = Donhang.objects.all().filter(pk=self.instance.name.pk)