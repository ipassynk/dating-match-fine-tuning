core_domain = {
    "values": [
        "family style", "honesty", "spirituality", "materialistic", "career oriented"
    ],
    "lifestyle": [
        "social", "quiet, active", "relaxed", "organized", "disorganized", "urban oriented", "suburban oriented", "country oriented"
    ],
    "interests": [
       "music",  "movies", "tv", "gaming", "dogs", "cats"
    ,
    "activities": [
        "hiking", "sports", "dog training", "gardening", "painting", "writing",
    ],
    "dealbreakers": [
        "smoking", "drinking", "religion", "controlling behavior"
    ]
}

positive_actions = ["I love", "I belive in", "I enjoy", "I am happy about"];
negative_actions = ["I don't like", "I cannot stand", "I hate", "I am not happy about"];

from enum import Enum

class Weights(Enum):
    values = 8
    dealbreakers = 10
    lifestyle = 7
    Interests = 5
    Activities = 3

class Label(Enum):
    COMPATIBLE = 1
    INCOMPATIBLE = 0

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class InstructionalPair(BaseModel):
    def __init__(self, label, gender1, action1, category1, 
    categoryValue1, gender2, action2, category2, categoryValue2):
        self.label = label
        self.gender1 = gender1
        self.action1 = action1
        self.categoryValue1 = categoryValue1
        self.gender2 = gender2
        self.action2 = action2
        self.categoryValue2 = categoryValue2

def generate_dating_pairs(core_domain, positive_actions, negative_actions):
    core_domain_interests = [{"category": "values", "value": value} for value in core_domain["interests"]]
    core_domain_activities = [{"category": "activities", "value": value} for value in core_domain["activities"]]
    core_domain_dealbreakers = [{"category": "dealbreakers", "value": value} for value in core_domain["dealbreakers"]]
    core_domain_lifestyle = [{"category": "lifestyle", "value": value} for value in core_domain["lifestyle"]]

    activities_interests = [core_domain_activities, core_domain_interests]]

    # Simple compatible pairs (shared positive preferences)
    for i in range(10):
        choice1 = randon.choice(activities_interests);
        choice2 = randon.choice(activities_interests);
        dating_pairs.append(InstructionalPair(Label.COMPATIBLE,Gender.MALE, 
            positive_actions[random.randint(0, len(positive_actions) - 1)], 
            choice1["category"], choice1["value"], 
            Gender.FEMALE, 
            positive_actions[random.randint(0, len(positive_actions) - 1)], choice2["category"], choice2["value"]))
∏
    # Incompatible pairs (shared negative preferences)
    for i in range(10):
        choice1 = randon.choice(core_domain_lifestyle);
        dating_pairs.append(InstructionalPair(Label.INCOMPATIBLE,Gender.MALE, 
            positive_actions[random.randint(0, len(positive_actions) - 1)], 
            choice1["category"], choice1["value"], Gender.FEMALE, 
            negative_actions[random.randint(0, len(negative_actions) - 1)], choice1["category"], choice1["value"]))

    # Dealbreaker scenarios
     for i in range(10):
        choice1 = randon.choice(core_domain_dealbreakers);
        dating_pairs.append(InstructionalPair(Label.INCOMPATIBLE,Gender.MALE, 
            positive_actions[random.randint(0, len(positive_actions) - 1)], 
            choice1["category"], choice1["value"], Gender.FEMALE, 
            negative_actions[random.randint(0, len(negative_actions) - 1)], choice1["category"], choice1["value"]))
    
    #Basic complex pairs (multi-preference without LLM)
    
    return dating_pairs

def main():
    pass

if __name__ == "__main__":
    main()  