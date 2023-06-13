from typing import List

from django.http import JsonResponse

from credit import services


def list_contracts_view(request):
    contracts = services.list_contracts()
    return JsonResponse({
        'contracts': list(contracts),
    })


def list_producer_ids_by_contract_view(request, contract_id: id):
    producer_ids = services.list_producer_ids_by_contract_id(contract_id)
    return JsonResponse({
        'contract_id': contract_id,
        'producer_ids': list(producer_ids),
    })
