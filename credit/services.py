import logging
from typing import List, Any, Dict

from credit.models import Producer, Contract, CreditRequest

logger = logging.getLogger('django')


def list_contracts():
    contracts = Contract.objects.all().values()
    logger.info(f'SQL query to get contracts list')
    logger.info(contracts.query)
    logger.info('-'*70)
    return contracts


def list_producer_ids_by_contract_id(contract_id: int):
    credit_request = CreditRequest.objects.filter(contract_id=contract_id).values_list('products__producer_id')
    logger.info(f'SQL query to get contracts list related with CreditRequest<contract_id={contract_id}>')
    logger.info(credit_request.query)
    logger.info('-' * 70)
    return credit_request
