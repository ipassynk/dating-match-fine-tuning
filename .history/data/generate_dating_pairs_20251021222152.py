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

class InstructionalPair:
    def __init__(self, gender1, action1, category1, gender2, action2, category2):
        self.value = value
        self.gender1 = gender1
        self.action1 = action1
        self.gender2 = gender2
        self.action2 = action2

def generate_dating_pairs(core_domain, positive_actions, negative_actions):
    for value in core_domain["values"]:
        for dealbreaker in core_domain["dealbreakers"]:
            for lifestyle in core_domain["lifestyle"]:
                for interest in core_domain["interests"]:
                    for activity in core_domain["activities"]:
                        dating_pairs.append(InstructionalPair(Gender.MALE, 
                        positive_actions[random.randint(0, len(positive_actions) - 1)], 
                        Gender.FEMALE, 
                        negative_actions[random.randint(0, len(negative_actions) - 1)]))
                        dating_pairs.append(InstructionalPair(Gender.FEMALE, 
                        positive_actions[random.randint(0, len(positive_actions) - 1)], 
                        Gender.MALE, 
                        negative_actions[random.randint(0, len(negative_actions) - 1)]))
    return dating_pairs

def main():
    pass

if __name__ == "__main__":
    main()  