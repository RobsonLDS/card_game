from django.db import models

class Card(models.Model):
    name = models.TextField(null=True, blank=True)
    auto_descricao = models.TextField(null=True, blank=True)

    vidas = models.IntegerField(null=True, blank=True)
    potencia = models.IntegerField(null=True, blank=True)
    habilidade = models.IntegerField(null=True, blank=True)
    razao = models.IntegerField(null=True, blank=True)
    esperanca = models.IntegerField(null=True, blank=True)
    alma = models.IntegerField(null=True, blank=True)
    vontade = models.IntegerField(null=True, blank=True)

    especial_descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_nome(self):
        return self.name

    def get_id(self):
        return self.id

    def get_descricao(self):
        return self.auto_descricao

    def get_vidas(self):
        return self.vidas

    def get_pot(self):
        return self.potencia

    def get_hab(self):
        return self.habilidade

    def get_raz(self):
        return self.razao

    def get_esp(self):
        return self.esperanca

    def get_alm(self):
        return self.alma

    def get_von(self):
        return self.vontade

    def get_especial(self):
        return self.especial_descricao