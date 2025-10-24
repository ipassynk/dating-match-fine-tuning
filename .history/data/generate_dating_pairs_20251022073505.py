import random
from enum import Enum
from pydantic import BaseModel

core_domain = {
    "values": [
        "family oriented",
        "honesty",
        "spirituality",
        "materialistic",
        "career oriented"
    ],
    "lifestyle": [
        "social",
        "quiet",
        "active",
        "relaxed",
        "organized",
        "disorganized",
        "urban oriented",
        "suburban oriented",
        "country oriented",
    ],
    "interests": ["music", "movies", "tv", "gaming", "dogs", "cats"],
    "activities": [
        "hiking",
        "sports",
        "dog training",
        "gardening",
        "painting",
        "writing",
    ],
    "dealbreakers": ["smoking", "drinking", "religious beliefs", "controlling behavior", "child-free"],
}

positive_actions = ["I love", "I believe in", "I enjoy", "I am happy about"]
negative_actions = ["I don't like", "I cannot stand", "I hate", "I am not happy about"]


class Weights(Enum):
    values = 8
    dealbreakers = 10
    lifestyle = 7
    Interests = 5
    Activities = 3


class Label(Enum):
    COMPATIBLE = 1
    INCOMPATIBLE = 0

class PairType(Enum):
    SIMPLE_COMPATIBLE = 1
    SIMPLE_INCOMPATIBLE = 0
    COMPLEX_COMPATIBLE = 2
    COMPLEX_INCOMPATIBLE = 3


class InstructionalPair(BaseModel):
    def __init__(
        self,
        label,
        pair_type
        text1,
        category1,
        text2,
        category2,
    ):
        self.label = label
        self.pair_type = pair_type
        self.action2 = action2
        self.category1 = category1
        self.category2 = category2
        self.text_1 = f"boy: {text1}"
        self.text_2 = f"girl: {text2}"


def generate_dating_pairs(core_domain, positive_actions, negative_actions):
    dating_pairs = []

    interests = [
        {"category": "interests", "value": value} for value in core_domain["interests"]
    ]
    activities = [
        {"category": "activities", "value": value}
        for value in core_domain["activities"]
    ]
    dealbreakers = [
        {"category": "dealbreakers", "value": value}
        for value in core_domain["dealbreakers"]
    ]
    lifestyle = [
        {"category": "lifestyle", "value": value} for value in core_domain["lifestyle"]
    ]

    activities_interests = activities + interests

    # Simple compatible pairs (shared positive preferences)
    for i in range(10):
        choice = random.choice(activities_interests)
        dating_pairs.append(
            InstructionalPair(
                Label.COMPATIBLE,
                f"{random.choice(positive_actions)} {choice['value']}",
                choice["category"],
                f"{random.choice(positive_actions)} {choice['value']}",
                choice["category"]
            )
        )
        dating_pairs.append(
            InstructionalPair(
                Label.COMPATIBLE,
                Gender.FEMALE,
                negative_actions[random.randint(0, len(negative_actions) - 1)],
                choice["category"],
                choice["value"],
                Gender.MALE,
                negative_actions[random.randint(0, len(negative_actions) - 1)],
                choice["category"],
                choice["value"],
            )
        )

    # Incompatible pairs (shared negative preferences)
    for i in range(10):
        choice = random.choice(lifestyle)
        dating_pairs.append(
            InstructionalPair(
                Label.INCOMPATIBLE,
                Gender.MALE,
                "I am",
                choice["category"],
                choice["value"],
                Gender.FEMALE,
                "I hate people who are",
                choice["category"],
                choice["value"],
            )
        )

    # Dealbreaker scenarios
    for i in range(10):
        choice = random.choice(dealbreakers)
        dating_pairs.append(
            InstructionalPair(
                Label.INCOMPATIBLE,
                Gender.MALE,
                positive_actions[random.randint(0, len(positive_actions) - 1)],
                choice["category"],
                choice["value"],
                Gender.FEMALE,
                negative_actions[random.randint(0, len(negative_actions) - 1)],
                choice["category"],
                choice["value"],
            )
        )
    # Basic complex pairs (multi-preference without LLM)
    for i in range(10):
        

    return dating_pairs


def main():
    pass


if __name__ == "__main__":
    main()
