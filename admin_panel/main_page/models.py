from django.db import models

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    textarea = models.TextField()

    def __str__(self):
        str_name = f"Имя: {self.name}, Почта: {self.email}"
        return str_name

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

