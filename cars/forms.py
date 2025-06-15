from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    # Precisamos subscrever a classe Meta do form
    class Meta:
        # O model irá receber o nosso modelo Car
        model = Car
        # Com isso ele irá pegar todos os campos do nosso model Car
        # Fields = Campo
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possivel cadastrar carros fabricados antes de 1975')
        return factory_year







"""
class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    # Modelchoicefield = Mostrar a lista de opçoes disponiveis
    # Brand.objects.all = Traga todos os modelos de carros do Objeto
    brand = forms.ModelChoiceField(Brand.objects.all())
    factory_year = forms.IntegerField()
    model_year = forms.IntegerField()
    plate = forms.CharField(max_length=10)
    value = forms.FloatField()
    photo = forms.ImageField()

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo'],
        )
        car.save()
        return car
    
"""

