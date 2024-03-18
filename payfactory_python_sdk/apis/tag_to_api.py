import typing_extensions

from payfactory_python_sdk.apis.tags import TagValues
from payfactory_python_sdk.apis.tags.application_api import ApplicationApi
from payfactory_python_sdk.apis.tags.reporting_api import ReportingApi
from payfactory_python_sdk.apis.tags.application_form_api import ApplicationFormApi
from payfactory_python_sdk.apis.tags.transaction_api import TransactionApi
from payfactory_python_sdk.apis.tags.document_api import DocumentApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.APPLICATION: ApplicationApi,
        TagValues.REPORTING: ReportingApi,
        TagValues.APPLICATION_FORM: ApplicationFormApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.DOCUMENT: DocumentApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.APPLICATION: ApplicationApi,
        TagValues.REPORTING: ReportingApi,
        TagValues.APPLICATION_FORM: ApplicationFormApi,
        TagValues.TRANSACTION: TransactionApi,
        TagValues.DOCUMENT: DocumentApi,
    }
)
