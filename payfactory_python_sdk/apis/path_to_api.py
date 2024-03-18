import typing_extensions

from payfactory_python_sdk.paths import PathValues
from payfactory_python_sdk.apis.paths.v1_application_status_app_id import V1ApplicationStatusAppId
from payfactory_python_sdk.apis.paths.v1_application_details_app_id import V1ApplicationDetailsAppId
from payfactory_python_sdk.apis.paths.v1_application_start_underwriting_app_id import V1ApplicationStartUnderwritingAppId
from payfactory_python_sdk.apis.paths.v1_application_submit import V1ApplicationSubmit
from payfactory_python_sdk.apis.paths.v1_application_delete_app_id import V1ApplicationDeleteAppId
from payfactory_python_sdk.apis.paths.v1_application_form_session_session_id import V1ApplicationFormSessionSessionId
from payfactory_python_sdk.apis.paths.v1_application_form_session import V1ApplicationFormSession
from payfactory_python_sdk.apis.paths.v1_document_upload_type_app_id import V1DocumentUploadTypeAppId
from payfactory_python_sdk.apis.paths.v1_reporting_deposits import V1ReportingDeposits
from payfactory_python_sdk.apis.paths.v1_reporting_deposits_reference_id import V1ReportingDepositsReferenceId
from payfactory_python_sdk.apis.paths.v1_reporting_ach_transactions_reference_id import V1ReportingAchTransactionsReferenceId
from payfactory_python_sdk.apis.paths.v1_reporting_deposits_number_of_deposits import V1ReportingDepositsNumberOfDeposits
from payfactory_python_sdk.apis.paths.v1_transaction_metadata import V1TransactionMetadata
from payfactory_python_sdk.apis.paths.v1_transaction_metadata_bulk import V1TransactionMetadataBulk

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V1_APPLICATION_STATUS_APP_ID: V1ApplicationStatusAppId,
        PathValues.V1_APPLICATION_DETAILS_APP_ID: V1ApplicationDetailsAppId,
        PathValues.V1_APPLICATION_START_UNDERWRITING_APP_ID: V1ApplicationStartUnderwritingAppId,
        PathValues.V1_APPLICATION_SUBMIT: V1ApplicationSubmit,
        PathValues.V1_APPLICATION_DELETE_APP_ID: V1ApplicationDeleteAppId,
        PathValues.V1_APPLICATION_FORM_SESSION_SESSION_ID: V1ApplicationFormSessionSessionId,
        PathValues.V1_APPLICATION_FORM_SESSION: V1ApplicationFormSession,
        PathValues.V1_DOCUMENT_UPLOAD_TYPE_APP_ID: V1DocumentUploadTypeAppId,
        PathValues.V1_REPORTING_DEPOSITS: V1ReportingDeposits,
        PathValues.V1_REPORTING_DEPOSITS_REFERENCE_ID: V1ReportingDepositsReferenceId,
        PathValues.V1_REPORTING_ACH_TRANSACTIONS_REFERENCE_ID: V1ReportingAchTransactionsReferenceId,
        PathValues.V1_REPORTING_DEPOSITS_NUMBER_OF_DEPOSITS: V1ReportingDepositsNumberOfDeposits,
        PathValues.V1_TRANSACTION_METADATA: V1TransactionMetadata,
        PathValues.V1_TRANSACTION_METADATA_BULK: V1TransactionMetadataBulk,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V1_APPLICATION_STATUS_APP_ID: V1ApplicationStatusAppId,
        PathValues.V1_APPLICATION_DETAILS_APP_ID: V1ApplicationDetailsAppId,
        PathValues.V1_APPLICATION_START_UNDERWRITING_APP_ID: V1ApplicationStartUnderwritingAppId,
        PathValues.V1_APPLICATION_SUBMIT: V1ApplicationSubmit,
        PathValues.V1_APPLICATION_DELETE_APP_ID: V1ApplicationDeleteAppId,
        PathValues.V1_APPLICATION_FORM_SESSION_SESSION_ID: V1ApplicationFormSessionSessionId,
        PathValues.V1_APPLICATION_FORM_SESSION: V1ApplicationFormSession,
        PathValues.V1_DOCUMENT_UPLOAD_TYPE_APP_ID: V1DocumentUploadTypeAppId,
        PathValues.V1_REPORTING_DEPOSITS: V1ReportingDeposits,
        PathValues.V1_REPORTING_DEPOSITS_REFERENCE_ID: V1ReportingDepositsReferenceId,
        PathValues.V1_REPORTING_ACH_TRANSACTIONS_REFERENCE_ID: V1ReportingAchTransactionsReferenceId,
        PathValues.V1_REPORTING_DEPOSITS_NUMBER_OF_DEPOSITS: V1ReportingDepositsNumberOfDeposits,
        PathValues.V1_TRANSACTION_METADATA: V1TransactionMetadata,
        PathValues.V1_TRANSACTION_METADATA_BULK: V1TransactionMetadataBulk,
    }
)
