core_domain = {
    "values": [
        "family", "honesty", "spirituality", "materialistic", "career"
    ],
    "lifestyle": [
        "social", "quiet, active", "relaxed", "organized", "disorganized", "urban", "suburban", "country"
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

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"

class InstructionalPair(BaseModel):
    def __init__(self, gender1, action1, category1, 
    categoryValue1, gender2, action2, category2, categoryValue2):
        self.value = value
        self.gender1 = gender1
        self.action1 = action1
        self.categoryValue1 = categoryValue1
        self.gender2 = gender2
        self.action2 = action2
        self.categoryValue2 = categoryValue2

def generate_dating_pairs(core_domain, positive_actions, negative_actions):
    core_domain_interests = [{"category": "values", "value": value} for value in core_domain["interests"]]
    core_domain_activities = [{"category": "activities", "value": value} for value in core_domain["activities"]]

    # Simple compatible pairs (shared positive preferences)
    always_positive = [core_domain_activities, core_domain_interests]]

    for i in range(10):
        choice1 = randon.choice(always_positive);
        choice2 = randon.choice(always_positive);
        dating_pairs.append(InstructionalPair(Gender.MALE, positive_actions[random.randint(0, len(positive_actions) - 1)], choice1["category"], choice1["value"], Gender.FEMALE, negative_actions[random.randint(0, len(positive_actions) - 1)], choice2["category"], choice2["value"]))

    #Incompatible pairs (shared negative preferences)

    return dating_pairs

def main():
    pass

if __name__ == "__main__":
    main()  