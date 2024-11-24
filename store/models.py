from django.db import models

# Define choices
PLAN_CHOICES = [
    ('Basic', 'Basic Plan (Solo)'),
    ('Balanced', 'Balanced Plan (2 People)'),
    ('Family', 'Family Plan (4 People)'),
]

DIET_CHOICES = [
    ('Vegan', 'Vegan'),
    ('Non_Vegan', 'Non-Vegan'),
    ('No_Preference', 'No Preference'),
]

class GeneralInfo(models.Model):  # Class name corrected to use standard naming convention
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    delivery_address = models.TextField()
    selected_plan = models.CharField(
        max_length=50,
        choices=PLAN_CHOICES,
        default='Basic'
    )
    dietary_preference = models.CharField(
        max_length=50,
        choices=DIET_CHOICES,
        default='No_Preference'
    )
    Optional_Add_ons = models.TextField(blank=True, null=True)
    token_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.selected_plan} - {self.dietary_preference}"
