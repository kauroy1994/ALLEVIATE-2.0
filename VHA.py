from Patient import Patient
from Prover import Prover

class VHA(object):

    def __init__(self,
                 facts=[],
                 schema = [],
                 abstractions = [],
                 guidelines = [],
                 decode_instructions = [],
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

    def set_guidelines(self,
                       guidelines):
        '''sets the list of guidelines
           KG init
        '''

        self.guidelines = guidelines


    def add_guideline(self,
                      guideline):
        '''adds a guideline to the list of guidelines
           as a horn clause
        '''

        self.guidelines.append(guideline)

    def add_facts(self,
                  fact):
        '''adds a fact to the list of facts
           as a predicate - KG update/init
        '''

        self.facts.append(fact)

    def set_schema(self,
                   schema):
        '''sets schema for the predicates
           in the fact file - KG init
        '''

        self.schema = schema

    def update_schema(self,
                      line,
                      add = True):
        '''updates the schema - KG update
           line can be added/deleted
        '''

        if add:
            self.schema.append(line)
        else:
            self.schema.remove(line)


#============TESTER FUNCTION===============
def main():

    my_vha = VHA()
    my_vha.set_guidelines(["depression(X):-significant(X,S)",
                           "significant(X,S):-depSymptom(X,S);freq(S,high)"])

    patient = Patient()
    print (patient.facts)

main()
    

