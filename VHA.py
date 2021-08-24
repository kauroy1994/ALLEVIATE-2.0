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
    my_vha.set_guidelines([depression(X):-significant(X,S),
                           significant(X,S):-depSymptom(X,S);freq(S,"high")])
    
                           depSymptom(X,"feelings_of_sadness"),
                           depSymptom(X,"tearfulness"),
                           depSymptom(X,"emptiness"),
                           depSymptom(X,"hopelessness"),
                           depSymptom(X,"angry_outbursts"),
                           depSymptom(X,"irritability"),
                           depSymptom(X,"frustration"),
                           depSymptom(X,"loss_of_interest"),
                           depSymptom(X,"loss_of_pleasure"),
                           depSymptom(X,"loss_of_hobbies"),
                           depSymptom(X,"sleep_disturbances"),
                           depSymptom(X,"insomnia"),
                           depSymptom(X,"sleeping_too_much"),
                           depSymptom(X,"tiredness"),
                           depSymptom(X,"lack_of_energy"),
                           depSymptom(X,"reduced_appetite"),
                           depSymptom(X,"weight_loss"),
                           depSymptom(X,"increased_cravings"),
                           depSymptom(X,"weight_gain"),
                           depSymptom(X,"anxiety"),
                           depSymptom(X,"agitation"),
                           depSymptom(X,"restlessness"),
                           depSymptom(X,"slowed_thinking"),
                           depSymptom(X,"slow_speaking"),
                           depSymptom(X,"slow_body_movements"),
                           depSymptom(X,"feelings_of_worthlessness"),
                           depSymptom(X,"feelings_of_guilt"),
                           depSymptom(X,"feelings_of_failure"),
                           depSymptom(X,"feelings_of_blame"),
                           depSymptom(X,"trouble_thinking"),
                           depSymptom(X,"trouble_concentrating"),
                           depSymptom(X,"trouble_with_decisions"),
                           depSymptom(X,"trouble_remembering_things"),
                           depSymptom(X,"frequent_thoughts_of_death"),
                           depSymptom(X,"suicidal_thoughts"),
                           depSymptom(X,"suicide_attempts"),
                           depSymptom(X,"suicide"),
                           depSymptom(X,"unexplained_problems")])

