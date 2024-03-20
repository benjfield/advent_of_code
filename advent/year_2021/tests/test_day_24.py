from advent.year_2021.day_24 import *

def monad_reverse():
    for divisor in range(1, 27):
        for additive_1 in range(-26, 27):
            for additive_2 in range(-26, 27):
                for input in range(1, 10):
                    final_z = {}
                    for initial_z in range(1000):
                        z = monad(initial_z, input, divisor, additive_1, additive_2)
                        if z in final_z:
                            final_z[z].append(initial_z)
                        else:
                            final_z[z] = [initial_z]

                    for key in final_z.keys():
                        final_z[key].sort()
                    
                        initial_z = monad_reverse(key, input, divisor, additive_1, additive_2)

                        initial_z = [x for x in initial_z if x < 1000 and x >= 0]

                        initial_z.sort()

                        test = (initial_z == final_z[key])

                        if not test:
                            print(key)
                            print(monad(key, input, divisor, additive_1, additive_2))
                            print(input, divisor, additive_1, additive_2)

                        assert initial_z == final_z[key]