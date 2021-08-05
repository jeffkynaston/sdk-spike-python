# openapi_client.DocumentsApi

All URIs are relative to *https://connect.sandbox.plastiq.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_post**](DocumentsApi.md#documents_post) | **POST** /documents | Upload a document


# **documents_post**
> DocumentUpload documents_post(create_document_upload_request)

Upload a document

### Example

* Bearer (token) Authentication (BearerAuth):
```python
import time
import openapi_client
from openapi_client.api import documents_api
from openapi_client.model.error import Error
from openapi_client.model.create_document_upload_request import CreateDocumentUploadRequest
from openapi_client.model.document_upload import DocumentUpload
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
    api_instance = documents_api.DocumentsApi(api_client)
    create_document_upload_request = CreateDocumentUploadRequest(
        payer=PayerId(
            id="8f51c396-6e29-49a6-ba5a-1a31d5420158",
        ),
        type="INVOICE",
        file_type="doc",
        filename="invoice_123.pdf",
    ) # CreateDocumentUploadRequest | Document metadata
    trace_id = "Trace-Id_example" # str | A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. (optional)
    user_agent = "User-Agent_example" # str | A string representing the User Agent. Required only when the request is not coming from the end user's browser. (optional)
    end_user_device_id = "End-User-Device-Id_example" # str | A unique identifier for the end user's browser. Recommended for compliance when the request is not coming from the end user's browser. (optional)
    end_user_ip = "End-User-Ip_example" # str | The IP address of the end user. Recommended for compliance when the request is not coming from the end user's browser. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a document
        api_response = api_instance.documents_post(create_document_upload_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a document
        api_response = api_instance.documents_post(create_document_upload_request, trace_id=trace_id, user_agent=user_agent, end_user_device_id=end_user_device_id, end_user_ip=end_user_ip)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentsApi->documents_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_document_upload_request** | [**CreateDocumentUploadRequest**](CreateDocumentUploadRequest.md)| Document metadata |
 **trace_id** | **str**| A valid UUID (V4) for tracing requests. Will be returned as a header. If not present or invalid, a generated UUID will be returned. | [optional]
 **user_agent** | **str**| A string representing the User Agent. Required only when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_device_id** | **str**| A unique identifier for the end user&#39;s browser. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]
 **end_user_ip** | **str**| The IP address of the end user. Recommended for compliance when the request is not coming from the end user&#39;s browser. | [optional]

### Return type

[**DocumentUpload**](DocumentUpload.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document upload URL generated successfully |  * Trace-Id - The trace ID for the request <br>  |
**400** | Bad Request |  * Trace-Id - The trace ID for the request <br>  |
**401** | Unauthorized |  * Trace-Id - The trace ID for the request <br>  |
**403** | Forbidden |  * Trace-Id - The trace ID for the request <br>  |
**500** | Internal Server Error |  * Trace-Id - The trace ID for the request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

