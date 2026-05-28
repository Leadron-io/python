"""SDK exceptions."""


class LeadronError(Exception):
    def __init__(self, message="", status_code=None, response_body=None):
        super().__init__(message)
        self.status_code = status_code
        self.response_body = response_body


class LeadronAuthError(LeadronError):
    pass


class LeadronValidationError(LeadronError):
    pass


class LeadronRateLimitError(LeadronError):
    def __init__(self, message="", retry_after=60, status_code=429, response_body=None):
        super().__init__(message, status_code, response_body)
        self.retry_after = retry_after
