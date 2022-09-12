#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    results = []

    for i in range(list_length):
        div = None
        try:
            if type(my_list_1[i]) not in [int, float]:
                raise TypeError
            if type(my_list_2[i]) not in [int, float]:
                raise TypeError

            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            results.append(div if div is not None else 0)

    return results
