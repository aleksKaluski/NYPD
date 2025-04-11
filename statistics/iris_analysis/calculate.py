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
        print(value)
        result[key] = {
            "mean": count_mean(value),
            "median": count_median(value),
            "sd": count_sd(value)}
    print(result)
    return result

stat_data = {
    "sepal_length": [5.1, 3.3],
    "sepal_width": [3.5, 5.5],
    "petal_length": [1.4, 2.3],
    "petal_width": [0.2, 0.9]
}

stats_for_all(stat_data)

