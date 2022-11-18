def refine_input(prompt='', type_=None, min_=None, max_=None, range_=None):
    """ Used for sanitizing input provided by the user
    """
    str_not_valid_input = "That is not a valid input. "
    while True:
        if min_ is not None and max_ is not None and max_ < min_:
            raise ValueError("Lower bound must be less than or equal to upper bound.")
        while True:
            variable = input(prompt)
            if type_ is not None:
                try:
                    variable = type_(variable)
                except ValueError:
                    print(str_not_valid_input + "Value has to be {}.".format(type_.__name__))
                    continue
            if max_ is not None and variable > max_:
                print(str_not_valid_input + "Value must be less than or equal to {}.".format(max_))
            elif min_ is not None and variable < min_:
                print(str_not_valid_input + "Value must be greater than or equal to {}".format(min_))
            elif range_ is not None and variable not in range_:
                if isinstance(range_, range):
                    str_must_be_between = "Value must be between {} and {}.".format(range_.start, range_.stop)
                    print(str_must_be_between)
                else:
                    str_var_must_be = "Value must be {}."
                    if len(range_) == 1:
                        print(str_var_must_be.format(*range_))
                    else:
                        expected = " or ".join((", ".join(str(x) for x in range_[:-1]), str(range_[-1])))
                        print(str_var_must_be.format(expected))
            else:
                return variable


def str_rjust(value, size=2, padding_char='0') -> str:
    """ Used for cleaning strings for file naming, etc.
    """
    value_str = str(value)
    if len(value_str) > 2:
        short = value_str[-2:]
    else:
        short = value_str

    return short.rjust(size, padding_char)
