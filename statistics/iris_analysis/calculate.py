import statistics as st

def count_mean(data: list) -> float:
    data = sorted(data)
    return  round(st.mean(data), 3)

def count_median(data: list) -> float:
    data = sorted(data)
    return  round(st.median(data), 3)

def count_sd(data: list)-> float:
    data = sorted(data)
    return round(st.stdev(data), 3)

def stats_for_all(dictionary: dict) -> dict:
    result = {"sepal_length": [],
              "sepal_width": [],
              "petal_length": [],
              "petal_width": []}

    for key, value in dictionary.items():
        result[key] = {
            'feature': key,
            "mean": count_mean(value),
            "median": count_median(value),
            "sd": count_sd(value)}
    print(result)
    return result
