def split_every(string, count):
    while string:
        yield string[:count]
        string = string[count:]

def split_at_value(container, target_value, value_function, starting_value=0):

    curr_val = starting_value
    
    current_set = []
    for obj in container:
        obj_value = value_function(obj)
        if curr_val + obj_value > target_value:
            yield current_set
            current_set = []
            curr_val = starting_value

        curr_val = curr_val + obj_value 
        current_set.append(obj)

    yield current_set
