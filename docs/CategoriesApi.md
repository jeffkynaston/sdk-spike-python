# openapi_client.CategoriesApi

All URIs are relative to *https://connect.sandbox.plastiq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categories_get**](CategoriesApi.md#categories_get) | **GET** /categories | Retrieve a paginated list of Categories by query parameter(s)


# **categories_get**
> InlineResponse200 categories_get()

Retrieve a paginated list of Categories by query parameter(s)

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import categories_api
from openapi_client.model.error import Error
from openapi_client.model.inline_response200 import InlineResponse200
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
    api_instance = categories_api.CategoriesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Retrieve a paginated list of Categories by query parameter(s)
        api_response = api_instance.categories_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CategoriesApi->categories_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Categories |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**404** | Not found |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

