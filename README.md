<div align="left">

[![Visit Payfactory](./header.png)](https://payfactory.io&#x2F;)

# Payfactory<a id="payfactory"></a>

Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`payfactory.application.create_new_application`](#payfactoryapplicationcreate_new_application)
  * [`payfactory.application.get_application_details`](#payfactoryapplicationget_application_details)
  * [`payfactory.application.get_application_status`](#payfactoryapplicationget_application_status)
  * [`payfactory.application.remove_by_id`](#payfactoryapplicationremove_by_id)
  * [`payfactory.application.start_underwriting_process`](#payfactoryapplicationstart_underwriting_process)
  * [`payfactory.application_form.create_session`](#payfactoryapplication_formcreate_session)
  * [`payfactory.application_form.get_session_info`](#payfactoryapplication_formget_session_info)
  * [`payfactory.application_form.update_session_activity`](#payfactoryapplication_formupdate_session_activity)
  * [`payfactory.document.upload_agreement`](#payfactorydocumentupload_agreement)
  * [`payfactory.reporting.get_ach_transactions_by_reference_id`](#payfactoryreportingget_ach_transactions_by_reference_id)
  * [`payfactory.reporting.get_deposits`](#payfactoryreportingget_deposits)
  * [`payfactory.reporting.get_deposits_by_count`](#payfactoryreportingget_deposits_by_count)
  * [`payfactory.reporting.get_deposits_by_reference_id`](#payfactoryreportingget_deposits_by_reference_id)
  * [`payfactory.transaction.create_metadata`](#payfactorytransactioncreate_metadata)
  * [`payfactory.transaction.create_metadata_bulk`](#payfactorytransactioncreate_metadata_bulk)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Payfactory&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from payfactory_python_sdk import Payfactory, ApiException

payfactory = Payfactory(

        api_key = 'YOUR_API_KEY',
)

try:
    # Submit a new Application
    create_new_application_response = payfactory.application.create_new_application(
        isv_name="aaa",
        business_details={
        "address": {
            "street1": "125 West Third Street 1st Floor",
            "city": "Tulsa",
            "state": "OK",
            "zip": "74555",
        },
        "phone": "5551234567",
        "established_date": "1959-02-03",
        "legal_name": "ACME LLC.",
        "dba_name": "ACME",
        "tax_id": "123456789",
        "website": "https://www.acme.com",
        "mcc": 7297,
        "ownership_type": "Unknown",
    },
        customer_service_contact={
        "phone": "5551234567",
        "email": "test@test.com",
    },
        risk_contact={
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
    },
        business_contact={
        "title": "CEO",
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
        "phone": "5551234567",
        "dob": "1947-03-25",
        "ssn": "5554449999",
    },
        processing_details={
        "billing_descriptor": "ACME_WEST_POS",
        "monthly_transaction_volume": 1000,
        "low_transaction_amount": 2000,
        "average_transaction_amount": 3000,
        "high_transaction_amount": 4000,
        "daily_transaction_count": 5000,
        "card_not_present_perctange": 90,
        "card_present_perctange": 10,
    },
        bank_details={
        "routing_number": "082900872",
        "account_number": "1234567890",
    },
        pricing_structure={
        "amex": {
            "rate": 2.5,
            "fee": 0.25,
        },
,
,
        "monthly_fee": 25,
        "billing_frequency": "Monthly",
        "program": "MerchantServices",
    },
        external_id="aaa",
        owners=[
        {
            "title": "CEO",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@test.com",
            "phone": "5551234567",
            "dob": "1947-03-25",
            "ssn": "5554449999",
            "ownership_percentage": 100,
        }
    ],
    )
    print(create_new_application_response)
except ApiException as e:
    print("Exception when calling ApplicationApi.create_new_application: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from payfactory_python_sdk import Payfactory, ApiException

payfactory = Payfactory(

        api_key = 'YOUR_API_KEY',
)

async def main():
    try:
        # Submit a new Application
        create_new_application_response = await payfactory.application.acreate_new_application(
            isv_name="aaa",
            business_details={
        "address": {
            "street1": "125 West Third Street 1st Floor",
            "city": "Tulsa",
            "state": "OK",
            "zip": "74555",
        },
        "phone": "5551234567",
        "established_date": "1959-02-03",
        "legal_name": "ACME LLC.",
        "dba_name": "ACME",
        "tax_id": "123456789",
        "website": "https://www.acme.com",
        "mcc": 7297,
        "ownership_type": "Unknown",
    },
            customer_service_contact={
        "phone": "5551234567",
        "email": "test@test.com",
    },
            risk_contact={
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
    },
            business_contact={
        "title": "CEO",
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
        "phone": "5551234567",
        "dob": "1947-03-25",
        "ssn": "5554449999",
    },
            processing_details={
        "billing_descriptor": "ACME_WEST_POS",
        "monthly_transaction_volume": 1000,
        "low_transaction_amount": 2000,
        "average_transaction_amount": 3000,
        "high_transaction_amount": 4000,
        "daily_transaction_count": 5000,
        "card_not_present_perctange": 90,
        "card_present_perctange": 10,
    },
            bank_details={
        "routing_number": "082900872",
        "account_number": "1234567890",
    },
            pricing_structure={
        "amex": {
            "rate": 2.5,
            "fee": 0.25,
        },
,
,
        "monthly_fee": 25,
        "billing_frequency": "Monthly",
        "program": "MerchantServices",
    },
            external_id="aaa",
            owners=[
        {
            "title": "CEO",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@test.com",
            "phone": "5551234567",
            "dob": "1947-03-25",
            "ssn": "5554449999",
            "ownership_percentage": 100,
        }
    ],
        )
        print(create_new_application_response)
    except ApiException as e:
        print("Exception when calling ApplicationApi.create_new_application: %s\n" % e)
        pprint(e.body)
        if e.status == 400:
            pprint(e.body["status"])
            pprint(e.body["message"])
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from payfactory_python_sdk import Payfactory, ApiException

payfactory = Payfactory(

        api_key = 'YOUR_API_KEY',
)

try:
    # Submit a new Application
    create_new_application_response = payfactory.application.raw.create_new_application(
        isv_name="aaa",
        business_details={
        "address": {
            "street1": "125 West Third Street 1st Floor",
            "city": "Tulsa",
            "state": "OK",
            "zip": "74555",
        },
        "phone": "5551234567",
        "established_date": "1959-02-03",
        "legal_name": "ACME LLC.",
        "dba_name": "ACME",
        "tax_id": "123456789",
        "website": "https://www.acme.com",
        "mcc": 7297,
        "ownership_type": "Unknown",
    },
        customer_service_contact={
        "phone": "5551234567",
        "email": "test@test.com",
    },
        risk_contact={
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
    },
        business_contact={
        "title": "CEO",
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
        "phone": "5551234567",
        "dob": "1947-03-25",
        "ssn": "5554449999",
    },
        processing_details={
        "billing_descriptor": "ACME_WEST_POS",
        "monthly_transaction_volume": 1000,
        "low_transaction_amount": 2000,
        "average_transaction_amount": 3000,
        "high_transaction_amount": 4000,
        "daily_transaction_count": 5000,
        "card_not_present_perctange": 90,
        "card_present_perctange": 10,
    },
        bank_details={
        "routing_number": "082900872",
        "account_number": "1234567890",
    },
        pricing_structure={
        "amex": {
            "rate": 2.5,
            "fee": 0.25,
        },
,
,
        "monthly_fee": 25,
        "billing_frequency": "Monthly",
        "program": "MerchantServices",
    },
        external_id="aaa",
        owners=[
        {
            "title": "CEO",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@test.com",
            "phone": "5551234567",
            "dob": "1947-03-25",
            "ssn": "5554449999",
            "ownership_percentage": 100,
        }
    ],
    )
    pprint(create_new_application_response.body)
    pprint(create_new_application_response.body["app_id"])
    pprint(create_new_application_response.headers)
    pprint(create_new_application_response.status)
    pprint(create_new_application_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ApplicationApi.create_new_application: %s\n" % e)
    pprint(e.body)
    if e.status == 400:
        pprint(e.body["status"])
        pprint(e.body["message"])
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `payfactory.application.create_new_application`<a id="payfactoryapplicationcreate_new_application"></a>

Submit a new Application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_application_response = payfactory.application.create_new_application(
    isv_name="aaa",
    business_details={
        "address": {
            "street1": "125 West Third Street 1st Floor",
            "city": "Tulsa",
            "state": "OK",
            "zip": "74555",
        },
        "phone": "5551234567",
        "established_date": "1959-02-03",
        "legal_name": "ACME LLC.",
        "dba_name": "ACME",
        "tax_id": "123456789",
        "website": "https://www.acme.com",
        "mcc": 7297,
        "ownership_type": "Unknown",
    },
    customer_service_contact={
        "phone": "5551234567",
        "email": "test@test.com",
    },
    risk_contact={
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
    },
    business_contact={
        "title": "CEO",
        "first_name": "John",
        "last_name": "Doe",
        "email": "test@test.com",
        "phone": "5551234567",
        "dob": "1947-03-25",
        "ssn": "5554449999",
    },
    processing_details={
        "billing_descriptor": "ACME_WEST_POS",
        "monthly_transaction_volume": 1000,
        "low_transaction_amount": 2000,
        "average_transaction_amount": 3000,
        "high_transaction_amount": 4000,
        "daily_transaction_count": 5000,
        "card_not_present_perctange": 90,
        "card_present_perctange": 10,
    },
    bank_details={
        "routing_number": "082900872",
        "account_number": "1234567890",
    },
    pricing_structure={
        "amex": {
            "rate": 2.5,
            "fee": 0.25,
        },
,
,
        "monthly_fee": 25,
        "billing_frequency": "Monthly",
        "program": "MerchantServices",
    },
    external_id="aaa",
    owners=[
        {
            "title": "CEO",
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@test.com",
            "phone": "5551234567",
            "dob": "1947-03-25",
            "ssn": "5554449999",
            "ownership_percentage": 100,
        }
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### isv_name: `str`<a id="isv_name-str"></a>

##### business_details: [`BusinessDetailsModel`](./payfactory_python_sdk/type/business_details_model.py)<a id="business_details-businessdetailsmodelpayfactory_python_sdktypebusiness_details_modelpy"></a>


##### customer_service_contact: [`CustomerServiceContactModel`](./payfactory_python_sdk/type/customer_service_contact_model.py)<a id="customer_service_contact-customerservicecontactmodelpayfactory_python_sdktypecustomer_service_contact_modelpy"></a>


##### risk_contact: [`RiskContactModel`](./payfactory_python_sdk/type/risk_contact_model.py)<a id="risk_contact-riskcontactmodelpayfactory_python_sdktyperisk_contact_modelpy"></a>


##### business_contact: [`PersonModel`](./payfactory_python_sdk/type/person_model.py)<a id="business_contact-personmodelpayfactory_python_sdktypeperson_modelpy"></a>


##### processing_details: [`ProcessingDetailsModel`](./payfactory_python_sdk/type/processing_details_model.py)<a id="processing_details-processingdetailsmodelpayfactory_python_sdktypeprocessing_details_modelpy"></a>


##### bank_details: [`BankDetailsModel`](./payfactory_python_sdk/type/bank_details_model.py)<a id="bank_details-bankdetailsmodelpayfactory_python_sdktypebank_details_modelpy"></a>


##### pricing_structure: [`PricingModel`](./payfactory_python_sdk/type/pricing_model.py)<a id="pricing_structure-pricingmodelpayfactory_python_sdktypepricing_modelpy"></a>


##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

##### owners: List[`OwnerModel`]<a id="owners-listownermodel"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ApplicationSubmitRequestModel`](./payfactory_python_sdk/type/application_submit_request_model.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationSubmitResponseModel`](./payfactory_python_sdk/pydantic/application_submit_response_model.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Application/Submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.application.get_application_details`<a id="payfactoryapplicationget_application_details"></a>

Gets Details for an Application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_details_response = payfactory.application.get_application_details(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationDetailsResponse`](./payfactory_python_sdk/pydantic/application_details_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Application/Details/{appId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.application.get_application_status`<a id="payfactoryapplicationget_application_status"></a>

Gets the Status of an Application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_application_status_response = payfactory.application.get_application_status(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ApplicationStatusResponse`](./payfactory_python_sdk/pydantic/application_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Application/Status/{appId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.application.remove_by_id`<a id="payfactoryapplicationremove_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
payfactory.application.remove_by_id(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Application/Delete/{appId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.application.start_underwriting_process`<a id="payfactoryapplicationstart_underwriting_process"></a>

Start Underwriting Process for an Application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
payfactory.application.start_underwriting_process(
    app_id="appId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### app_id: `str`<a id="app_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Application/StartUnderwriting/{appId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.application_form.create_session`<a id="payfactoryapplication_formcreate_session"></a>

Creates a new Session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_session_response = payfactory.application_form.create_session(
    signer={
        "email_address": "test@test.com",
        "first_name": "Testor",
        "last_name": "Testington",
    },
    company_name="Test",
    redirect_url="https://test.com/return",
    complete_url="https://test.com/complete",
    refresh_url="https://test.com/refresh",
    external_id="Test1234",
    pricing_plan_id="APFOG8GTO04FKF",
    business_details={
        "phone": "5551234567",
        "established_date": "1959-02-03",
        "legal_name": "ACME LLC.",
        "dba_name": "ACME",
        "tax_id": "123456789",
        "website": "https://www.acme.com",
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### signer: [`CreateSessionRequestSignerModel`](./payfactory_python_sdk/type/create_session_request_signer_model.py)<a id="signer-createsessionrequestsignermodelpayfactory_python_sdktypecreate_session_request_signer_modelpy"></a>


##### company_name: `str`<a id="company_name-str"></a>

Name of the merchant account

##### redirect_url: `str`<a id="redirect_url-str"></a>

Url to redirect the merchant user to when clicking the back button

##### complete_url: `str`<a id="complete_url-str"></a>

Url to redirect the merchant user to upon completing the application

##### refresh_url: `str`<a id="refresh_url-str"></a>

Url to redirect to the merchant user to when their session is expired

##### external_id: `str`<a id="external_id-str"></a>

Unique identifier for the merchant in your system

##### pricing_plan_id: `Optional[str]`<a id="pricing_plan_id-optionalstr"></a>

Id of the Pricing Plan. Only used if enabled for the partner

##### business_details: [`SessionBusinessDetailsModel`](./payfactory_python_sdk/type/session_business_details_model.py)<a id="business_details-sessionbusinessdetailsmodelpayfactory_python_sdktypesession_business_details_modelpy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateSessionRequest`](./payfactory_python_sdk/type/create_session_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`SessionResponse`](./payfactory_python_sdk/pydantic/session_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ApplicationForm/session` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.application_form.get_session_info`<a id="payfactoryapplication_formget_session_info"></a>

Gets information about a Session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_session_info_response = payfactory.application_form.get_session_info(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SessionResponse`](./payfactory_python_sdk/pydantic/session_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ApplicationForm/session/{sessionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.application_form.update_session_activity`<a id="payfactoryapplication_formupdate_session_activity"></a>

Touch a Session, keeping it active

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_session_activity_response = payfactory.application_form.update_session_activity(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`SessionResponse`](./payfactory_python_sdk/pydantic/session_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/ApplicationForm/session/{sessionId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.document.upload_agreement`<a id="payfactorydocumentupload_agreement"></a>

Upload an Agreement for a new Application

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
payfactory.document.upload_agreement(
    type="type_example",
    app_id="appId_example",
    document=".pdf",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### type: `str`<a id="type-str"></a>

##### app_id: `str`<a id="app_id-str"></a>

##### document: `IO`<a id="document-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DocumentUploadAgreementRequest`](./payfactory_python_sdk/type/document_upload_agreement_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Document/Upload/{type}/{appId}` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.reporting.get_ach_transactions_by_reference_id`<a id="payfactoryreportingget_ach_transactions_by_reference_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_ach_transactions_by_reference_id_response = payfactory.reporting.get_ach_transactions_by_reference_id(
    reference_id="referenceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reference_id: `str`<a id="reference_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReportingGetAchTransactionsByReferenceIdResponse`](./payfactory_python_sdk/pydantic/reporting_get_ach_transactions_by_reference_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Reporting/AchTransactions/{referenceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.reporting.get_deposits`<a id="payfactoryreportingget_deposits"></a>

Get current Deposits

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_deposits_response = payfactory.reporting.get_deposits()
```

#### 🔄 Return<a id="🔄-return"></a>

[`ReportingGetDepositsResponse`](./payfactory_python_sdk/pydantic/reporting_get_deposits_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Reporting/Deposits` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.reporting.get_deposits_by_count`<a id="payfactoryreportingget_deposits_by_count"></a>

Get {n} current Deposits

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_deposits_by_count_response = payfactory.reporting.get_deposits_by_count(
    number_of_deposits=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### number_of_deposits: `int`<a id="number_of_deposits-int"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReportingGetDepositsByCountResponse`](./payfactory_python_sdk/pydantic/reporting_get_deposits_by_count_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Reporting/Deposits/{numberOfDeposits}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.reporting.get_deposits_by_reference_id`<a id="payfactoryreportingget_deposits_by_reference_id"></a>

Get Deposits by ReferenceId.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_deposits_by_reference_id_response = payfactory.reporting.get_deposits_by_reference_id(
    reference_id="referenceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### reference_id: `str`<a id="reference_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ReportingGetDepositsByReferenceIdResponse`](./payfactory_python_sdk/pydantic/reporting_get_deposits_by_reference_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Reporting/Deposits/{referenceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.transaction.create_metadata`<a id="payfactorytransactioncreate_metadata"></a>

Post Metadata related to a Transaction

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_metadata_response = payfactory.transaction.create_metadata(
    transaction_id="a",
    merchant_id="4BCD-3FGH",
    card_holder_name="John Doe",
    external_id="abcdef123456",
    order_id="321654987",
    partner_fee=1.25,
    item_count=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### transaction_id: `str`<a id="transaction_id-str"></a>

The transaction Id from the payment processor

##### merchant_id: `str`<a id="merchant_id-str"></a>

Payfactoy's merchant Id

##### card_holder_name: `str`<a id="card_holder_name-str"></a>

Name of the Cardholder

##### external_id: `Optional[str]`<a id="external_id-optionalstr"></a>

Any identifier you choose to send

##### order_id: `Optional[str]`<a id="order_id-optionalstr"></a>

Any identifier you choose to send

##### partner_fee: `Optional[Union[int, float]]`<a id="partner_fee-optionalunionint-float"></a>

Required if partner is configured for the partner fee program

##### item_count: `Optional[int]`<a id="item_count-optionalint"></a>

Number of items sold in the transaction

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionMetadataRequest`](./payfactory_python_sdk/type/transaction_metadata_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Transaction/Metadata` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `payfactory.transaction.create_metadata_bulk`<a id="payfactorytransactioncreate_metadata_bulk"></a>

Post multiple Metadate related to a Transactions

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_metadata_bulk_response = payfactory.transaction.create_metadata_bulk(
    body=[
        {
            "transaction_id": "transaction_id_example",
            "merchant_id": "4BCD-3FGH",
            "card_holder_name": "John Doe",
            "external_id": "abcdef123456",
            "order_id": "321654987",
            "partner_fee": 1.25,
            "item_count": 1,
        }
    ],
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TransactionCreateMetadataBulkRequest`](./payfactory_python_sdk/type/transaction_create_metadata_bulk_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/v1/Transaction/MetadataBulk` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
