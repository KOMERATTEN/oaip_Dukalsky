def calc_avg(numbers: list) -> float:
  
    if not numbers:
        return 0.0
        
    return sum(numbers) / len(numbers)


def fmt_fio(parts: list[str], capitalize: bool = True) -> str:
 
    
    fio = " ".join(parts)
    
    if capitalize:
        return fio.title()
        
    return fio


def filter_scores(data_dict: dict[str, int | float], min_value: int | float) -> dict[str, int | float]:
   
    result = {}
    
    for key, value in data_dict.items():
        if value >= min_value:
            result[key] = value
            
    return result

if __name__ == "__main__":
    print("\n  Функция 1 ")
    numbers_list = [10, 20, 30, 40]
    average = calc_avg(numbers_list)
    print(f"Среднее значение {numbers_list}: {average}")
    print(f"Среднее значение пустого списка: {calc_avg([])}")
    
    print("\n  Функция 2 ")
    fio_parts = ["петров", "иван", "сергеевич"]
    formatted_fio1 = fmt_fio(fio_parts)
    print(f"ФИО с капитализацией: {formatted_fio1}")
    
    formatted_fio2 = fmt_fio(["сидорова", "анна", "валерьевна"], capitalize=False)
    print(f"ФИО без капитализации: {formatted_fio2}")
    
    print("\n Функция 3 ")
    scores = {"math": 95, "history": 78, "english": 88, "art": 92}
    filtered_scores = filter_scores(scores, 90)
    print(f"Исходные оценки: {scores}")
    print(f"Оценки >= 90: {filtered_scores}")