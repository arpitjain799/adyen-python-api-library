from ..base import AdyenServiceBase


class TerminalActionsCompanyLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TerminalActionsCompanyLevelApi, self).__init__(client=client)
        self.service = "management"

    def list_android_apps(self, companyId, idempotency_key=None, **kwargs):
        """
        Get a list of Android apps
        """
        endpoint = f"/companies/{companyId}/androidApps"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def list_android_certificates(self, companyId, idempotency_key=None, **kwargs):
        """
        Get a list of Android certificates
        """
        endpoint = f"/companies/{companyId}/androidCertificates"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def list_terminal_actions(self, companyId, idempotency_key=None, **kwargs):
        """
        Get a list of terminal actions
        """
        endpoint = f"/companies/{companyId}/terminalActions"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_terminal_action(self, companyId, actionId, idempotency_key=None, **kwargs):
        """
        Get terminal action
        """
        endpoint = f"/companies/{companyId}/terminalActions/{actionId}"
        endpoint = endpoint.replace('/', '', 1)
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

