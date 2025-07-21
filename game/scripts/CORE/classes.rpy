init python:

    class GameCharacter:
        
        def __init__(self, name, starting_stats, starting_emotions):
            self.name = name
            self.stats = starting_stats
            self.emotions = starting_emotions
            self.sanity = 100
            self.inventory = Inventory(owner=self, capacity=20)
            self.health = {
                "head": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 74},
                "body": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 70},
                "left_arm": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 74},
                "right_arm": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 70},
                "left_leg": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 73},
                "right_leg": {"status": "fine", "health": 100, "conditions": [], "temperature": 70, "cleanliness": 72}
            }
            self.relationships = {}
            self._initialize_stats()
        # === HEALTH & STATUS METHODS ===
        def heal(self, part, amount):
            if part in self.health:
                self.health[part]["health"] = min(self.health[part]["health"] + amount, self.max_health)
                renpy.notify(f"{self.name}'s {part.replace('_', ' ')} restored by {amount} points.")

        def take_damage(self, part, amount):
            if part in self.health:
                self.modify_cleanliness(part, -1)
                self.health[part]["health"] = max(self.health[part]["health"] - amount, 0)
                if self.health[part]["health"] == 0 and part == "head": renpy.jump("gameover")
        def has_item(self, item_name):
            return item_name in self.items
        def calculate_averages(self):
            body_part_count = len(self.health)
            if body_part_count == 0:
                return 0, 0, 0
            total_health = sum(status['health'] for status in self.health.values())
            total_cleanliness = sum(status['cleanliness'] for status in self.health.values())
            total_temperature = sum(status['temperature'] for status in self.health.values())
            return round(total_health / body_part_count), round(total_cleanliness / body_part_count), round(total_temperature / body_part_count)
        def is_stat_higher(self, stat_name, value_to_compare):
            """Checks if a character's stat is higher than a given value."""
            if stat_name in self.stats:
                return self.stats[stat_name]["current_value"] > value_to_compare
            return False
        def get_relationship_description(self, person_name):
            """Gets the relationship status description for a specific person."""
            if person_name not in self.relationships:
                return "Stranger"
            
            rel = self.relationships[person_name]
            trust = rel.get("trust", 0)
            friendship = rel.get("friendship", 0)
            hostility = rel.get("hostility", 0)     

            if trust > 80 and friendship > 80: return "Best Friend"
            if trust > 70 and friendship > 70: return "Close Friend"
            if friendship > 50: return "Friend"
            if hostility > 70: return "Enemy"
            if hostility > 50: return "Adversary"
            if trust > 50: return "Trusted Associate"
            return "Acquaintance"        
        def add_condition(self, part, new_condition):
            if part in self.health and new_condition not in self.health[part]["conditions"]:
                self.health[part]["conditions"].append(new_condition)
                self.max_health = max(0, self.max_health - 10)
                self.take_damage(part, 10)
                renpy.notify(f"{self.name} is now afflicted with {new_condition}.")

        def remove_condition(self, part, condition):
            if part in self.health and condition in self.health[part]["conditions"]:
                self.health[part]["conditions"].remove(condition)
                self.max_health = min(100, self.max_health + 10)
                self.heal(part, 10)
                renpy.notify(f"{condition.capitalize()} has been cured for {self.name}.")

        def has_condition(self, part, condition):
            return condition in self.health.get(part, {}).get("conditions", [])

        def modify_cleanliness(self, part, amount):
            if part in self.health:
                self.health[part]['cleanliness'] = max(0, min(100, self.health[part]['cleanliness'] + amount))
                self._check_cleanliness_and_adjust_temp(part)

        def _check_cleanliness_and_adjust_temp(self, part):
            cleanliness = self.health[part]['cleanliness']
            if cleanliness > 90: self.health[part]['temperature'] -= 2
            elif cleanliness > 75: self.health[part]['temperature'] -= 1
            elif cleanliness < 50: self.health[part]['temperature'] += 1
            elif cleanliness < 25: self.health[part]['temperature'] += 2

        def check_body_temperatures(self):
            for part, data in self.health.items():
                temp = data['temperature']
                if temp > 90 and not self.has_condition(part, "overheating"): self.add_condition(part, "overheating")
                elif temp < 45 and not self.has_condition(part, "hypothermia"): self.add_condition(part, "hypothermia")
                elif 45 <= temp <= 90:
                    if self.has_condition(part, "overheating"): self.remove_condition(part, "overheating")
                    if self.has_condition(part, "hypothermia"): self.remove_condition(part, "hypothermia")

        def apply_room_temperature(self, room_temp):
            for part in self.health:
                variation = random.uniform(-3, 3)
                if part == "body": variation += random.uniform(7, 12)
                if part == "head": variation += random.uniform(3, 7)
                self.health[part]['temperature'] = round(room_temp + variation)
            self.check_body_temperatures()

        def use_medkit_item(self, part, item_name):
            if item_name not in medkit_contents:
                renpy.notify(f"You don't have {item_name.capitalize()} in your medkit!")
                return
            healing_info = medkit_contents[item_name]
            for condition in healing_info.get("conditions", []):
                if self.has_condition(part, condition): self.remove_condition(part, condition)
            self.heal(part, healing_info.get("healing", 0))
            del medkit_contents[item_name]
            renpy.notify(f"Used {item_name.capitalize()} on {self.name}'s {part.replace('_', ' ')}.")            
        def perform_roll(self, skill_name, base_chance=30, circumstance_bonus=0):

            if skill_name not in self.stats:
                renpy.notify(f"System Error: Skill '{skill_name}' not found for {self.name}!")
                return False # Automatically fail if the character doesn't have the skill.

            # 1. Get the base value from the character's stats
            skill_value = self.stats[skill_name].get("current_value", 0)
            
            # 2. Automatically calculate the bonus from the character's current emotions
            emotion_bonus = self._get_emotion_bonus(skill_name)
            
            # 3. Calculate the total chance of success
            total_chance = base_chance + skill_value + emotion_bonus + circumstance_bonus
            
            # Clamp the success chance to prevent impossible (0%) or guaranteed (100%) rolls
            total_chance = max(5, min(total_chance, 95))
            
            # 4. Perform the roll
            roll = renpy.random.randint(1, 100)
            
            success = (roll <= total_chance)
            
            # 5. Notify the player of the result (great for debugging)
            if success:
                renpy.notify(f"Success! (Rolled {roll} vs {total_chance})")
            else:
                renpy.notify(f"Failure. (Rolled {roll} vs {total_chance})")
                
            return success


        def _get_emotion_bonus(self, skill_name):
            """A private helper method to calculate the total emotion bonus for a skill."""
            sorted_emotions = sorted(self.emotions.items(), key=lambda x: x[1]["value"], reverse=True)
            if not sorted_emotions:
                return 0

            total_bonus = 0
            
            # Main bonus from the top emotion
            top_emotion_data = sorted_emotions[0][1]
            total_bonus += top_emotion_data.get("bonus", {}).get(skill_name, 0)
            
            # Reduced (halved) bonus from the second and third emotions
            for _, data in sorted_emotions[1:3]:
                reduced_bonuses = {stat: bonus // 2 for stat, bonus in data.get("bonus", {}).items()}
                total_bonus += reduced_bonuses.get(skill_name, 0)
                
            return total_bonus

        def _initialize_stats(self):
            for stat_name, data in self.stats.items():
                level = data.get("level", 1)
                data["current_value"] = (level * 4) + random.randint(1, 6)

        def add_experience(self, stat_name, amount):
            if stat_name in self.stats:
                stat = self.stats[stat_name]
                stat["current_xp"] += amount
                if stat["current_xp"] >= stat["max_xp"]:
                    self.level_up(stat_name)

        def level_up(self, stat_name):
            if stat_name in self.stats:
                stat = self.stats[stat_name]
                stat["level"] += 1
                stat["current_xp"] = 0
                stat["max_xp"] = round(stat["max_xp"] + random.randint(10, 35))
                stat["current_value"] += random.randint(1, 8)
                renpy.notify(f"{self.name}'s {stat_name.capitalize()} increased to level {stat['level']}!")

        def take_damage(self, part, amount):
            if part in self.health:
                self.health[part]['health'] -= amount
                renpy.notify(f"{self.name} took {amount} damage to the {part}.")
                if self.health[part]['health'] <= 0:
                    self.health[part]['health'] = 0

        def heal(self, part, amount):
            if part in self.health:
                max_health = 100
                self.health[part]['health'] += amount
                if self.health[part]['health'] > max_health:
                    self.health[part]['health'] = max_health

        def get_top_emotions(self):
            sorted_emotions = sorted(self.emotions.items(), key=lambda x: x[1]["value"], reverse=True)
            return sorted_emotions[:3]    
    class Inventory:
        def __init__(self, owner, capacity=20):
            self.owner = owner
            self.capacity = capacity
            self.items = []
            self.equipment = {
                "head": None, "body": None, "left_arm": None, "right_arm": None,
                "left_hand": None, "right_hand": None, "left_leg": None, "right_leg": None
            }
            self.liquids = [
                {"name": "Water", "amount": 100}, {"name": "Ethanol", "amount": 50},
                {"name": "Oil", "amount": 30}, {"name": "Glue", "amount": 30}
            ]
            self.containers = [
                {"name": "Regular Bottle", "capacity": 100, "current_amount": 0, "contents": []},
                {"name": "Water Bottle", "capacity": 500, "current_amount": 0, "contents": []},
            ]

        def get_item_weight(self, item_name):
            return items_database.get(item_name, {}).get("weight", 1)

        def get_total_weight(self):
            return sum(self.get_item_weight(item) for item in self.items)

        def add_item(self, item_name):
            if item_name not in items_database:
                renpy.notify(f"System Error: Item '{item_name}' does not exist.")
                return False
            if len(self.items) >= self.capacity:
                renpy.notify("Inventory is full.")
                return False
            self.items.append(item_name)
            renpy.notify(f"Added '{item_name}' to inventory.")
            return True

        def remove_item(self, item_name):
            if item_name in self.items:
                self.items.remove(item_name)
                return True
            return False

        def equip(self, item_name, slot):
            if item_name not in self.items:
                renpy.notify(f"Cannot equip: {item_name} not in inventory.")
                return
            if slot not in self.equipment:
                renpy.notify(f"System Error: Invalid slot '{slot}'.")
                return
            if self.equipment[slot] is not None:
                self.unequip(slot)
            self.equipment[slot] = item_name
            self.items.remove(item_name)
            renpy.notify(f"Equipped {item_name}.")

        def unequip(self, slot):
            if slot not in self.equipment or self.equipment[slot] is None:
                renpy.notify(f"Nothing to unequip from {slot}.")
                return
            item_to_unequip = self.equipment[slot]
            self.equipment[slot] = None
            self.items.append(item_to_unequip)
            renpy.notify(f"Unequipped {item_to_unequip}.")

        def use_item(self, item_name):
            if item_name not in self.items:
                return
            if item_name == "First aid kit":
                self.remove_item(item_name)
                renpy.show_screen("heal_menu")
            elif item_name == "Tissue":
                self.remove_item(item_name)
                self.add_item("Wet Tissue")
                renpy.notify("You blow your nose.")
            else:
                renpy.notify(f"You can't use the {item_name} right now.")
        def get_item_weight(self, item_name):
            return items_database.get(item_name, {}).get("weight", 1)
        def has_item(self, item_name):
            if item_name in self.items:
                return True
            for slot, equipped_item in self.equipment.items():
                if equipped_item == item_name:
                    return True
            return False
        def add_item(self, item_name):
            if item_name not in items_database:
                renpy.notify(f"System Error: Item '{item_name}' does not exist.")
                return False
            if len(self.items) >= self.capacity:
                renpy.notify("Inventory is full.")
                return False
            self.items.append(item_name)
            renpy.notify(f"Added '{item_name}' to inventory.")
            return True

        def remove_item(self, item_name):
            if item_name in self.items:
                self.items.remove(item_name)
                return True
            return False

        def equip(self, item_name, slot):
            if item_name not in self.items: return
            if slot not in self.equipment: return
            if self.equipment[slot] is not None: self.unequip(slot)
            self.equipment[slot] = item_name
            self.items.remove(item_name)
            renpy.notify(f"Equipped {item_name}.")

        def unequip(self, slot):
            if slot not in self.equipment or self.equipment[slot] is None: return
            item_to_unequip = self.equipment[slot]
            self.equipment[slot] = None
            self.items.append(item_to_unequip)
            renpy.notify(f"Unequipped {item_to_unequip}.")

        def use_item(self, item_name):
            if item_name not in self.items: return
            if item_name == "First aid kit":
                self.remove_item(item_name)
                renpy.show_screen("heal_menu")
            elif item_name == "Tissue":
                self.remove_item(item_name)
                self.add_item("Wet Tissue")
                renpy.notify("You blow your nose.")
            else:
                renpy.notify(f"You can't use the {item_name} right now.")


         