import random 

class ValidatorSelection:
    def __init__(self):
        self.stakers={}
    
    def add_staker(self, validator, stake):
        self.stakers[validator] = self.stakers.get(validator, 0) + stake 

    def select_validator(self):
        total_stake = sum(self.stakers.values())
        pick = random.uniform(0, total_stake)
        current = 0
        for validator, stake in self.stakers.items():
            current += stake
            if current > pick:
                return validator
