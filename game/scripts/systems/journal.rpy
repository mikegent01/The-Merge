
default collected_tapes = []
default unlocked_books = []
default journal_entries = []
default missions = {"active": [], "completed": []}
init python:
    def add_mission(title, description, objectives=None):
        if objectives is None: objectives = []
        current_day = getattr(store, 'day', 1)
        if any(m["title"] == title for m in persistent.missions["active"]): return

        new_mission = {"title": title, "description": description, "objectives": objectives, "progress": 0, "date_added": f"Day {current_day}"}
        persistent.missions["active"].append(new_mission)
        renpy.notify("New mission added: " + title)

    def update_mission_progress(title, progress):
        for mission in persistent.missions["active"]:
            if mission["title"] == title:
                mission["progress"] = min(100, max(0, progress))
                if mission["progress"] == 100:
                    complete_mission(title)
                return True
        return False

    def complete_mission(title):
        for i, mission in enumerate(persistent.missions["active"]):
            if mission["title"] == title:
                mission["progress"] = 100
                persistent.missions["completed"].append(mission)
                persistent.missions["active"].pop(i)
                renpy.notify("Mission completed: " + title)
                return True
        return False

    def add_journal_entry(title, content):
        current_day = getattr(store, 'day', 1)
        entry = {"title": title, "content": content, "date": f"Day {current_day}"}
        persistent.journal_entries.append(entry)
        renpy.notify("New journal entry added")

    def unlock_book(title, text_file, preview="images/inventory/inventory_hud/default_book.png"):
        current_day = getattr(store, 'day', 1)
        if any(b["title"] == title for b in store.unlocked_books): return
        if renpy.loadable(text_file):
            new_book = {"title": title, "text_file": text_file, "preview": preview, "date_unlocked": f"Day {current_day}"}
            store.unlocked_books.append(new_book)
        else:
            renpy.notify("Error: Book file not found: " + text_file)

    def load_book_text(text_file):
        try:
            with renpy.file(text_file) as f:
                content = f.read().decode("utf-8")
            words = content.split()
            return [" ".join(words[i:i + 250]) for i in range(0, len(words), 250)]
        except:
            return ["Error loading book content."]    