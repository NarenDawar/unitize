conversion_history = []

def add_to_history(conversion):
    conversion_history.append(conversion)

def get_history():
    return conversion_history

def clear_history():
    conversion_history.clear()
