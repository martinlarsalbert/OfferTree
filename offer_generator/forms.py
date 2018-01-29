from django import forms

from .models import Item,ItemGroup


class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('name', 'price',)


class ItemGroupForm(forms.ModelForm):

    class Meta:
        model = ItemGroup
        #fields = ('sub_groups', 'sub_items',)
        fields = ('name',)