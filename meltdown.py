def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - power that corresponds to a 100% efficiency.
    :return: str - one of ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:

    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60%, but still 30% or more,
    4. black ->  less than 30% efficient.

    The percentage value is calculated as
    (generated power/ theoretical max power)*100
    where generated power = voltage * current
    """

    percentage = ((voltage*current)/theoretical_max_power)*100

    if percentage >= 80:
        return 'green'
    elif percentage < 80 and percentage >= 60:
        return 'orange'
    elif percentage < 60 and percentage >= 30:
        return 'red'
    else:
        return 'black'

# print(reactor_efficiency(10,799,10000))


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return status code for the reactor.

    :param temperature: int or float - value of the temperature in kelvin.
    :param neutrons_produced_per_second: int or float - neutron flux.
    :param threshold: int or float - threshold for category.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons per second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons per second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons per second` is not in the above-stated ranges
    """

    if (temperature * neutrons_produced_per_second) < (threshold*0.9):
        return 'LOW'
    elif ((temperature * neutrons_produced_per_second) >= (threshold*0.9)) and ((temperature * neutrons_produced_per_second) <= (threshold*1.1)):
        return 'NORMAL'
    else: 
        return 'DANGER'

# print(fail_safe(10, 1101, 10000))