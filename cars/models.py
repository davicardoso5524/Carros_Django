from django.db import models
# blank=true = pode deixar o campo em branco e null=True pode deixar null 

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200) # String # max_lenght = maximo de caracteres

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True) # Campo que se auto incrementa, id 1, id 2...
    model = models.CharField(max_length=200) 
    # ForeignKey = chave estrangeir, seria a ligação com outra tabela, logo o primeiro campo é o nome da tabela
    # on_delete = A ligação nesse caso, estará em modo PROTECT, caso seja deletada | tem tbm o CASCADE, que irá deletar todos os carros relacionados a marca
    # related_name = o nome da relação entre car e brand, car_brand 
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True) # Campo inteiro
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True) # Campo de ponto flutuante, R$ 112312, 123123
    # ImageField = Faz o upload da imagem para uma pasta, no caso dentro da pasta cars, e vai gerar uma pasta com uploads dessas imagens
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'