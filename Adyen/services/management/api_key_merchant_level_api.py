from ..base import AdyenServiceBase


class APIKeyMerchantLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(APIKeyMerchantLevelApi, self).__init__(client=client)
        self.service = "management"

    def generate_new_api_key(self, merchantId, apiCredentialId, idempotency_key=None, **kwargs):
        """
        Generate new API key
        """
        endpoint = f"/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey"
        method = "POST"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

