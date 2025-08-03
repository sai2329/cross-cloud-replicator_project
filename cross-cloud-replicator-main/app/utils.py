from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type
from botocore.exceptions import EndpointConnectionError
from google.api_core.exceptions import ServiceUnavailable

# Retry logic for transient network/cloud errors
retry_on_network_errors = retry(
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(3),
    retry=retry_if_exception_type((EndpointConnectionError, ServiceUnavailable)),
    reraise=True
)
