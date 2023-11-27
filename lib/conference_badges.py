def badge_maker(name):
    message = f"Hello, my name is {name}."
    return message

def batch_badge_creator(names):
    messages = []
    for name in names:
        message = f"Hello, my name is {name}."
        messages.append(message)

    return messages

def assign_rooms(names):
    messages = []
    for name in names:
          message = f"Hello, {name}! You'll be assigned to room {names.index(name)+1}!"
          messages.append(message)
    return messages

def printer(names):
    badges =batch_badge_creator(names)
    rooms =assign_rooms(names)
    for badge in badges:
         print(badge)
    for room in rooms:
        print(room)
    
    return None
