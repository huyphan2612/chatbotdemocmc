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
        person_phonenumber = tracker.get_slot('person_phonenumber')

        ## Instance to connect to SQL Server
        conn = pymssql.connect(server="10.222.238.59", user="asap", password="p@sswOrd", database="CMIS_ASAP")
        cursor = conn.cursor()

        cursor.execute('''SELECT [Phone]
          FROM [CMIS_ASAP].[dbo].[UserGroups] ug
          LEFT JOIN [CMIS_ASAP].[dbo].[Users] u on ug.UserID = u.ID
          where ug.GroupID=10099 and [LastName] like %s''', person_phonenumber)

        for row in cursor:
            phonenumber  = row[0]

        response = """Đây là số điện thoại của {}: {}""".format(
            person_phonenumber, phonenumber)

        dispatcher.utter_message(response)

        conn.close()
        return [SlotSet('person_phonenumber', person_phonenumber)]

class ActionLookupEmail(Action):
    def name(self):
        return 'action_lookup_email'

    def run(self, dispatcher, tracker, domain):
        person_email = tracker.get_slot('person_email')

        ## Instance to connect to SQL Server
        conn = pymssql.connect(server="10.222.238.59", user="asap", password="p@sswOrd", database="CMIS_ASAP")
        cursor = conn.cursor()

        cursor.execute('''SELECT [Email]
          FROM [CMIS_ASAP].[dbo].[UserGroups] ug
          LEFT JOIN [CMIS_ASAP].[dbo].[Users] u on ug.UserID = u.ID
          where ug.GroupID=10099 and [LastName] like %s''', person_email)

        for row in cursor:
            email = row[0]

        response = """Đây là email của {}: {}""".format(
            person_email, email)

        dispatcher.utter_message(response)

        conn.close()
        return [SlotSet('person_email', person_email)]