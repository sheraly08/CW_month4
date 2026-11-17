from django import forms
from Ad.models import Ad, Category


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ("title", "description", "price", "category")


    


    def clean_title(self):
        title = self.cleaned_data['title']
        

        if len(title) < 5:
            raise forms.ValidationError("Минимум  5 символов")

       
        

        return title

    def clean_description(self):
        description = self.cleaned_data["description"]

        if len(description) < 10:
            raise forms.ValidationError("Опишите подробнее — минимум 10 символов")

        return description
        

        



    def clean_price(self):
        price = self.cleaned_data['price']

        if price is not None and price <= 0:
            raise forms.ValidationError("Цена должна быть больше нуля ") 


        return price 
        



