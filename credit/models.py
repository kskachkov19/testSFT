from django.db import models


class BaseCreditModel(models.Model):
    date = models.DateTimeField(auto_now_add=True, editable=False)    # or just (editable=False) - this is not clear in test_task

    class Meta:
        abstract = True


class Contract(BaseCreditModel):
    pass


class CreditRequest(BaseCreditModel):
    contract = models.ForeignKey('Contract', on_delete=models.CASCADE, related_name='credit_requests')


class Product(BaseCreditModel):
    credit_request = models.ForeignKey('CreditRequest', on_delete=models.CASCADE, related_name='products')
    producer = models.ForeignKey('Producer', on_delete=models.CASCADE, related_name='products')


class Producer(BaseCreditModel):
    name = models.CharField(max_length=255, unique=True)
