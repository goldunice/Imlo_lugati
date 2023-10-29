from django.db import models


class Togri(models.Model):
    t_soz = models.CharField(max_length=255)

    def __str__(self):
        return self.t_soz


class Notogri(models.Model):
    n_soz = models.CharField(max_length=255)
    t_id = models.ForeignKey(Togri, on_delete=models.CASCADE)

    def __str__(self):
        return self.n_soz
