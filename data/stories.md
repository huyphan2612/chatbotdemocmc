## story_001
* greet
   - utter_greet
* inform_weather
   - utter_ask_location
* inform_weather[location=London]
   - slot{"location": "London"}
   - action_weather
* goodbye
   - utter_goodbye
## story_002
* greet
   - utter_greet
* inform_weather[location=Paris]
   - slot{"location": "Paris"}
   - action_weather
* goodbye
   - utter_goodbye 
## story_003
* greet
   - utter_greet
* inform_weather
   - utter_ask_location
* inform_weather[location=Vilnius]
   - slot{"location": "Vilnius"}
   - action_weather
* goodbye
   - utter_goodbye
## story_004
* greet
   - utter_greet
* inform_weather[location=Italy]
   - slot{"location": "Italy"}
   - action_weather
* goodbye
   - utter_goodbye 
## story_005
* greet
   - utter_greet
* inform_weather
   - utter_ask_location
* inform_weather[location=Lithuania]
   - slot{"location": "Lithuania"}
   - action_weather
* goodbye
   - utter_goodbye
   
   
   
   
## cmc_story_001
* greet
   - utter_greet
* lookup_phonenumber
   - utter_ask_person_phone
* lookup_phonenumber[person_phonenumber=Huy]
   - slot{"person_phonenumber": "Huy"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye
## cmc_story_002
* greet
   - utter_greet
* lookup_email
   - utter_ask_person_email
* lookup_email[person_email=Huy]
   - slot{"person_email": "Huy"}
   - action_lookup_email
* goodbye
   - utter_goodbye
## cmc_story_003
* joke_lick
   - utter_joke_lick
## cmc_story_004
* greet
   - utter_greet
* joke_lick
   - utter_joke_lick    
## cmc_story_005
* greet
   - utter_greet
* lookup_phonenumber[person_phonenumber=Huy]
   - slot{"person_phonenumber": "Huy"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye
## cmc_story_006
* greet
   - utter_greet
* lookup_email[person_email=Huy]
   - slot{"person_email": "Huy"}
   - action_lookup_email
* goodbye
   - utter_goodbye 
## cmc_story_007
* joke_insulting_bot
   - utter_insulting_bot
## cmc_story_008
* joke_waiting_message
   - utter_waiting_message
## cmc_story_009
* joke_seen
   - utter_joke_seen
## cmc_story_010
* joke_love
   - utter_joke_love
## cmc_story_011
* lookup_phonenumber
   - utter_ask_person_phone
* lookup_phonenumber[person_phonenumber=Huy]
   - slot{"person_phonenumber": "Huy"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye
## cmc_story_012
* lookup_email
   - utter_ask_person_email
* lookup_email[person_email=Huy]
   - slot{"person_email": "Huy"}
   - action_lookup_email
* goodbye
   - utter_goodbye
## cmc_story_013
* lookup_phonenumber[person_phonenumber=Huy]
   - slot{"person_phonenumber": "Huy"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye
## cmc_story_014
* lookup_email[person_email=Huy]
   - slot{"person_email": "Huy"}
   - action_lookup_email
* goodbye
   - utter_goodbye
## cmc_story_015
* greet
   - utter_greet
* joke_insulting_bot
   - utter_insulting_bot
## cmc_story_016
* greet
   - utter_greet
* joke_waiting_message
   - utter_waiting_message
## cmc_story_017
* greet
   - utter_greet
* joke_seen
   - utter_joke_seen
## cmc_story_018
* greet
   - utter_greet
* joke_love
   - utter_joke_love
## cmc_story_019
* greet
   - utter_greet
* joke_lick
   - utter_joke_lick
* goodbye
   - utter_goodbye
## cmc_story_020
* greet
   - utter_greet
* joke_insulting_bot
   - utter_insulting_bot
* goodbye
   - utter_goodbye
## cmc_story_021
* greet
   - utter_greet
* joke_waiting_message
   - utter_waiting_message
* goodbye
   - utter_goodbye
## cmc_story_022
* greet
   - utter_greet
* joke_seen
   - utter_joke_seen
* goodbye
   - utter_goodbye
## cmc_story_023
* greet
   - utter_greet
* joke_love
   - utter_joke_love
* goodbye
   - utter_goodbye   
 
  
