from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Roster(models.Model):
    positions = [
        ("QB", "Quarterback"),
        ("RB", "Running Back"),
        ("FB", "Fullback"),
        ("WR", "Wide Receiver"),
        ("TE", "Tight End"),
        ("OL", "Offensive Line"),
        ("DL", "Defensive Line"),
        ("LB", "Linebacker"),
        ("CB", "Cornerback"),
        ("S", "Safety")
    ]

    name = models.CharField(max_length=64)
    position = models.CharField(max_length=2, choices = positions, default="QB")
    depth = models.IntegerField()
    coach = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
