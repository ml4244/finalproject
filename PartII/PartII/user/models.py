from django.db import models

# Create your models here.
class Squirrel(models.Model):
    unique_squirrel_id = models.CharField(primary_key=True,max_length=500, null=False)
    x = models.CharField(max_length=500, null=True, blank=True)
    y = models.CharField(max_length=500, null=True, blank=True)
    hectare = models.CharField(max_length=500, null=True, blank=True)
    shift = models.CharField(max_length=500, null=True, blank=True)
    date = models.CharField(max_length=500, null=True, blank=True)
    hectare_squirrel_number = models.CharField(max_length=500, null=True, blank=True)
    age = models.CharField(max_length=500, null=True, blank=True)
    primary_fur_color = models.CharField(max_length=500, null=True, blank=True)
    highlight_fur_color = models.CharField(max_length=500, null=True, blank=True)
    combination_of_primary_and_highlight = models.CharField(max_length=500, null=True, blank=True)
    color_notes = models.CharField(max_length=500, null=True, blank=True)
    location = models.CharField(max_length=500, null=True, blank=True)
    above_ground_sighter_measurement = models.CharField(max_length=500, null=True, blank=True)
    specific_location = models.CharField(max_length=500, null=True, blank=True)
    running = models.CharField(max_length=500, null=True, blank=True)
    chasing = models.CharField(max_length=500, null=True, blank=True)
    climbing = models.CharField(max_length=500, null=True, blank=True)
    eating = models.CharField(max_length=500, null=True, blank=True)
    foraging = models.CharField(max_length=500, null=True, blank=True)
    other_activities = models.CharField(max_length=500, null=True, blank=True)
    kuks = models.CharField(max_length=500, null=True, blank=True)
    quaas = models.CharField(max_length=500, null=True, blank=True)
    moans = models.CharField(max_length=500, null=True, blank=True)
    tail_flags = models.CharField(max_length=500, null=True, blank=True)
    tail_twitches = models.CharField(max_length=500, null=True, blank=True)
    approaches = models.CharField(max_length=500, null=True, blank=True)
    indifferent = models.CharField(max_length=500, null=True, blank=True)
    runs_from = models.CharField(max_length=500, null=True, blank=True)
    other_interactions = models.CharField(max_length=500, null=True, blank=True)
    lat_long = models.CharField(max_length=500, null=True, blank=True)

    def getName(self):
        return self.unique_squirrel_id

    class Meta:
        # ordering = ["-c_time"]
        verbose_name = "squirrel"
        verbose_name_plural = "squirrel"
