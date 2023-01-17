from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TodoList(models.Model):
    status_choices = (
        ("FA", "⛔️ a Fazer"),
        ("RE", "⚠️ Fazendo"),
        ("FI", "✅ Finalizado"),
    )

    dono = models.ForeignKey(User, verbose_name=("autor"), on_delete=models.CASCADE)
    title = models.CharField(max_length=100, null=False, blank=False)
    como = models.CharField(max_length=2, choices=status_choices, default='FA')
    datacriacao = models.DateTimeField(("date joined"), default=timezone.now)
        
    def __str__(self):
        return self.title

    def to_dict(self):
        return {
            'title': self.title,
            'como': self.como ,
            'datacriacao': self.datacriacao ,
        }