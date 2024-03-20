from aocd import get_data

function_registry = {}

def register(day, year, part, split_text=False):
    def inner(f):
        if f"{day}_{year}_{part}" in function_registry:
            raise Exception(f"{day}_{year}_{part} already registered")
        function_registry[f"{day}_{year}_{part}"] = (f, split_text)
        return f
    return inner

def run_method(day, year, part):
    func_details = function_registry[f"{day}_{year}_{part}"]

    data = get_data(day=day, year=year)

    if func_details[1]:
        data = data.split("\n")

    return func_details[0](data)