from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
import pymssql


class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '2585abb899344506a0865040181409'  # your apixu key
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
            condition, city, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

class ActionLookupPhonenumber(Action):
    def name(self):
        return 'action_lookup_phonenumber'

    def run(self, dispatcher, tracker, domain):
        per = tracker.get_slot('person')

        ## Instance to connect to SQL Server
        conn = pymssql.connect(server="13.76.131.229", user="sa", password="P@ssw0rd", database="CMCSISG_Contact")
        cursor = conn.cursor()

        cursor.execute('''[Phone]
                      FROM [CMCSISG_Contact].[dbo].[Contacts]
                      WHERE [LastName] like %s''', per)

        for row in cursor:
            phonenumber  = row[0]

        response = """Đây là số điện thoại của {}: {}""".format(
            per, phonenumber)

        dispatcher.utter_message(response)

        conn.close()
        return [SlotSet('person', per)]

class ActionLookupEmail(Action):
    def name(self):
        return 'action_lookup_email'

    def run(self, dispatcher, tracker, domain):
        per = tracker.get_slot('person')

        ## Instance to connect to SQL Server
        conn = pymssql.connect(server="13.76.131.229", user="sa", password="P@ssw0rd", database="CMCSISG_Contact")
        cursor = conn.cursor()

        cursor.execute('''SELECT [Email]
                        FROM [CMCSISG_Contact].[dbo].[Contacts]
                        WHERE [LastName] like %s''', per)

        for row in cursor:
            email = row[0]

        response = """Đây là email của {}: {}""".format(
            per, email)

        dispatcher.utter_message(response)

        conn.close()
        return [SlotSet('person', per)]