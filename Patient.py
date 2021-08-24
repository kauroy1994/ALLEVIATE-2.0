from random import random
class Patient(object):

    count = 0

    possible_facts = ["depSymptom(X,feelings_of_sadness)",
                      "depSymptom(X,tearfulness)",
                      "depSymptom(X,emptiness)",
                      "depSymptom(X,hopelessness)",
                      "depSymptom(X,angry_outbursts)",
                      "depSymptom(X,irritability)",
                      "depSymptom(X,frustration)",
                      "depSymptom(X,loss_of_interest)",
                      "depSymptom(X,loss_of_pleasure)",
                      "depSymptom(X,loss_of_hobbies)",
                      "depSymptom(X,sleep_disturbances)",
                      "depSymptom(X,insomnia)",
                      "depSymptom(X,sleeping_too_much)",
                      "depSymptom(X,tiredness)",
                      "depSymptom(X,lack_of_energy)",
                      "depSymptom(X,reduced_appetite)",
                      "depSymptom(X,weight_loss)",
                      "depSymptom(X,increased_cravings)",
                      "depSymptom(X,weight_gain)",
                      "depSymptom(X,anxiety)",
                      "depSymptom(X,agitation)",
                      "depSymptom(X,restlessness)",
                      "depSymptom(X,slowed_thinking)",
                      "depSymptom(X,slow_speaking)",
                      "depSymptom(X,slow_body_movements)",
                      "depSymptom(X,feelings_of_worthlessness)",
                      "depSymptom(X,feelings_of_guilt)",
                      "depSymptom(X,feelings_of_failure)",
                      "depSymptom(X,feelings_of_blame)",
                      "depSymptom(X,trouble_thinking)",
                      "depSymptom(X,trouble_concentrating)",
                      "depSymptom(X,trouble_with_decisions)",
                      "depSymptom(X,trouble_remembering_things)",
                      "depSymptom(X,frequent_thoughts_of_death)",
                      "depSymptom(X,suicidal_thoughts)",
                      "depSymptom(X,suicide_attempts)",
                      "depSymptom(X,suicide)",
                      "depSymptom(X,unexplained_problems)"]

    @staticmethod
    def get_id():

        return Patient.count

    def __init__(self):

        self.facts = []

        for fact in Patient.possible_facts:
            if random() < 0.5:
                self.facts.append(fact.replace('X','p'+str(Patient.get_id())))
                if random() < 0.5:
                    self.facts.append('freq('+'p'+str(Patient.get_id())+','+fact.split(',')[1][:-1]+',high'+')')

        Patient.count += 1           
