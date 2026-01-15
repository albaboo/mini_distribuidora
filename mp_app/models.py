from django.db import models

# Create your models here.

Estat = ((0,'PENDENT'), (1,'EN_PREPARACIO'), (2,'ENVIAT'), (3,'ENTREGAT'), (4, 'CANCELAT'))

class Client(models.Model):
    codi_client = models.CharField(unique=True)
    nom_comercial = models.CharField()
    cif = models.CharField()
    persona_contacte = models.CharField()
    telefon = models.CharField()
    email = models.CharField()
    adreca_entrega = models.CharField()
    poblacio = models.CharField()
    codi_postal = models.CharField()
    actiu = models.BooleanField(default=True)

class Albara(models.Model):
    numero_albara = models.CharField(unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='albarans')
    data_creacio = models.DateTimeField(auto_now_add=True)
    data_entrega_prevista = models.DateTimeField()
    estat = models.CharField(choices=Estat)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    observacions = models.TextField(null=True, blank=True)

class LineaAlbara(models.Model):
    albara = models.ForeignKey(Albara, on_delete=models.CASCADE, related_name='lineas')
    nom_producte = models.CharField()
    quantitat = models.IntegerField()
    preu_unitari = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(null=True, blank=True)