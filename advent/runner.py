from aocd import get_data

function_registry = {}

def register(day, year, part):
    def inner(f):
        if f"{day}_{year}_{part}" in function_registry:
            raise Exception(f"{day}_{year}_{part} already registered")
        function_registry[f"{day}_{year}_{part}"] = f
        return f
    return inner

def run_method(day, year, part):
    func = function_registry[f"{day}_{year}_{part}"]

    data = get_data(day=day, year=year)

    return func(data)