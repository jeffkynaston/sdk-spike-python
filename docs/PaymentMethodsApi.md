# openapi_client.PaymentMethodsApi

All URIs are relative to *https://connect.sandbox.plastiq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_methods_get**](PaymentMethodsApi.md#payment_methods_get) | **GET** /payment-methods | Retrieve a paginated list of Payment Methods by query parameter(s)
[**payment_methods_id_delete**](PaymentMethodsApi.md#payment_methods_id_delete) | **DELETE** /payment-methods/{id} | Delete a Payment Method
[**payment_methods_id_get**](PaymentMethodsApi.md#payment_methods_id_get) | **GET** /payment-methods/{id} | Retrieve a Payment Method
[**payment_methods_id_patch**](PaymentMethodsApi.md#payment_methods_id_patch) | **PATCH** /payment-methods/{id} | Update a Payment Method
[**payment_methods_post**](PaymentMethodsApi.md#payment_methods_post) | **POST** /payment-methods | Create a Payment Method


# **payment_methods_get**
> InlineResponse2003 payment_methods_get(payer_id)

Retrieve a paginated list of Payment Methods by query parameter(s)

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.inline_response2003 import InlineResponse2003
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
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    payer_id = "payerId_example" # str | The associated Payer ID to list Payment Methods for
    offset = 1 # int | The number of records you wish to skip before selecting records (optional)
    limit = 1 # int | Number of items to return (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a paginated list of Payment Methods by query parameter(s)
        api_response = api_instance.payment_methods_get(payer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a paginated list of Payment Methods by query parameter(s)
        api_response = api_instance.payment_methods_get(payer_id, offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payer_id** | **str**| The associated Payer ID to list Payment Methods for |
 **offset** | **int**| The number of records you wish to skip before selecting records | [optional]
 **limit** | **int**| Number of items to return | [optional]

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Payment Methods |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_methods_id_delete**
> payment_methods_id_delete(id)

Delete a Payment Method

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
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
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    id = "id_example" # str | The ID of the Payment Method

    # example passing only required values which don't have defaults set
    try:
        # Delete a Payment Method
        api_instance.payment_methods_id_delete(id)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_id_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Payment Method |

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
**204** | Payment Method deleted successfully |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_methods_id_get**
> PaymentMethod payment_methods_id_get(payer_id, id)

Retrieve a Payment Method

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.error import Error
from openapi_client.model.payment_method import PaymentMethod
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
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    payer_id = "payerId_example" # str | The Payer ID associated to the Payment Method
    id = "id_example" # str | The ID of the Payment Method

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a Payment Method
        api_response = api_instance.payment_methods_id_get(payer_id, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payer_id** | **str**| The Payer ID associated to the Payment Method |
 **id** | **str**| The ID of the Payment Method |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Payment Method object |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_methods_id_patch**
> PaymentMethod payment_methods_id_patch(id, patch_payment_method_request)

Update a Payment Method

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.patch_payment_method_request import PatchPaymentMethodRequest
from openapi_client.model.error import Error
from openapi_client.model.payment_method import PaymentMethod
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
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    id = "id_example" # str | The ID of the Payment Method
    patch_payment_method_request = PatchPaymentMethodRequest(
        type="CARD",
        data=,
        payer=PayerId(
            id="8f51c396-6e29-49a6-ba5a-1a31d5420158",
        ),
    ) # PatchPaymentMethodRequest | Payment Method to update
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Payment Method
        api_response = api_instance.payment_methods_id_patch(id, patch_payment_method_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_id_patch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Payment Method
        api_response = api_instance.payment_methods_id_patch(id, patch_payment_method_request, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Payment Method |
 **patch_payment_method_request** | [**PatchPaymentMethodRequest**](PatchPaymentMethodRequest.md)| Payment Method to update |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment Method updated successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_methods_post**
> PaymentMethod payment_methods_post(create_payment_method_request)

Create a Payment Method

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payment_methods_api
from openapi_client.model.error import Error
from openapi_client.model.create_payment_method_request import CreatePaymentMethodRequest
from openapi_client.model.payment_method import PaymentMethod
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
    api_instance = payment_methods_api.PaymentMethodsApi(api_client)
    create_payment_method_request = CreatePaymentMethodRequest(
        type="CARD",
        data=,
        payer=,
    ) # CreatePaymentMethodRequest | Payment Method to create
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Payment Method
        api_response = api_instance.payment_methods_post(create_payment_method_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Payment Method
        api_response = api_instance.payment_methods_post(create_payment_method_request, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentMethodsApi->payment_methods_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_method_request** | [**CreatePaymentMethodRequest**](CreatePaymentMethodRequest.md)| Payment Method to create |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment Method created successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

