init python:
    selected_liquids = []
    selected_container = None
    def add_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                liquid["amount"] += amount
                break

    def remove_liquid(liquid_name, amount):
        for liquid in liquid_inventory:
            if liquid["name"] == liquid_name:
                if liquid["amount"] >= amount: liquid["amount"] -= amount
                else: renpy.notify("Not enough liquid available.")
                break

    def add_liquid_to_selected(liquid):
        if not selected_container: return
        amount = 10
        if selected_container["current_amount"] + amount > selected_container["capacity"]:
            renpy.notify("Not enough space in the container!")
            return
        if amount > liquid["amount"]:
            renpy.notify("Not enough liquid available!")
            return

        found = False
        for content in selected_container["contents"]:
            if content["name"] == liquid["name"]:
                content["amount"] += amount
                found = True
                break
        if not found:
            selected_container["contents"].append({"name": liquid["name"], "amount": amount})

        selected_container["current_amount"] += amount
        liquid["amount"] -= amount
        renpy.notify(f"Added {amount} ml of {liquid['name']} to {selected_container['name']}.")

    def mix_liquids(container, liquids):
        recipe_name = check_mix_recipe(container)
        if recipe_name:
            total_volume = sum(c["amount"] for c in container["contents"])
            container["contents"] = [{"name": recipe_name, "amount": total_volume}]
            container["current_amount"] = total_volume
            renpy.notify(f"Successfully created {recipe_name}!")
        else:
            renpy.notify("No valid recipe found. The mixture turned into sludge.")
            container["contents"] = [{"name": "Sludge", "amount": container["current_amount"]}]

    def check_mix_recipe(container):
        container_liquids = {c["name"]: c["amount"] for c in container["contents"]}
        for recipe_name, recipe_ingredients in liquid_mix_recipes.items():
            if all(ingredient in container_liquids and container_liquids[ingredient] >= amount for ingredient, amount in recipe_ingredients.items()):
                return recipe_name
        return None

    def drain_liquid(container):
        if container["contents"]:
            container["contents"].clear()
            container["current_amount"] = 0
            renpy.notify(f"Drained all liquid from the {container['name']}.")

    def pour_liquid(source_container, target_container):
        if source_container["contents"]:
            # Simplified: Pour all contents
            total_pour_amount = source_container["current_amount"]
            if target_container:
                if target_container["current_amount"] + total_pour_amount <= target_container["capacity"]:
                    # Basic mixing: just add lists. A real system would be more complex.
                    target_container["contents"].extend(source_container["contents"])
                    target_container["current_amount"] += total_pour_amount
                    source_container["contents"].clear()
                    source_container["current_amount"] = 0
                    renpy.notify(f"Poured contents from {source_container['name']} to {target_container['name']}.")
                else:
                    renpy.notify("Not enough space in the target container!")
            else: # Pour to ground
                source_container["contents"].clear()
                source_container["current_amount"] = 0
                renpy.notify(f"Poured contents from {source_container['name']} to the ground.")
