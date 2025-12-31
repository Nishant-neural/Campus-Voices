from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):
    CATEGORY_CHOICES = [
        ('Hostel', 'Hostel'),
        ('Mess', 'Mess'),
        ('Academics', 'Academics'),
        ('Infrastructure', 'Infrastructure'),
        ('Safety', 'Safety'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def vote_count(self):
        return self.votes.count()

    def __str__(self):
        return self.title


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, related_name="votes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'issue')