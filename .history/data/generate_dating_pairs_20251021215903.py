core_domain = {
    "values": [
        "family", "honesty", "spirituality", "materialistic", "career"
    ],
    "lifestyle": [
        "social", "quiet, active", "relaxed", "organized", "disorganized"
    ],
    "interests": [
       "music",  "movies", "tv", "gaming"
    ,
    "activities": []
        "hiking", "sports", "dog training", "gardening", "painting", "writing",
    ],
    "dealbreakers": [
        "smoking", "drinking", "drugs", "religion", "racism"
    ]
}

positive_actions = ["I love", "I belive in", "I enjoy", "I am happy about"];
negative_actions = ["I don't like", "I don't believe in", "I don't enjoy", "I am not happy about"];

def generate_dating_pairs(core_domain, positive_actions, negative_actions):
    dating_pairs = []
    for value in core_domain["values"]:
        for lifestyle in core_domain["lifestyle"]:
            for interest in core_domain["interests"]:
                for activity in core_domain["activities"]:
                    for dealbreaker in core_domain["dealbreakers"]:
                        dating_pairs.append({"value": value, "lifestyle": lifestyle, "interest": interest, "activity": activity, "dealbreaker": dealbreaker})
    return dating_pairs

def main():
    pass

if __name__ == "__main__":
    main()  