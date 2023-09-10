from django.db import models
from django.urls import reverse


class Journal(models.Model):
    class Meta:
        db_table = "Journals"

    title = models.CharField(max_length=100)
    date = models.DateField()
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})


class SubJournals(models.Model):
    class Meta:
        db_table = "SubJournals"

    parent = models.ForeignKey(Journal, on_delete=models.CASCADE, to_field="id")
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to="subjournal_images")
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
