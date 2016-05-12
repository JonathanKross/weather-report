import requests

wunder_key = "60e75ccda6ae8676"
base_url = 'http://api.wunderground.com/api/60e75ccda6ae8676/'
zipcode = input("What zipcode would you like to search for? ")
url = base_url + 'conditions/forecast10day/astronomy/alerts/currenthurricane/q/{}.json'.format(zipcode)
response = requests.get(url).json()


class CurrentConditions:

    def __init__(self, response):
        self.temp = response['current_observation']['temp_f']
        self.description = response['current_observation']['weather']

    def __str__(self):
        return "\nCurrent Temp: {}. Current Conditions: {}\n".format(
                                                            self.temp,
                                                            self.description)


class TenDay:

    def __init__(self, response):
        self.temp = response['current_observation']['temp_f']
        self.description = response['current_observation']['weather']
        self.tenday = ''

    def get_ten_day(self, response):

        for n in range(20):

            tenday_period = response['forecast']['txt_forecast']['forecastday'][n]['title']
            tenday_forecast = response['forecast']['txt_forecast']['forecastday'][n]['fcttext']
            self.tenday += "\n{}: {}\n".format(tenday_period, tenday_forecast)

        return self.tenday

    def __str__(self):
        return self.tenday


class SunriseSunset:

    def __init__(self, response):
        self.sunrise_hour = response['moon_phase']['sunrise']['hour']
        self.sunrise_minute = response['moon_phase']['sunrise']['minute']
        self.sunset_hour = response['moon_phase']['sunset']['hour']
        self.sunset_minute = response['moon_phase']['sunset']['minute']
        self.sunset_h12 = (int(self.sunrise_hoursunset_hour)-12)

    def __str__(self):
        return "\nSunrise: {}:{} am. Sunset {}:{} pm.\n".format(
                                                            self.sunrise_hour,
                                                            self.sunrise_minute,
                                                            self.sunset_h12,
                                                            self.sunset_minute)


class Alerts:

    def __init__(self, response):
        self.alert = False

    def assign_alerts(self,response):
        if not response['alerts']:
            self.alert = 'No alerts'
            return self.alert
        else:
            for alert in response['alerts']:
                self.alert = response['alerts'][0]['message']
                return self.alert

    def __str__(self):
        return self.alert


class Hurricanes:

    def __init__(self, response):
        self.hurricanes = False


    def assign_hurricanes(self, response):
        hurricanes = ''

        if not response['currenthurricane']:
            self.hurricanes = 'None'

        else:
            for hurricane in response['currenthurricane']:
                hurricanes += hurricane['stormInfo']['stormName']+'\n'
            self.hurricanes = hurricanes

        return self.hurricanes

    def __str__(self):
        return self.hurricanes
