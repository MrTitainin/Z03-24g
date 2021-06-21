"""
    Weatherbit.io - Swagger UI Weather API documentation

    This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from openapi_client.model.aq_hourly import AQHourly
from openapi_client.model.error import Error


class AirQualityForecastApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __forecast_airqualitycity_idcity_id_get(
            self,
            city_id,
            key,
            **kwargs
        ):
            """Returns 72 hour (hourly) Air Quality forecast - Given a City ID.  # noqa: E501

            Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.forecast_airqualitycity_idcity_id_get(city_id, key, async_req=True)
            >>> result = thread.get()

            Args:
                city_id (int): City ID. Example: 4487042
                key (str): Your registered API key.

            Keyword Args:
                param_callback (str): Wraps return in jsonp callback. Example - callback=func. [optional]
                hours (int): Number of hours to return.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AQHourly
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['city_id'] = \
                city_id
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.forecast_airqualitycity_idcity_id_get = _Endpoint(
            settings={
                'response_type': (AQHourly,),
                'auth': [],
                'endpoint_path': '/forecast/airquality?city_id={city_id}',
                'operation_id': 'forecast_airqualitycity_idcity_id_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'city_id',
                    'key',
                    'param_callback',
                    'hours',
                ],
                'required': [
                    'city_id',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'city_id':
                        (int,),
                    'key':
                        (str,),
                    'param_callback':
                        (str,),
                    'hours':
                        (int,),
                },
                'attribute_map': {
                    'city_id': 'city_id',
                    'key': 'key',
                    'param_callback': 'callback',
                    'hours': 'hours',
                },
                'location_map': {
                    'city_id': 'path',
                    'key': 'query',
                    'param_callback': 'query',
                    'hours': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__forecast_airqualitycity_idcity_id_get
        )

        def __forecast_airqualitycitycitycountrycountry_get(
            self,
            city,
            country,
            key,
            **kwargs
        ):
            """Returns 72 hour (hourly) Air Quality forecast - Given City and/or State, Country.  # noqa: E501

            Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.forecast_airqualitycitycitycountrycountry_get(city, country, key, async_req=True)
            >>> result = thread.get()

            Args:
                city (str): City search.. Example - &city=Raleigh,NC or &city=Berlin,DE or city=Paris&country=FR
                country (str): Country Code (2 letter).
                key (str): Your registered API key.

            Keyword Args:
                state (str): Full name of state.. [optional]
                param_callback (str): Wraps return in jsonp callback. Example: callback=func. [optional]
                hours (int): Number of hours to return.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AQHourly
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['city'] = \
                city
            kwargs['country'] = \
                country
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.forecast_airqualitycitycitycountrycountry_get = _Endpoint(
            settings={
                'response_type': (AQHourly,),
                'auth': [],
                'endpoint_path': '/forecast/airquality?city={city}&country={country}',
                'operation_id': 'forecast_airqualitycitycitycountrycountry_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'city',
                    'country',
                    'key',
                    'state',
                    'param_callback',
                    'hours',
                ],
                'required': [
                    'city',
                    'country',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'city':
                        (str,),
                    'country':
                        (str,),
                    'key':
                        (str,),
                    'state':
                        (str,),
                    'param_callback':
                        (str,),
                    'hours':
                        (int,),
                },
                'attribute_map': {
                    'city': 'city',
                    'country': 'country',
                    'key': 'key',
                    'state': 'state',
                    'param_callback': 'callback',
                    'hours': 'hours',
                },
                'location_map': {
                    'city': 'path',
                    'country': 'path',
                    'key': 'query',
                    'state': 'query',
                    'param_callback': 'query',
                    'hours': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__forecast_airqualitycitycitycountrycountry_get
        )

        def __forecast_airqualitylatlatlonlon_get(
            self,
            lat,
            lon,
            key,
            **kwargs
        ):
            """Returns 72 hour (hourly) Air Quality forecast - Given a lat/lon.  # noqa: E501

            Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.forecast_airqualitylatlatlonlon_get(lat, lon, key, async_req=True)
            >>> result = thread.get()

            Args:
                lat (float): Latitude component of location.
                lon (float): Longitude component of location.
                key (str): Your registered API key.

            Keyword Args:
                param_callback (str): Wraps return in jsonp callback. Example - callback=func. [optional]
                hours (int): Number of hours to return.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AQHourly
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['lat'] = \
                lat
            kwargs['lon'] = \
                lon
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.forecast_airqualitylatlatlonlon_get = _Endpoint(
            settings={
                'response_type': (AQHourly,),
                'auth': [],
                'endpoint_path': '/forecast/airquality?lat={lat}&lon={lon}',
                'operation_id': 'forecast_airqualitylatlatlonlon_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'lat',
                    'lon',
                    'key',
                    'param_callback',
                    'hours',
                ],
                'required': [
                    'lat',
                    'lon',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'lat':
                        (float,),
                    'lon':
                        (float,),
                    'key':
                        (str,),
                    'param_callback':
                        (str,),
                    'hours':
                        (int,),
                },
                'attribute_map': {
                    'lat': 'lat',
                    'lon': 'lon',
                    'key': 'key',
                    'param_callback': 'callback',
                    'hours': 'hours',
                },
                'location_map': {
                    'lat': 'path',
                    'lon': 'path',
                    'key': 'query',
                    'param_callback': 'query',
                    'hours': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__forecast_airqualitylatlatlonlon_get
        )

        def __forecast_airqualitypostal_codepostal_code_get(
            self,
            postal_code,
            key,
            **kwargs
        ):
            """Returns 72 hour (hourly) Air Quality forecast - Given a Postal Code.  # noqa: E501

            Returns 72 hour (hourly) Air Quality forecast, where each point represents a one hour period.  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.forecast_airqualitypostal_codepostal_code_get(postal_code, key, async_req=True)
            >>> result = thread.get()

            Args:
                postal_code (int): Postal Code. Example: 28546
                key (str): Your registered API key.

            Keyword Args:
                country (str): Country Code (2 letter).. [optional]
                param_callback (str): Wraps return in jsonp callback. Example - callback=func. [optional]
                hours (int): Number of hours to return.. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                AQHourly
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['postal_code'] = \
                postal_code
            kwargs['key'] = \
                key
            return self.call_with_http_info(**kwargs)

        self.forecast_airqualitypostal_codepostal_code_get = _Endpoint(
            settings={
                'response_type': (AQHourly,),
                'auth': [],
                'endpoint_path': '/forecast/airquality?postal_code={postal_code}',
                'operation_id': 'forecast_airqualitypostal_codepostal_code_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'postal_code',
                    'key',
                    'country',
                    'param_callback',
                    'hours',
                ],
                'required': [
                    'postal_code',
                    'key',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'postal_code':
                        (int,),
                    'key':
                        (str,),
                    'country':
                        (str,),
                    'param_callback':
                        (str,),
                    'hours':
                        (int,),
                },
                'attribute_map': {
                    'postal_code': 'postal_code',
                    'key': 'key',
                    'country': 'country',
                    'param_callback': 'callback',
                    'hours': 'hours',
                },
                'location_map': {
                    'postal_code': 'path',
                    'key': 'query',
                    'country': 'query',
                    'param_callback': 'query',
                    'hours': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__forecast_airqualitypostal_codepostal_code_get
        )