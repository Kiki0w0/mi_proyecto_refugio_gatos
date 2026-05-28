from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre


class Gato(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="categoría",
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=20)
    disponibilidad = models.BooleanField(default=True)
    fecha_actualizacion = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self) -> str:
        return f"{self.nombre} - {self.edad} años"

    class Meta:
        verbose_name = "Gato"
        verbose_name_plural = "Gatos"
        # La siguiente línea es para que no se puedan repetir el nombre y la categoría
        constraints = [
            models.UniqueConstraint(
                fields=["categoria", "nombre"], name="categoria_nombre"
            )
        ]
        # La siguiente línea es para crear un índice en la base de datos
        # Un ínidice es una estructura de datos que mejora la velocidad de búsqueda
        indexes = [models.Index(fields=["nombre"])]



class SolicitudAdopcion(models.Model):
    gato = models.ForeignKey(Gato, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitud de {self.nombre}"        