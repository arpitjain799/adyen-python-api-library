from ..base import AdyenServiceBase


class TerminalActionsTerminalLevelApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(TerminalActionsTerminalLevelApi, self).__init__(client=client)
        self.service = "management"

    def create_terminal_action(self, request, idempotency_key=None, **kwargs):
        """
        Create a terminal action
        """
        endpoint = f"/terminals/scheduleActions"
        endpoint = endpoint.replace('/', '', 1)
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

