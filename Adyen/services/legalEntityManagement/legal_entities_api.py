from ..base import AdyenServiceBase


class LegalEntitiesApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(LegalEntitiesApi, self).__init__(client=client)
        self.service = "legalEntityManagement"

    def get_legal_entity(self, id, idempotency_key=None, **kwargs):
        """
        Get a legal entity
        """
        endpoint = f"/legalEntities/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_all_business_lines_under_legal_entity(self, id, idempotency_key=None, **kwargs):
        """
        Get all business lines under a legal entity
        """
        endpoint = f"/legalEntities/{id}/businessLines"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_legal_entity(self, request, id, idempotency_key=None, **kwargs):
        """
        Update a legal entity
        """
        endpoint = f"/legalEntities/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_legal_entity(self, request, idempotency_key=None, **kwargs):
        """
        Create a legal entity
        """
        endpoint = f"/legalEntities"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

