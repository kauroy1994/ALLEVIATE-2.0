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

    def prove_examples(self,patient_objects):
        '''proves all consequents in a loop
           from patient facts using guidelines
        '''
        examples = []
        true_examples = []
        symptoms = [x.split(',')[1][:-1] for x in Patient.possible_facts]
        patients = ['p'+str(i) for i in range(Patient.count)]
        for patient in patients:
            examples.append("depression("+patient+')')
            for symptom in symptoms:
                examples.append("significant("+patient+','+symptom+')')


        for example in examples:
            before_count = 0
            while True:
                after_count = before_count
                for guideline in self.guidelines:
                    if example.split('(')[0] in guideline.split(":-")[0]:
                        Prover.rule = guideline
                        Patient_id = example.split('(')[1][1:-1]
                        for patient in patient_objects:
                            if patient.id == Patient_id:
                                Prover.facts = patient.facts
                                break
                        print (example)
                        print (Prover.rule)
                        print (Prover.facts)
                        input()
                        if Prover.prove_rule(example):
                            true_examples.append(example)
                            after_count += 1
                            break
                if after_count == before_count:
                    break
                before_count = after_count
                print (true_examples)
                input()
        return true_examples
                           
#============TESTER FUNCTIONS===============

def main():

    my_vha = VHA()
    my_vha.set_guidelines(["depression(X):-significant(X,S)",
                           "significant(X,S):-depsymptom(X,S);freq(X,S,high)"])
    
    patients = []
    patient = Patient()
    patients.append(patient)
    facts = my_vha.prove_examples(patients)
    '''
    Prover.rule = my_vha.guidelines[1]
    Prover.facts = patient.facts
    examples = create_examples()
    print (Prover.facts)
    print (Prover.rule)
    print (examples[1])
    print (Prover.prove_rule(examples[1]))
    '''

main()
    

