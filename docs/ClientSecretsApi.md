# openapi_client.ClientSecretsApi

All URIs are relative to *https://connect.sandbox.plastiq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_secrets_post**](ClientSecretsApi.md#client_secrets_post) | **POST** /client-secrets | Create a single-use Client Secret


# **client_secrets_post**
> InlineResponse2001 client_secrets_post(inline_object)

Create a single-use Client Secret

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import client_secrets_api
from openapi_client.model.inline_object import InlineObject
from openapi_client.model.inline_response2001 import InlineResponse2001
from openapi_client.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://connect.sandbox.plastiq.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://connect.sandbox.plastiq.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (token): BearerAuth
configuration = openapi_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = client_secrets_api.ClientSecretsApi(api_client)
    inline_object = InlineObject(
        payer=PayerId(
            id="8f51c396-6e29-49a6-ba5a-1a31d5420158",
        ),
        type="CARD",
    ) # InlineObject | 
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a single-use Client Secret
        api_response = api_instance.client_secrets_post(inline_object)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientSecretsApi->client_secrets_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a single-use Client Secret
        api_response = api_instance.client_secrets_post(inline_object, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClientSecretsApi->client_secrets_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **inline_object** | [**InlineObject**](InlineObject.md)|  |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client Secret created successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

