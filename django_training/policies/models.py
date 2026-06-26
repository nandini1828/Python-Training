from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Policy(models.Model):
    policy_number = models.CharField(max_length=50)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="policies"
    )
    premium = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.policy_number


class Claim(models.Model):
    claim_number = models.CharField(max_length=20)
    policy = models.ForeignKey(
        Policy,
        on_delete=models.CASCADE,
        related_name="claims"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.claim_number