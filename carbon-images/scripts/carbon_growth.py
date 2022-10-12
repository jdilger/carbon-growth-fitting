import numpy as np
from typing import Any, Tuple


def chapman_richards(age: float, b0: float, b1: float, b2: float):
    return (b0 * (1 - np.exp(-b1 * age))) ** b2


def growth_function_by_hectares(
    growth_func, x: float, parameters: Tuple[float], hectares: float
):
    return growth_func(x, *parameters) * hectares


chapman_richards_growth_params = {
    "natural_asia_humid": {
        "name": "Natural Asia Humid",
        "parameters": (22.20201292, 0.08282659, 1.65756327),
    }
}


def get_growth_params(params, key):
    return params[key]


# func itsself
def get_growth_hectares(values, hectares, age):
    res = growth_function_by_hectares(
        chapman_richards, age, values["parameters"], hect
    )
    return (values["name"], res)


if __name__ == "__main__":
    k = "natural_asia_humid"
    hect = 100
    age = 10
    v = get_growth_params(chapman_richards_growth_params, "natural_asia_humid")
    print(get_growth_hectares(v, hect, age))
