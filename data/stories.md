## Generated Story -8448706230886248124
* greet
    - utter_greet
* inform_weather{"info_lookup_type": "Thoi tiet", "location": "Saigon"}
    - slot{"info_lookup_type": "Thoi tiet"}
    - slot{"location": "Saigon"}
    - action_weather
    - slot{"location": "Saigon"}
* joke_waiting_message
    - utter_waiting_message


## weather_story_001
* greet
   - utter_greet
* inform_weather{"info_lookup_type": "Thoi tiet"}
   - utter_ask_location
* inform_weather{"info_lookup_type": "Thoi tiet", "location": "London"}
   - action_weather
* goodbye
   - utter_goodbye
## weather_story_002
* greet
   - utter_greet
* inform_weather{"info_lookup_type": "Thoi tiet", "location": "Paris"}
   - action_weather
* goodbye
   - utter_goodbye  
## weather_story_003
* greet
   - utter_greet
* inform_weather{"info_lookup_type": "Thoi tiet"}
   - utter_ask_location
* inform_weather{"info_lookup_type": "Thoi tiet", "location": "Sai gon"}
   - action_weather
* goodbye
   - utter_goodbye
   - action_restart   
## weather_story_004
* inform_weather{"info_lookup_type": "Thoi tiet"}
   - utter_ask_location
* inform_weather{"info_lookup_type": "Thoi tiet", "location": "Sai gon"}
   - action_weather
   - action_restart 
## weather_story_005
* greet
   - utter_greet
* inform_weather{"info_lookup_type": "Thoi tiet"}
   - utter_ask_location
* inform_weather{"info_lookup_type": "Thoi tiet", "location": "Lithuania"}
   - action_weather
* goodbye
   - utter_goodbye
   - action_restart
## weather_story_006
* inform_weather{"info_lookup_type": "Thoi tiet", "location": "Sai gon"}
   - action_weather
   - action_restart    
   
## cmc_story_001
* greet
   - utter_greet
* lookup_phonenumber{"info_lookup_type": "so dien thoai"}
   - utter_ask_person_phone
* lookup_phonenumber{"info_lookup_type": "so dien thoai", "person": "Huy"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_002
* greet
   - utter_greet
* lookup_email{"info_lookup_type": "email"}
   - utter_ask_person_email
* lookup_email{"info_lookup_type": "email", "person": "Huy"}
   - action_lookup_email
* goodbye
   - utter_goodbye
   - action_restart   
## cmc_story_003
* joke_lick
   - utter_joke_lick
   - action_restart
## cmc_story_004
* greet
   - utter_greet
* joke_lick
   - utter_joke_lick
   - action_restart   
## cmc_story_005
* greet
   - utter_greet
* lookup_phonenumber{"info_lookup_type": "so dien thoai", "person": "Huy"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye
   - action_restart   
## cmc_story_006
* greet
   - utter_greet
* lookup_email{"info_lookup_type": "email", "person": "Huy"}
   - action_lookup_email
* goodbye
   - utter_goodbye
   - action_restart    
## cmc_story_007
* joke_insulting_bot
   - utter_insulting_bot
   - action_restart
## cmc_story_008
* joke_waiting_message
   - utter_waiting_message
   - action_restart
## cmc_story_009
* joke_seen
   - utter_joke_seen
   - action_restart
## cmc_story_010
* joke_love
   - utter_joke_love
   - action_restart
## cmc_story_011
* lookup_phonenumber{"info_lookup_type": "so dien thoai"}
   - utter_ask_person_phone
* lookup_phonenumber{"info_lookup_type": "so dien thoai", "person": "Huy"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_012
* lookup_email{"info_lookup_type": "email"}
   - utter_ask_person_email
* lookup_email{"info_lookup_type": "email", "person": "Huy"}
   - action_lookup_email
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_013
* lookup_phonenumber{"info_lookup_type": "so dien thoai", "person": "Tấn"}
   - action_lookup_phonenumber
* goodbye
   - utter_goodbye  
   - action_restart 
## cmc_story_014
* lookup_email{"info_lookup_type": "email", "person": "Thu"}
   - action_lookup_email
* goodbye
   - utter_goodbye   
   - action_restart
## cmc_story_015
* greet
   - utter_greet
* joke_insulting_bot
   - utter_insulting_bot
   - action_restart   
## cmc_story_016
* greet
   - utter_greet
* joke_waiting_message
   - utter_waiting_message
   - action_restart
## cmc_story_017
* greet
   - utter_greet
* joke_seen
   - utter_joke_seen
   - action_restart
## cmc_story_018
* greet
   - utter_greet
* joke_love
   - utter_joke_love
   - action_restart
## cmc_story_019
* greet
   - utter_greet
* joke_lick
   - utter_joke_lick
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_020
* greet
   - utter_greet
* joke_insulting_bot
   - utter_insulting_bot
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_021
* greet
   - utter_greet
* joke_waiting_message
   - utter_waiting_message
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_022
* greet
   - utter_greet
* joke_seen
   - utter_joke_seen
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_023
* greet
   - utter_greet
* joke_love
   - utter_joke_love
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_024
* thankyou
   - utter_thankyou
   - action_restart      
# cmc_story_025
* greet
   - utter_greet
* joke_lick
   - utter_joke_lick
* thankyou
   - utter_thankyou
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_026
* greet
   - utter_greet
* joke_insulting_bot
   - utter_insulting_bot
* thankyou
   - utter_thankyou
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_027
* greet
   - utter_greet
* joke_waiting_message
   - utter_waiting_message
* thankyou
   - utter_thankyou
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_028
* greet
   - utter_greet
* joke_seen
   - utter_joke_seen
* thankyou
   - utter_thankyou
* goodbye
   - utter_goodbye
   - action_restart
## cmc_story_029
* greet
   - utter_greet
* joke_love
   - utter_joke_love
* thankyou
   - utter_thankyou
* goodbye
   - utter_goodbye
   - action_restart
  
