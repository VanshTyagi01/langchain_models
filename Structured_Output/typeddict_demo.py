from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person={'name':'Vansh', 'age':'22'}

print(new_person)