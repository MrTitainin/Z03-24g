"""
    Weatherbit.io - Swagger UI Weather API documentation

    This is the documentation for the Weatherbit Weather API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the `key` parameter.        An Example for a 5 day forecast for London, UK would be `http://api.weatherbit.io/v2.0/forecast/3hourly?city=London`&`country=UK`. See our [Weather API description page](https://www.weatherbit.io/api) for additional documentation.  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.current_weather_data_api import CurrentWeatherDataApi  # noqa: E501


class TestCurrentWeatherDataApi(unittest.TestCase):
    """CurrentWeatherDataApi unit test stubs"""

    def setUp(self):
        self.api = CurrentWeatherDataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_currentcitiescities_get(self):
        """Test case for currentcitiescities_get

        Returns a group of observations given a list of cities  # noqa: E501
        """
        pass

    def test_currentcity_idcity_id_get(self):
        """Test case for currentcity_idcity_id_get

        Returns a current observation by city id.  # noqa: E501
        """
        pass

    def test_currentcitycitycountrycountry_get(self):
        """Test case for currentcitycitycountrycountry_get

        Returns a Current Observation - Given City and/or State, Country.  # noqa: E501
        """
        pass

    def test_currentlatlatlonlon_get(self):
        """Test case for currentlatlatlonlon_get

        Returns a Current Observation - Given a lat/lon.  # noqa: E501
        """
        pass

    def test_currentpostal_codepostal_code_get(self):
        """Test case for currentpostal_codepostal_code_get

        Returns a current observation by postal code.  # noqa: E501
        """
        pass

    def test_currentstationsstations_get(self):
        """Test case for currentstationsstations_get

        Returns a group of observations given a list of stations  # noqa: E501
        """
        pass

    def test_currentstationstation_get(self):
        """Test case for currentstationstation_get

        Returns a Current Observation. - Given a station ID.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()