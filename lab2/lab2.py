### Model-Bäsed reflex ägent

class ModelBasedReflexAgent:
    def __init__(self, rules, model):
        self.rules = rules 
        self.model = model
        
        def sense(self, environment):
            self.model.update(environment)
            
            
        def act(self):
            action = None
            for rule in self.rules:
                if rule.matches(self.model):
                    action = rule.action
                    break
            return action
        
        
        
class Rule:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action
        
        
    def matches(self, model):
        return self.condition(model)
    
    
    
class EnvironmentModel:
    def __init__(self, temperature):
        self.temperature = temperature
        
    def update(self, environment):
        self.temperature = environment.temperature
        


rules = [    Rule(lambda model: model.temperature < 70, "turn on heater"),    Rule(lambda model: model.temperature > 80, "turn on AC"),    Rule(lambda model: 70 <= model.temperature <= 80, "do nothing")]

model = EnvironmentModel(75)

agent = ModelBasedReflexAgent(rules, model)
