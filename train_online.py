from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.train import online
from rasa_core.utils import EndpointConfig
from rasa_core.policies.fallback import FallbackPolicy
from rasa_core.policies.keras_policy import KerasPolicy

logger = logging.getLogger(__name__)


def run_train_online(interpreter,
                       domain_file="domain.yml",
                       training_data_file='data/stories.md'):
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    fallback = FallbackPolicy(fallback_action_name="action_default_fallback",
                              core_threshold=0.3,
                              nlu_threshold=0.9)
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=2), KerasPolicy(), fallback],
                  interpreter=interpreter,
                  action_endpoint=action_endpoint)

    data = agent.load_data(training_data_file)
    agent.train(data,
                batch_size=50,
                epochs=300,
                max_training_samples=1000)
    online.serve_agent(agent)
    return agent


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/nlumodel')
    run_train_online(nlu_interpreter)