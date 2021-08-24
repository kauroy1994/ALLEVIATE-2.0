from random import random
class Patient(object):

    count = 0

    possible_facts = ["depsymptom(X,feelings_of_sadness)",
                      "depsymptom(X,tearfulness)",
                      "depsymptom(X,emptiness)",
                      "depsymptom(X,hopelessness)",
                      "depsymptom(X,angry_outbursts)",
                      "depsymptom(X,irritability)",
                      "depsymptom(X,frustration)",
                      "depsymptom(X,loss_of_interest)",
                      "depsymptom(X,loss_of_pleasure)",
                      "depsymptom(X,loss_of_hobbies)",
                      "depsymptom(X,sleep_disturbances)",
                      "depsymptom(X,insomnia)",
                      "depsymptom(X,sleeping_too_much)",
                      "depsymptom(X,tiredness)",
                      "depsymptom(X,lack_of_energy)",
                      "depsymptom(X,reduced_appetite)",
                      "depsymptom(X,weight_loss)",
                      "depsymptom(X,increased_cravings)",
                      "depsymptom(X,weight_gain)",
                      "depsymptom(X,anxiety)",
                      "depsymptom(X,agitation)",
                      "depsymptom(X,restlessness)",
                      "depsymptom(X,slowed_thinking)",
                      "depsymptom(X,slow_speaking)",
                      "depsymptom(X,slow_body_movements)",
                      "depsymptom(X,feelings_of_worthlessness)",
                      "depsymptom(X,feelings_of_guilt)",
                      "depsymptom(X,feelings_of_failure)",
                      "depsymptom(X,feelings_of_blame)",
                      "depsymptom(X,trouble_thinking)",
                      "depsymptom(X,trouble_concentrating)",
                      "depsymptom(X,trouble_with_decisions)",
                      "depsymptom(X,trouble_remembering_things)",
                      "depsymptom(X,frequent_thoughts_of_death)",
                      "depsymptom(X,suicidal_thoughts)",
                      "depsymptom(X,suicide_attempts)",
                      "depsymptom(X,suicide)",
                      "depsymptom(X,unexplained_problems)"]

    @staticmethod
    def get_id():

        return Patient.count

    def __init__(self):

        self.facts = []
        self.id = str(Patient.get_id())

        for fact in Patient.possible_facts:
            if random() < 0.5:
                self.facts.append(fact.replace('X','p'+self.id))
                if random() < 0.5:
                    self.facts.append('freq('+'p'+str(Patient.get_id())+','+fact.split(',')[1][:-1]+',high'+')')

        Patient.count += 1
