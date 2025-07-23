default player_initial_stats = {
    "intelligence": {"level": 2, "current_xp": 0, "max_xp": 77},
    "speech": {"level": 3, "current_xp": 0, "max_xp": 131},
    "strength": {"level": 5, "current_xp": 0, "max_xp": 230},
    "luck": {"level": 1, "current_xp": 0, "max_xp": 50},
    "speed": {"level": 2, "current_xp": 0, "max_xp": 87},
    "pain_tolerance": {"level": 2, "current_xp": 0, "max_xp": 90},
    "mental_resilience": {"level": 1, "current_xp": 0, "max_xp": 50},
    "medical": {"level": 1, "current_xp": 0, "max_xp": 50}
}

default player_initial_emotions = {
    "Authenticity": {"value": 50, "bonus": {"speech": 5, "luck": -2, "mental_resilience": -6, "pain_tolerance": -5}},
    "Authority": {"value": 60, "bonus": {"strength": 6, "intelligence": -5}},
    "Composure": {"value": 20, "bonus": {"speech": 5, "strength": 3, "intelligence": -3, "pain_tolerance": 3}},
    "Confidence": {"value": 15, "bonus": {"speech": -3, "intelligence": -4, "mental_resilience": 4}},
    "Dignity": {"value": 60, "bonus": {"speech": 5, "mental_resilience": 3, "luck": -2}},
    "Pride": {"value": 10, "bonus": {"intelligence": -5, "strength": 5, "mental_resilience": 6, "pain_tolerance": 5}},
}
default soft_skills = ["intelligence", "speech", "luck", "mental_resilience", "medical", "leadership", "empathy", "creativity", "adaptability", "teamwork"]
default hard_skills = ["strength", "speed", "pain_tolerance"]
default player = GameCharacter(
    name="Benjamin",
    starting_stats=player_initial_stats,
    starting_emotions=player_initial_emotions
)