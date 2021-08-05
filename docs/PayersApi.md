# openapi_client.PayersApi

All URIs are relative to *https://connect.sandbox.plastiq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payers_id_delete**](PayersApi.md#payers_id_delete) | **DELETE** /payers/{id} | Delete a Payer
[**payers_id_get**](PayersApi.md#payers_id_get) | **GET** /payers/{id} | Retrieve a Payer
[**payers_id_patch**](PayersApi.md#payers_id_patch) | **PATCH** /payers/{id} | Update a Payer
[**payers_post**](PayersApi.md#payers_post) | **POST** /payers | Create a Payer


# **payers_id_delete**
> payers_id_delete(id)

Delete a Payer

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payers_api
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
    api_instance = payers_api.PayersApi(api_client)
    id = "id_example" # str | The ID of the Payer

    # example passing only required values which don't have defaults set
    try:
        # Delete a Payer
        api_instance.payers_id_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling PayersApi->payers_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Payer |

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
**204** | Payer deleted successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payers_id_get**
> Payer payers_id_get(id)

Retrieve a Payer

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payers_api
from openapi_client.model.payer import Payer
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
    api_instance = payers_api.PayersApi(api_client)
    id = "id_example" # str | The ID of the Payer

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Payer
        api_response = api_instance.payers_id_get(id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PayersApi->payers_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Payer |

### Return type

[**Payer**](Payer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payer retrieved successfully. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payers_id_patch**
> Payer payers_id_patch(id, update_payer_request)

Update a Payer

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payers_api
from openapi_client.model.payer import Payer
from openapi_client.model.update_payer_request import UpdatePayerRequest
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
    api_instance = payers_api.PayersApi(api_client)
    id = "id_example" # str | The ID of the Payer
    update_payer_request = UpdatePayerRequest(
        business_name="Philz Coffee",
        contact=Contact(),
        business_address={},
        identity_documents=[
            ,
        ],
    ) # UpdatePayerRequest | Payer to update

    # example passing only required values which don't have defaults set
    try:
        # Update a Payer
        api_response = api_instance.payers_id_patch(id, update_payer_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PayersApi->payers_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Payer |
 **update_payer_request** | [**UpdatePayerRequest**](UpdatePayerRequest.md)| Payer to update |

### Return type

[**Payer**](Payer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payer updated successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payers_post**
> Payer payers_post(create_payer_request)

Create a Payer

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payers_api
from openapi_client.model.payer import Payer
from openapi_client.model.error import Error
from openapi_client.model.create_payer_request import CreatePayerRequest
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
    api_instance = payers_api.PayersApi(api_client)
    create_payer_request = CreatePayerRequest(
        business_name="Philz Coffee",
        contact=Contact(),
        business_address={},
        identity_documents=[
            ,
        ],
    ) # CreatePayerRequest | Payer to create
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Payer
        api_response = api_instance.payers_post(create_payer_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PayersApi->payers_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Payer
        api_response = api_instance.payers_post(create_payer_request, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PayersApi->payers_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payer_request** | [**CreatePayerRequest**](CreatePayerRequest.md)| Payer to create |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]

### Return type

[**Payer**](Payer.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payer created successfully. |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

