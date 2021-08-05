# openapi_client.RecipientsApi

All URIs are relative to *https://connect.sandbox.plastiq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recipients_get**](RecipientsApi.md#recipients_get) | **GET** /recipients | Retrieve a paginated list of Recipients by query parameter(s)
[**recipients_id_delete**](RecipientsApi.md#recipients_id_delete) | **DELETE** /recipients/{id} | Delete a Recipient
[**recipients_id_get**](RecipientsApi.md#recipients_id_get) | **GET** /recipients/{id} | Retrieve a Recipient
[**recipients_id_patch**](RecipientsApi.md#recipients_id_patch) | **PATCH** /recipients/{id} | Update a Recipient
[**recipients_post**](RecipientsApi.md#recipients_post) | **POST** /recipients | Create a Recipient


# **recipients_get**
> InlineResponse2004 recipients_get()

Retrieve a paginated list of Recipients by query parameter(s)

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import recipients_api
from openapi_client.model.inline_response2004 import InlineResponse2004
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
    api_instance = recipients_api.RecipientsApi(api_client)
    payer_id = "payerId_example" # str | List only Recipients associated with this Payer ID (optional)
    offset = 1 # int | The number of records you wish to skip before selecting records (optional)
    limit = 1 # int | Number of items to return (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a paginated list of Recipients by query parameter(s)
        api_response = api_instance.recipients_get(payer_id=payer_id, offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payer_id** | **str**| List only Recipients associated with this Payer ID | [optional]
 **offset** | **int**| The number of records you wish to skip before selecting records | [optional]
 **limit** | **int**| Number of items to return | [optional]

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Recipients |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipients_id_delete**
> recipients_id_delete(id)

Delete a Recipient

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import recipients_api
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
    api_instance = recipients_api.RecipientsApi(api_client)
    id = "id_example" # str | The ID of the Recipient
    payer_id = "payerId_example" # str | The ID of the Payer the Recipient is scoped to (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a Recipient
        api_instance.recipients_id_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_id_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a Recipient
        api_instance.recipients_id_delete(id, payer_id=payer_id)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Recipient |
 **payer_id** | **str**| The ID of the Payer the Recipient is scoped to | [optional]

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Recipient deleted successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipients_id_get**
> Recipient recipients_id_get(id)

Retrieve a Recipient

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import recipients_api
from openapi_client.model.error import Error
from openapi_client.model.recipient import Recipient
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
    api_instance = recipients_api.RecipientsApi(api_client)
    id = "id_example" # str | The ID of the Recipient
    payer_id = "payerId_example" # str | The ID of the Payer the Recipient is scoped to (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Recipient
        api_response = api_instance.recipients_id_get(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_id_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a Recipient
        api_response = api_instance.recipients_id_get(id, payer_id=payer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Recipient |
 **payer_id** | **str**| The ID of the Payer the Recipient is scoped to | [optional]

### Return type

[**Recipient**](Recipient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Recipient object |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipients_id_patch**
> Recipient recipients_id_patch(id, patch_recipient_request)

Update a Recipient

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import recipients_api
from openapi_client.model.patch_recipient_request import PatchRecipientRequest
from openapi_client.model.error import Error
from openapi_client.model.recipient import Recipient
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
    api_instance = recipients_api.RecipientsApi(api_client)
    id = "id_example" # str | The ID of the Recipient
    patch_recipient_request = PatchRecipientRequest(
        business_name="Coffee Beans Supply Co.",
        business_address={},
        contact=CreateRecipientRequestContact(
            first_name="Bob",
            last_name="Smith",
            email="bobsmith@coffeebean.supply",
            phone="4155550100",
        ),
        payer=PayerId(
            id="8f51c396-6e29-49a6-ba5a-1a31d5420158",
        ),
    ) # PatchRecipientRequest | Recipient to create

    # example passing only required values which don't have defaults set
    try:
        # Update a Recipient
        api_response = api_instance.recipients_id_patch(id, patch_recipient_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Recipient |
 **patch_recipient_request** | [**PatchRecipientRequest**](PatchRecipientRequest.md)| Recipient to create |

### Return type

[**Recipient**](Recipient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recipient updated successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recipients_post**
> Recipient recipients_post(create_recipient_request)

Create a Recipient

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import recipients_api
from openapi_client.model.create_recipient_request import CreateRecipientRequest
from openapi_client.model.error import Error
from openapi_client.model.recipient import Recipient
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
    api_instance = recipients_api.RecipientsApi(api_client)
    create_recipient_request = CreateRecipientRequest(
        business_name="Coffee Beans Supply Co.",
        category_id="d7a2beba-0c2c-42de-9690-26f00ba08339",
        business_address={},
        contact=CreateRecipientRequestContact(
            first_name="Bob",
            last_name="Smith",
            email="bobsmith@coffeebean.supply",
            phone="4155550100",
        ),
        receiving_method=,
        payer=PayerId(
            id="8f51c396-6e29-49a6-ba5a-1a31d5420158",
        ),
    ) # CreateRecipientRequest | Recipient to create
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Recipient
        api_response = api_instance.recipients_post(create_recipient_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Recipient
        api_response = api_instance.recipients_post(create_recipient_request, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RecipientsApi->recipients_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_recipient_request** | [**CreateRecipientRequest**](CreateRecipientRequest.md)| Recipient to create |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]

### Return type

[**Recipient**](Recipient.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Recipient created successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

