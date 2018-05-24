# swagger_client.DefaultApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**registration_api_bots_get**](DefaultApi.md#registration_api_bots_get) | **GET** /registration/api/bots/ | 


# **registration_api_bots_get**
> Model0 registration_api_bots_get()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.registration_api_bots_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->registration_api_bots_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Model0**](Model0.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

