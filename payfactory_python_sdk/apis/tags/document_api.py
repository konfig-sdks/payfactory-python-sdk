# coding: utf-8

"""
    Payfactory Api

    Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from payfactory_python_sdk.paths.v1_document_upload_type_app_id.post import UploadAgreement
from payfactory_python_sdk.apis.tags.document_api_raw import DocumentApiRaw


class DocumentApi(
    UploadAgreement,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DocumentApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DocumentApiRaw(api_client)