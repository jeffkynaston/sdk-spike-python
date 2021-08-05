# openapi_client.PaymentsApi

All URIs are relative to *https://connect.sandbox.plastiq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payment_intents_id_get**](PaymentsApi.md#payment_intents_id_get) | **GET** /payment-intents/{id} | Retrieve a single Payment Intent
[**payment_intents_id_patch**](PaymentsApi.md#payment_intents_id_patch) | **PATCH** /payment-intents/{id} | Update a Payment Intent
[**payment_intents_post**](PaymentsApi.md#payment_intents_post) | **POST** /payment-intents | Create a Payment Intent
[**payments_get**](PaymentsApi.md#payments_get) | **GET** /payments | Retrieve a paginated list of payments by query parameter(s)
[**payments_id_get**](PaymentsApi.md#payments_id_get) | **GET** /payments/{id} | Retrieve a single Payment
[**payments_id_refunds_post**](PaymentsApi.md#payments_id_refunds_post) | **POST** /payments/{id}/refunds | Refund or cancel an existing Payment
[**payments_post**](PaymentsApi.md#payments_post) | **POST** /payments | Create a Payment from a Payment Intent


# **payment_intents_id_get**
> PaymentIntent payment_intents_id_get(payer_id, id)

Retrieve a single Payment Intent

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payments_api
from openapi_client.model.error import Error
from openapi_client.model.payment_intent import PaymentIntent
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
    api_instance = payments_api.PaymentsApi(api_client)
    payer_id = "payerId_example" # str | The Payer ID of the Payment Intent
    id = "id_example" # str | The ID of the Payment Intent

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a single Payment Intent
        api_response = api_instance.payment_intents_id_get(payer_id, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payment_intents_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payer_id** | **str**| The Payer ID of the Payment Intent |
 **id** | **str**| The ID of the Payment Intent |

### Return type

[**PaymentIntent**](PaymentIntent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Payment Intent object |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_intents_id_patch**
> PaymentIntent payment_intents_id_patch(id, patch_payment_intent_request_payload)

Update a Payment Intent

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payments_api
from openapi_client.model.error import Error
from openapi_client.model.payment_intent import PaymentIntent
from openapi_client.model.patch_payment_intent_request_payload import PatchPaymentIntentRequestPayload
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
    api_instance = payments_api.PaymentsApi(api_client)
    id = "id_example" # str | The ID of the Payment Intent
    patch_payment_intent_request_payload = PatchPaymentIntentRequestPayload(
        target_amount=,
        details=PaymentDetails(
            account_name="Jen Doe",
            account_number="647823643287423",
            memo="Payment for Oct. coffee beans inventory",
        ),
        metadata={},
    ) # PatchPaymentIntentRequestPayload | Payment Intent to update

    # example passing only required values which don't have defaults set
    try:
        # Update a Payment Intent
        api_response = api_instance.payment_intents_id_patch(id, patch_payment_intent_request_payload)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payment_intents_id_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Payment Intent |
 **patch_payment_intent_request_payload** | [**PatchPaymentIntentRequestPayload**](PatchPaymentIntentRequestPayload.md)| Payment Intent to update |

### Return type

[**PaymentIntent**](PaymentIntent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment Intent updated successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payment_intents_post**
> PaymentIntent payment_intents_post(create_payment_intent_request_payload)

Create a Payment Intent

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payments_api
from openapi_client.model.create_payment_intent_request_payload import CreatePaymentIntentRequestPayload
from openapi_client.model.error import Error
from openapi_client.model.payment_intent import PaymentIntent
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
    api_instance = payments_api.PaymentsApi(api_client)
    create_payment_intent_request_payload = CreatePaymentIntentRequestPayload(
        target_amount=,
        payment_method=,
        recipient=,
        payer=,
        details=PaymentDetails(
            account_name="Jen Doe",
            account_number="647823643287423",
            memo="Payment for Oct. coffee beans inventory",
        ),
        metadata={},
    ) # CreatePaymentIntentRequestPayload | Create a Payment Intent object staging it for execution
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Payment Intent
        api_response = api_instance.payment_intents_post(create_payment_intent_request_payload)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payment_intents_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Payment Intent
        api_response = api_instance.payment_intents_post(create_payment_intent_request_payload, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payment_intents_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_intent_request_payload** | [**CreatePaymentIntentRequestPayload**](CreatePaymentIntentRequestPayload.md)| Create a Payment Intent object staging it for execution |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]

### Return type

[**PaymentIntent**](PaymentIntent.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment Intent created successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_get**
> InlineResponse2002 payments_get(payer_id)

Retrieve a paginated list of payments by query parameter(s)

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payments_api
from openapi_client.model.error import Error
from openapi_client.model.inline_response2002 import InlineResponse2002
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
    api_instance = payments_api.PaymentsApi(api_client)
    payer_id = "payerId_example" # str | The associated Payer ID to list payments for
    offset = 1 # int | The number of records you wish to skip before selecting records (optional)
    limit = 1 # int | Number of items to return (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a paginated list of payments by query parameter(s)
        api_response = api_instance.payments_get(payer_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a paginated list of payments by query parameter(s)
        api_response = api_instance.payments_get(payer_id, offset=offset, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payer_id** | **str**| The associated Payer ID to list payments for |
 **offset** | **int**| The number of records you wish to skip before selecting records | [optional]
 **limit** | **int**| Number of items to return | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Payments |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_get**
> Payment payments_id_get(payer_id, id)

Retrieve a single Payment

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payments_api
from openapi_client.model.payment import Payment
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
    api_instance = payments_api.PaymentsApi(api_client)
    payer_id = "payerId_example" # str | The Payer ID associated with the Payment
    id = "id_example" # str | The ID of the Payment

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a single Payment
        api_response = api_instance.payments_id_get(payer_id, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payer_id** | **str**| The Payer ID associated with the Payment |
 **id** | **str**| The ID of the Payment |

### Return type

[**Payment**](Payment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Payment object |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_id_refunds_post**
> PaymentRefund payments_id_refunds_post(id, payment_refund_request)

Refund or cancel an existing Payment

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payments_api
from openapi_client.model.payment_refund import PaymentRefund
from openapi_client.model.error import Error
from openapi_client.model.payment_refund_request import PaymentRefundRequest
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
    api_instance = payments_api.PaymentsApi(api_client)
    id = "id_example" # str | The ID of the Payment to refund
    payment_refund_request = PaymentRefundRequest(
        payer_id="2e571899-5ba6-4779-9267-899f0cb95c1f",
    ) # PaymentRefundRequest | Payment Refund body
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Refund or cancel an existing Payment
        api_response = api_instance.payments_id_refunds_post(id, payment_refund_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_id_refunds_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Refund or cancel an existing Payment
        api_response = api_instance.payments_id_refunds_post(id, payment_refund_request, trace_id=trace_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_id_refunds_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Payment to refund |
 **payment_refund_request** | [**PaymentRefundRequest**](PaymentRefundRequest.md)| Payment Refund body |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]

### Return type

[**PaymentRefund**](PaymentRefund.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment refunded successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payments_post**
> Payment payments_post(create_payment_request)

Create a Payment from a Payment Intent

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import payments_api
from openapi_client.model.create_payment_request import CreatePaymentRequest
from openapi_client.model.payment import Payment
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
    api_instance = payments_api.PaymentsApi(api_client)
    create_payment_request = CreatePaymentRequest() # CreatePaymentRequest | Payment to create
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    idempotency_key = "Idempotency-Key_example" # str | A valid UUID (V4) for handling duplicate requests. Will return original status code, response body, and set a 'Idempotent-Replay' header on response for a given key if a match exists. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Payment from a Payment Intent
        api_response = api_instance.payments_post(create_payment_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Payment from a Payment Intent
        api_response = api_instance.payments_post(create_payment_request, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip, idempotency_key=idempotency_key)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling PaymentsApi->payments_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payment_request** | [**CreatePaymentRequest**](CreatePaymentRequest.md)| Payment to create |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **idempotency_key** | **str**| A valid UUID (V4) for handling duplicate requests. Will return original status code, response body, and set a &#39;Idempotent-Replay&#39; header on response for a given key if a match exists. | [optional]

### Return type

[**Payment**](Payment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payment created successfully |  * Trace-Id - The trace ID for the request <br>  * Idempotent-Replay - Returned if an Idempotency-Key header was provided on the request and a match was found and returned. <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

