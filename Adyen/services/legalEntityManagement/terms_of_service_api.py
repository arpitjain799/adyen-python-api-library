from ..base import AdyenServiceBase


class TermsOfServiceApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TermsOfServiceApi, self).__init__(client=client)
        self.service = "legalEntityManagement"

    def get_terms_of_service_information_for_legal_entity(self, id, idempotency_key=None, **kwargs):
        """
        Get Terms of Service information for a legal entity
        """
        endpoint = f"/legalEntities/{id}/termsOfServiceAcceptanceInfos"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_terms_of_service_status(self, id, idempotency_key=None, **kwargs):
        """
        Get Terms of Service status
        """
        endpoint = f"/legalEntities/{id}/termsOfServiceStatus"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def accept_terms_of_service(self, request, id, termsofservicedocumentid, idempotency_key=None, **kwargs):
        """
        Accept Terms of Service
        """
        endpoint = f"/legalEntities/{id}/termsOfService/{termsofservicedocumentid}"
        endpoint = endpoint.replace('/', '', 1)
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_terms_of_service_document(self, request, id, idempotency_key=None, **kwargs):
        """
        Get Terms of Service document
        """
        endpoint = f"/legalEntities/{id}/termsOfService"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

