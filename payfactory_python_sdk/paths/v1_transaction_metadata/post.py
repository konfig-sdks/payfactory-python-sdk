# coding: utf-8

"""
    Payfactory Api

    Payfactory specializes in embedded payment facilitation (payfac) services for ISVs and SaaS companies. Our gateway-friendly platform integrates with software systems to provide seamless payment facilitation with little to no development required, allowing our partners to minimize integration costs and quickly gain a new revenue stream. Founded by payment industry veterans, we believe that integrated processing should be simple, frictionless and fast – while also maintaining the highest level of security, customer service and human support.

    The version of the OpenAPI document: v1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from payfactory_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from payfactory_python_sdk.api_response import AsyncGeneratorResponse
from payfactory_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from payfactory_python_sdk import schemas  # noqa: F401

from payfactory_python_sdk.model.transaction_metadata_request import TransactionMetadataRequest as TransactionMetadataRequestSchema
from payfactory_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from payfactory_python_sdk.type.transaction_metadata_request import TransactionMetadataRequest
from payfactory_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from payfactory_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from payfactory_python_sdk.pydantic.transaction_metadata_request import TransactionMetadataRequest as TransactionMetadataRequestPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = TransactionMetadataRequestSchema


request_body_transaction_metadata_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'ApiKey',
]
SchemaFor200ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = schemas.DictSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_metadata_mapped_args(
        self,
        transaction_id: str,
        merchant_id: str,
        card_holder_name: str,
        external_id: typing.Optional[typing.Optional[str]] = None,
        order_id: typing.Optional[typing.Optional[str]] = None,
        partner_fee: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        item_count: typing.Optional[typing.Optional[int]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if transaction_id is not None:
            _body["transactionId"] = transaction_id
        if merchant_id is not None:
            _body["merchantId"] = merchant_id
        if card_holder_name is not None:
            _body["cardHolderName"] = card_holder_name
        if external_id is not None:
            _body["externalId"] = external_id
        if order_id is not None:
            _body["orderId"] = order_id
        if partner_fee is not None:
            _body["partnerFee"] = partner_fee
        if item_count is not None:
            _body["itemCount"] = item_count
        args.body = _body
        return args

    async def _acreate_metadata_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Post Metadata related to a Transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/Transaction/Metadata',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_transaction_metadata_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_metadata_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Post Metadata related to a Transaction
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/Transaction/Metadata',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_transaction_metadata_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateMetadataRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_metadata(
        self,
        transaction_id: str,
        merchant_id: str,
        card_holder_name: str,
        external_id: typing.Optional[typing.Optional[str]] = None,
        order_id: typing.Optional[typing.Optional[str]] = None,
        partner_fee: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        item_count: typing.Optional[typing.Optional[int]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_metadata_mapped_args(
            transaction_id=transaction_id,
            merchant_id=merchant_id,
            card_holder_name=card_holder_name,
            external_id=external_id,
            order_id=order_id,
            partner_fee=partner_fee,
            item_count=item_count,
        )
        return await self._acreate_metadata_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_metadata(
        self,
        transaction_id: str,
        merchant_id: str,
        card_holder_name: str,
        external_id: typing.Optional[typing.Optional[str]] = None,
        order_id: typing.Optional[typing.Optional[str]] = None,
        partner_fee: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        item_count: typing.Optional[typing.Optional[int]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_metadata_mapped_args(
            transaction_id=transaction_id,
            merchant_id=merchant_id,
            card_holder_name=card_holder_name,
            external_id=external_id,
            order_id=order_id,
            partner_fee=partner_fee,
            item_count=item_count,
        )
        return self._create_metadata_oapg(
            body=args.body,
        )

class CreateMetadata(BaseApi):

    async def acreate_metadata(
        self,
        transaction_id: str,
        merchant_id: str,
        card_holder_name: str,
        external_id: typing.Optional[typing.Optional[str]] = None,
        order_id: typing.Optional[typing.Optional[str]] = None,
        partner_fee: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        item_count: typing.Optional[typing.Optional[int]] = None,
        validate: bool = False,
        **kwargs,
    ) -> Dictionary:
        raw_response = await self.raw.acreate_metadata(
            transaction_id=transaction_id,
            merchant_id=merchant_id,
            card_holder_name=card_holder_name,
            external_id=external_id,
            order_id=order_id,
            partner_fee=partner_fee,
            item_count=item_count,
            **kwargs,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)
    
    
    def create_metadata(
        self,
        transaction_id: str,
        merchant_id: str,
        card_holder_name: str,
        external_id: typing.Optional[typing.Optional[str]] = None,
        order_id: typing.Optional[typing.Optional[str]] = None,
        partner_fee: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        item_count: typing.Optional[typing.Optional[int]] = None,
        validate: bool = False,
    ) -> Dictionary:
        raw_response = self.raw.create_metadata(
            transaction_id=transaction_id,
            merchant_id=merchant_id,
            card_holder_name=card_holder_name,
            external_id=external_id,
            order_id=order_id,
            partner_fee=partner_fee,
            item_count=item_count,
        )
        if validate:
            return Dictionary(**raw_response.body)
        return api_client.construct_model_instance(Dictionary, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        transaction_id: str,
        merchant_id: str,
        card_holder_name: str,
        external_id: typing.Optional[typing.Optional[str]] = None,
        order_id: typing.Optional[typing.Optional[str]] = None,
        partner_fee: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        item_count: typing.Optional[typing.Optional[int]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_metadata_mapped_args(
            transaction_id=transaction_id,
            merchant_id=merchant_id,
            card_holder_name=card_holder_name,
            external_id=external_id,
            order_id=order_id,
            partner_fee=partner_fee,
            item_count=item_count,
        )
        return await self._acreate_metadata_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        transaction_id: str,
        merchant_id: str,
        card_holder_name: str,
        external_id: typing.Optional[typing.Optional[str]] = None,
        order_id: typing.Optional[typing.Optional[str]] = None,
        partner_fee: typing.Optional[typing.Optional[typing.Union[int, float]]] = None,
        item_count: typing.Optional[typing.Optional[int]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_metadata_mapped_args(
            transaction_id=transaction_id,
            merchant_id=merchant_id,
            card_holder_name=card_holder_name,
            external_id=external_id,
            order_id=order_id,
            partner_fee=partner_fee,
            item_count=item_count,
        )
        return self._create_metadata_oapg(
            body=args.body,
        )

