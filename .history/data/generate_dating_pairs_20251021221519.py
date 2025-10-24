# Gender definitions
MALE = "male"
FEMALE = "female"
NON_BINARY = "non_binary"

# Alternative: Using Enum for better type safety
from enum import Enum

class Gender(Enum):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"

core_domain = {
    "values": [
        "family", "honesty", "spirituality", "materialistic", "career"
    ],
    "lifestyle": [
        "social", "quiet", "active", "relaxed", "organized", "disorganized", "urban", "suburban", "country"
    ],
    "interests": [
        "music", "movies", "tv", "gaming", "dogs", "cats"
    ],
    "activities": [
        "hiking", "sports", "dog training", "gardening", "painting", "writing"
    ],
    "dealbreakers": [
        "smoking", "drinking", "religion", "controlling behavior"
    ]
}

positive_actions = ["I love", "I believe in", "I enjoy", "I am happy about"]
negative_actions = ["I don't like", "I cannot stand", "I hate", "I am not happy about"]

class InstructionalPair:
    def __init__(self, gender1, text1, gender2, text2, value=None):
        self.value = value
        self.gender1 = gender1
        self.text1 = text1
        self.gender2 = gender2
        self.text2 = text2

def generate_dating_pairs(core_domain, positive_actions, negative_actions):
    # Implementation here
    pass

def main():
    # Example usage with different gender definitions:
    
    # Using string constants
    pair1 = InstructionalPair(MALE, "I love hiking", FEMALE, "I enjoy reading")
    
    # Using Enum
    pair2 = InstructionalPair(Gender.MALE, "I love hiking", Gender.FEMALE, "I enjoy reading")
    
    # Using direct strings
    pair3 = InstructionalPair("male", "I love hiking", "female", "I enjoy reading")
    
    print("Gender examples created successfully!")

if __name__ == "__main__":
    main()  