from Prover import Prover

class VHA(object):

    def __init__(self,
                 facts=[],
                 schema = [],
                 abstractions = [],
                 guidelines = [],
                 decode_instructions = []
                 nlg_module = None):

        '''constructor that stores knowledge graph
           abstraction to abstract concepts to map to guideline
           guidelines that contain mapping from abstract concepts to prescription
           prescription decoder for execution by VHA
           natural language generation module
        '''

        self.facts = facts
        self.schema = schema
        self.abstractions = abstractions
        self.guidelines = guidelines
        self.decode_instructions = decode_instructions
        self.nlg_module = nlg_module


#============TESTER FUNCTION===============
def main():

    my_vha = VHA()
        

