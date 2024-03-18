# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from payfactory_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V1_APPLICATION_STATUS_APP_ID = "/v1/Application/Status/{appId}"
    V1_APPLICATION_DETAILS_APP_ID = "/v1/Application/Details/{appId}"
    V1_APPLICATION_START_UNDERWRITING_APP_ID = "/v1/Application/StartUnderwriting/{appId}"
    V1_APPLICATION_SUBMIT = "/v1/Application/Submit"
    V1_APPLICATION_DELETE_APP_ID = "/v1/Application/Delete/{appId}"
    V1_APPLICATION_FORM_SESSION_SESSION_ID = "/v1/ApplicationForm/session/{sessionId}"
    V1_APPLICATION_FORM_SESSION = "/v1/ApplicationForm/session"
    V1_DOCUMENT_UPLOAD_TYPE_APP_ID = "/v1/Document/Upload/{type}/{appId}"
    V1_REPORTING_DEPOSITS = "/v1/Reporting/Deposits"
    V1_REPORTING_DEPOSITS_REFERENCE_ID = "/v1/Reporting/Deposits/{referenceId}"
    V1_REPORTING_ACH_TRANSACTIONS_REFERENCE_ID = "/v1/Reporting/AchTransactions/{referenceId}"
    V1_REPORTING_DEPOSITS_NUMBER_OF_DEPOSITS = "/v1/Reporting/Deposits/{numberOfDeposits}"
    V1_TRANSACTION_METADATA = "/v1/Transaction/Metadata"
    V1_TRANSACTION_METADATA_BULK = "/v1/Transaction/MetadataBulk"
