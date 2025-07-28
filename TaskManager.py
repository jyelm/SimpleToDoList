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

        def is_int(s:str) -> bool:
            try:
                int(s)
                return True
            except ValueError:
                return False
        try:
            if phrase:
                if is_int(phrase):
                    return action(int(phrase))
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
    def remove(cls, id):
        cls.tasks = {key:value for key, value in cls.tasks.items() if key != id} 
    @classmethod
    def show(cls):
        for i in cls.tasks.values():
            print(f"{i}\n")
    @classmethod
    def search(cls, keyword):
        for i in cls.tasks.values():
            if keyword in i:
                print(f"{i}\n")

class BST:
    """
    have the method of storage be a binary search tree instead of a simple dictionary
    """
    def __init__(self):
        self.root = None
    class Node:
        def __init__(self, key):
            self.left = None
            self.right = None
            self.key = key
    def insert(self,key):
        def _insert(node, key):
            if node is None:
                return BST.Node(key)
            parent = None
            temp = BST.Node(key)
            curr = node
            while curr is not None:
                parent = curr
                if curr.key > key:
                    curr = curr.left #traversing
                elif curr.key < key:
                    curr = curr.right
                else:
                    return node
            if key > parent.key:
                parent.right = temp
            else:
                parent.left = temp
            return node
        self.root = _insert(self.root, key)
  #when called, python binds insert to the class, which adds and unwanted positional argument. Static method tells python to just retunr raw function; maybe the benfit to useing classes in general is to just group all related information and functionality in the same namespace
    def inorder(self):
        def _inorder(root):
            if root:
                _inorder(root.left)
                print(root.key, end=" ")
                _inorder(root.right)
        _inorder(self.root)

tree = BST()
for k in (50,30,20,40,70,60,80):
    tree.insert(k)
tree.inorder()   # same output

"""
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
"""









         


