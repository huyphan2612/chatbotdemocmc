from rasa_core.channels.facebook import FacebookInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

# load your trained agent
nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/nlumodel')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = FacebookInput(
    fb_verify="rasa_bot_cmc",
    # you need tell facebook this token, to confirm your URL
    fb_secret="1b355ba9326d3fa3c3c29c1f2f51c306",  # your app secret
    fb_access_token="EAAS4CGbJkE4BAOJU1UTgYuYmjEd6qHLa2nAlGpyg1I4ruzzVEdLPuv03bmRE26xjQPhKu16Mesv3XkwqJqyZBMX4fpJ38fb2ANme64FUGc2CzU37Xtwqe2jto3iGcqZBEsRSjpRVom2ssE7isbZB1lxuLZC1ZBCtnjVoK4GrRTAZDZD"
    # token for the page you subscribed to
)

# set serve_forever=False if you want to keep the server running
agent.handle_channels([input_channel], 5004, serve_forever=True)