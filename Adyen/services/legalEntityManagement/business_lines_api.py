from ..base import AdyenServiceBase


class BusinessLinesApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(BusinessLinesApi, self).__init__(client=client)
        self.service = "legalEntityManagement"

    def delete_business_line(self, id, idempotency_key=None, **kwargs):
        """
        Delete a business line
        """
        endpoint = f"/businessLines/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_business_line(self, id, idempotency_key=None, **kwargs):
        """
        Get a business line
        """
        endpoint = f"/businessLines/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_business_line(self, request, id, idempotency_key=None, **kwargs):
        """
        Update a business line
        """
        endpoint = f"/businessLines/{id}"
        endpoint = endpoint.replace('/', '', 1)
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_business_line(self, request, idempotency_key=None, **kwargs):
        """
        Create a business line
        """
        endpoint = f"/businessLines"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

