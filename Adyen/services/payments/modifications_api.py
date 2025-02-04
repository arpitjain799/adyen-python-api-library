from ..base import AdyenServiceBase


class ModificationsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(ModificationsApi, self).__init__(client=client)
        self.service = "payments"

    def adjust_authorisation(self, request, idempotency_key=None, **kwargs):
        """
        Change the authorised amount
        """
        endpoint = f"/adjustAuthorisation"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def cancel(self, request, idempotency_key=None, **kwargs):
        """
        Cancel an authorisation
        """
        endpoint = f"/cancel"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def cancel_or_refund(self, request, idempotency_key=None, **kwargs):
        """
        Cancel or refund a payment
        """
        endpoint = f"/cancelOrRefund"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def capture(self, request, idempotency_key=None, **kwargs):
        """
        Capture an authorisation
        """
        endpoint = f"/capture"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def donate(self, request, idempotency_key=None, **kwargs):
        """
        Create a donation
        """
        endpoint = f"/donate"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def refund(self, request, idempotency_key=None, **kwargs):
        """
        Refund a captured payment
        """
        endpoint = f"/refund"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def technical_cancel(self, request, idempotency_key=None, **kwargs):
        """
        Cancel an authorisation using your reference
        """
        endpoint = f"/technicalCancel"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def void_pending_refund(self, request, idempotency_key=None, **kwargs):
        """
        Cancel an in-person refund
        """
        endpoint = f"/voidPendingRefund"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

