import os
import warnings
from typing import Dict
from bot_logic import BotLogic
from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

bot_logic = BotLogic()
############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    try:
        import spacy
        import transformers
        import wikipedia

    except:
        return "Following packages must be installed: ['spacy', 'transformers', 'wikipedia']"
    


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    bot_logic = BotLogic()
    output = []
    for text in request.text:
        # TODO Add code here
        response = bot_logic.generate_response(text)
        output.append(response)

    return SchemaUtil.create(SimpleText(), dict(text=output))

