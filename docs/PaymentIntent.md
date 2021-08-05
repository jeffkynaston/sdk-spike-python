# PaymentIntent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**fees** | [**[PaymentIntentFees]**](PaymentIntentFees.md) |  | [optional] 
**source_amount** | **dict** |  | [optional] 
**target_amount** | **dict** |  | [optional] 
**payment_method** | [**PaymentMethodId**](PaymentMethodId.md) |  | [optional] 
**recipient** | [**RecipientId**](RecipientId.md) |  | [optional] 
**payer** | [**PayerId**](PayerId.md) |  | [optional] 
**details** | [**PaymentDetails**](PaymentDetails.md) |  | [optional] 
**status** | **str** |  | [optional] 
**status_reasons** | **[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]** |  | [optional] 
**delivery_date** | **date** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


