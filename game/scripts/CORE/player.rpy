default player_initial_stats = {
    "intelligence": {"level": 2, "current_xp": 50, "max_xp": 77},
    "speech": {"level": 3, "current_xp": 0, "max_xp": 131},
    "strength": {"level": 5, "current_xp": 0, "max_xp": 230},
    "luck": {"level": 1, "current_xp": 0, "max_xp": 50},
    "speed": {"level": 2, "current_xp": 0, "max_xp": 87},
    "pain_tolerance": {"level": 2, "current_xp": 0, "max_xp": 90},
    "mental_resilience": {"level": 1, "current_xp": 0, "max_xp": 50},
    "medical": {"level": 1, "current_xp": 0, "max_xp": 50}
}

default player_initial_emotions = {
    "Authenticity": {"value": 50, "bonus": {"speech": 5, "luck": -2, "mental_resilience": -6, "pain_tolerance": -5, "perception": 3}},  # Added proficiency bonus
    "Authority": {"value": 60, "bonus": {"strength": 6, "intelligence": -5, "brute_force": 4}}, 
    "Composure": {"value": 20, "bonus": {"speech": 5, "strength": 3, "intelligence": -3, "pain_tolerance": 3, "social": -2}},
    "Confidence": {"value": 15, "bonus": {"speech": -3, "intelligence": -4, "mental_resilience": 4, "lie": -2}},
    "Dignity": {"value": 60, "bonus": {"speech": 5, "mental_resilience": 3, "luck": -2, "political": 3}},
    "Pride": {"value": 10, "bonus": {"intelligence": -5, "strength": 5, "mental_resilience": 6, "pain_tolerance": 5, "kick_power": 3}},
    "Curiosity": {"value": 15, "bonus": {"intelligence": -5, "strength": 5, "mental_resilience": 6, "pain_tolerance": 5, "kick_power": 3}},

}
default player_initial_proficiencies = {
    "strength": {
        "brute_force": {"level": 1, "current_value": 5, "current_xp": 0, "max_xp": 50, "display_name": "Savage Smash", "energy_cost": 15},  # Higher cost for powerful act
        "kick_power": {"level": 1, "current_value": 4, "current_xp": 0, "max_xp": 50, "display_name": "Powerful Kick", "energy_cost": 10},
        "punch": {"level": 1, "current_value": 6, "current_xp": 0, "max_xp": 50, "display_name": "Fist Strike", "energy_cost": 12},
    },
    "intelligence": {
        "perception": {"level": 2, "current_value": 8, "current_xp": 10, "max_xp": 80, "energy_cost": 8},
        "history": {"level": 1, "current_value": 3, "current_xp": 0, "max_xp": 50, "energy_cost": 5},
        "medical": {"level": 1, "current_value": 12, "current_xp": 20, "max_xp": 100, "energy_cost": 10},
    },
    "speech": {
        "political": {"level": 1, "current_value": 4, "current_xp": 0, "max_xp": 50, "display_name": "Diplomatic Debate", "energy_cost": 5},  # Lower cost for talk
        "social": {"level": 2, "current_value": 6, "current_xp": 15, "max_xp": 60, "display_name": "Charming Banter", "energy_cost": 7},
        "persuasion": {"level": 1, "current_value": 5, "current_xp": 0, "max_xp": 50, "display_name": "Convincing Words", "energy_cost": 6},
    },
    "luck": {
        "gamble": {"level": 1, "current_value": 3, "current_xp": 0, "max_xp": 50, "display_name": "Risky Gamble", "energy_cost": 10},
        "fortune": {"level": 1, "current_value": 4, "current_xp": 0, "max_xp": 50, "display_name": "Lucky Break", "energy_cost": 8},
    },
    "speed": {
        "sprinting": {"level": 1, "current_value": 5, "current_xp": 0, "max_xp": 50, "display_name": "Quick Sprint", "energy_cost": 12},
        "dodging": {"level": 1, "current_value": 4, "current_xp": 0, "max_xp": 50, "display_name": "Agile Dodge", "energy_cost": 10},
    },
}
default barns_initial_emotions = {
    "Authenticity": {"value": 10, "bonus": {"speech": 2}},
    "Authority": {"value": 80, "bonus": {"strength": 10}},
    "Composure": {"value": 40, "bonus": {"speech": 2}},
    "Confidence": {"value": 90, "bonus": {"speech": 5}},
    "Dignity": {"value": 20, "bonus": {"speech": 1}},
    "Pride": {"value": 60, "bonus": {"strength": 7}},
    "Curiosity": {"value": 5, "bonus": {"intelligence": 1}},
}
default barns = GameCharacter(
    name="Barns",
    starting_stats=player_initial_stats,
    starting_emotions=barns_initial_emotions,
    starting_proficiencies=player_initial_proficiencies
)
default soft_skills = ["intelligence", "speech", "luck", "mental_resilience", "medical", "leadership", "empathy", "creativity", "adaptability", "teamwork"]
default hard_skills = ["strength", "speed", "pain_tolerance"]
default player = GameCharacter(
    name="Benjamin",
    starting_stats=player_initial_stats,
    starting_emotions=player_initial_emotions,
    starting_proficiencies=player_initial_proficiencies     
)