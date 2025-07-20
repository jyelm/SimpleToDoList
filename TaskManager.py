"""
The task manager needs to be able to store items in memory through descriptive words such as add, 
remove, find, list, and clear. The user should be able to retrieve the from the to do list by keyword,
one issue that may arise is that when the user inputs different entries, which will be differed by their id, 
with keywords both in their descirption, the to do list should be able to display both items. Maybe add a feature
where you can choose to group items, this may just add complexity when it comes to adding functinoality to the input of certain
descriptors
"""
from queue import Queue as q
import argparse
import sqlite3

# conn = sqlite3.connect("tasks.db")
# curr = conn.cursor()
# curr.execute("""
# CREATE TABLE IF NOT EXISTS tasks(
#     id  INTEGER PRIMARYT KEY AUTOINCREMENT,
#     description STRING NOT NULL
#              );
#              """)
# conn.commit()
# conn.close


class TaskManager:
    """
    for the scope of this porject, we can keep tasks as a class attribute, so when changed stays the same on every instance the task manager 
    class is created an object
    """
    ids = 1
    tasks = {}
    @classmethod
    def execute(cls, keyword:str, phrase=False):
        action = getattr(cls, keyword)
        try:
            if phrase:
                return action(phrase)
            else:
                return action()
        except:
            raise AttributeError(f"No action with {keyword}")
    @classmethod
    def add(cls, phrase):
        cls.tasks[cls.ids] = phrase
        cls.ids += 1
        # with sqlite3.connect('tasks.db') as conn:  #with automatically commits and closes
        #     curr = conn.cursor()
        #     curr.execute(
        #         "INSERT INTO tasks(description) VALUES(?);", #values(?) creates placeholder values to be replaced by the characters in phrase
        #         (phrase,)

        #     )


    @classmethod
    def remove(cls, phrase, id):
        cls.tasks = {key:value for key, value in cls.tasks.items() if key != id} 
    @classmethod
    def show(cls):
        for i in cls.tasks.values():
            print(f"{i}\n")
    @classmethod
    def search(cls, keyword):
        pass


def main():
    def int_or_str(value):
        try:
            return int(value)
        except ValueError:
            return value

    parser = argparse.ArgumentParser(
        description="A simple to-do list storer and accessor"
    )
    parser.add_argument(
        "function",
        type = str,
        help = "what do you want to do with the todo list?"
    )
    parser.add_argument(
        "item",
        type = int_or_str,
        nargs = "?", #makes the argument optional
        help = "the id of the entry you want to access or the phrase"
    )
    while True:
        try:
            line = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break
        if not line: #if the user just enters, it returns '' which is falsey 
            continue

        parts = line.split()
        if len(parts) > 1:
            parts = [parts[0], ' '.join(parts[1:])]

        try:
            args = parser.parse_args(parts)
        except SystemExit:
            continue

        TaskManager.execute(args.function, args.item)



if __name__ == "__main__":
    main()










         


