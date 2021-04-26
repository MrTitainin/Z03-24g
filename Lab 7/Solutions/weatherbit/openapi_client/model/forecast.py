"""
    Weatherbit.io - Swagger UI Weather API documentation

    This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from openapi_client.model.forecast_weather import ForecastWeather
    globals()['ForecastWeather'] = ForecastWeather


class Forecast(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'ts': (float,),  # noqa: E501
            'timestamp_local': (str,),  # noqa: E501
            'timestamp_utc': (str,),  # noqa: E501
            'datetime': (str,),  # noqa: E501
            'snow': (float,),  # noqa: E501
            'snow_depth': (float,),  # noqa: E501
            'precip': (float,),  # noqa: E501
            'temp': (float,),  # noqa: E501
            'dewpt': (float,),  # noqa: E501
            'max_temp': (float,),  # noqa: E501
            'min_temp': (float,),  # noqa: E501
            'app_max_temp': (float,),  # noqa: E501
            'app_min_temp': (float,),  # noqa: E501
            'rh': (int,),  # noqa: E501
            'clouds': (int,),  # noqa: E501
            'weather': (ForecastWeather,),  # noqa: E501
            'slp': (float,),  # noqa: E501
            'pres': (float,),  # noqa: E501
            'uv': (float,),  # noqa: E501
            'max_dhi': (float,),  # noqa: E501
            'vis': (float,),  # noqa: E501
            'pop': (float,),  # noqa: E501
            'moon_phase': (float,),  # noqa: E501
            'sunrise_ts': (int,),  # noqa: E501
            'sunset_ts': (int,),  # noqa: E501
            'moonrise_ts': (int,),  # noqa: E501
            'moonset_ts': (int,),  # noqa: E501
            'pod': (str,),  # noqa: E501
            'wind_spd': (float,),  # noqa: E501
            'wind_dir': (int,),  # noqa: E501
            'wind_cdir': (str,),  # noqa: E501
            'wind_cdir_full': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ts': 'ts',  # noqa: E501
        'timestamp_local': 'timestamp_local',  # noqa: E501
        'timestamp_utc': 'timestamp_utc',  # noqa: E501
        'datetime': 'datetime',  # noqa: E501
        'snow': 'snow',  # noqa: E501
        'snow_depth': 'snow_depth',  # noqa: E501
        'precip': 'precip',  # noqa: E501
        'temp': 'temp',  # noqa: E501
        'dewpt': 'dewpt',  # noqa: E501
        'max_temp': 'max_temp',  # noqa: E501
        'min_temp': 'min_temp',  # noqa: E501
        'app_max_temp': 'app_max_temp',  # noqa: E501
        'app_min_temp': 'app_min_temp',  # noqa: E501
        'rh': 'rh',  # noqa: E501
        'clouds': 'clouds',  # noqa: E501
        'weather': 'weather',  # noqa: E501
        'slp': 'slp',  # noqa: E501
        'pres': 'pres',  # noqa: E501
        'uv': 'uv',  # noqa: E501
        'max_dhi': 'max_dhi',  # noqa: E501
        'vis': 'vis',  # noqa: E501
        'pop': 'pop',  # noqa: E501
        'moon_phase': 'moon_phase',  # noqa: E501
        'sunrise_ts': 'sunrise_ts',  # noqa: E501
        'sunset_ts': 'sunset_ts',  # noqa: E501
        'moonrise_ts': 'moonrise_ts',  # noqa: E501
        'moonset_ts': 'moonset_ts',  # noqa: E501
        'pod': 'pod',  # noqa: E501
        'wind_spd': 'wind_spd',  # noqa: E501
        'wind_dir': 'wind_dir',  # noqa: E501
        'wind_cdir': 'wind_cdir',  # noqa: E501
        'wind_cdir_full': 'wind_cdir_full',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Forecast - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ts (float): Unix Timestamp. [optional]  # noqa: E501
            timestamp_local (str): Timestamp in local time. [optional]  # noqa: E501
            timestamp_utc (str): Timestamp UTC. [optional]  # noqa: E501
            datetime (str): Date in format \"YYYY-MM-DD:HH\". All datetime is in (UTC). [optional]  # noqa: E501
            snow (float): Accumulated snowfall since last forecast point - default (mm). [optional]  # noqa: E501
            snow_depth (float): Snow Depth - default (mm). [optional]  # noqa: E501
            precip (float): Accumulated precipitation since last forecast point - default (mm). [optional]  # noqa: E501
            temp (float): Temperature (Average) - default (C). [optional]  # noqa: E501
            dewpt (float): Dewpoint (Average) - default (C). [optional]  # noqa: E501
            max_temp (float): Maximum daily Temperature - default (C). [optional]  # noqa: E501
            min_temp (float): Minimum daily Temperature - default (C). [optional]  # noqa: E501
            app_max_temp (float): Apparent Maximum daily Temperature - default (C). [optional]  # noqa: E501
            app_min_temp (float): Apparent Minimum daily Temperature - default (C). [optional]  # noqa: E501
            rh (int): Relative Humidity as a percentage (%). [optional]  # noqa: E501
            clouds (int): Cloud cover as a percentage (%). [optional]  # noqa: E501
            weather (ForecastWeather): [optional]  # noqa: E501
            slp (float): Mean Sea level pressure (mb). [optional]  # noqa: E501
            pres (float): Pressure (mb). [optional]  # noqa: E501
            uv (float): UV Index. [optional]  # noqa: E501
            max_dhi (float): [Deprecated] Max direct component of solar insolation (W/m^2). [optional]  # noqa: E501
            vis (float): Average Visibility default (KM). [optional]  # noqa: E501
            pop (float): Chance of Precipitation as a percentage (%). [optional]  # noqa: E501
            moon_phase (float): Moon phase. [optional]  # noqa: E501
            sunrise_ts (int): Sunrise unix timestamp. [optional]  # noqa: E501
            sunset_ts (int): Sunset unix timestamp. [optional]  # noqa: E501
            moonrise_ts (int): Moonrise unix timestamp. [optional]  # noqa: E501
            moonset_ts (int): Moonset unix timestamp. [optional]  # noqa: E501
            pod (str): Part of the day (d = day, n = night). [optional]  # noqa: E501
            wind_spd (float): Wind Speed (default m/s). [optional]  # noqa: E501
            wind_dir (int): Wind direction. [optional]  # noqa: E501
            wind_cdir (str): Cardinal wind direction. [optional]  # noqa: E501
            wind_cdir_full (str): Cardinal wind direction (text). [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)