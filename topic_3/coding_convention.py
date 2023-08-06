import json


def add_student_record(
    file_path: str, student_id: str, name: str, age: int, grade: str
) -> None:
    """
    Add a new student record to the records and save it to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        student_id (str): The student ID.
        name (str): The name of the student.
        age (int): The age of the student.
        grade (str): The grade of the student.
    """
    try:
        with open(file_path, "r") as file:
            records = json.load(file)
    except FileNotFoundError:
        records = []

    new_record = {"student_id": student_id, "name": name, "age": age, "grade": grade}
    records.append(new_record)

    with open(file_path, "w") as file:
        json.dump(records, file)


def search_student(file_path: str, key: str, value: str) -> dict:
    """
    Search for a student in the records by student_id or name.

    Args:
        file_path (str): The path to the JSON file.
        key (str): The search key (either 'student_id' or 'name').
        value (str): The value to search for.

    Returns:
        dict: A dictionary containing the student's age and grade, if found. None otherwise.
    """
    try:
        with open(file_path, "r") as file:
            records = json.load(file)
    except FileNotFoundError:
        return None

    for record in records:
        if record.get(key) == value:
            return {"age": record["age"], "grade": record["grade"]}

    return None


if __name__ == "__main__":
    file_path = "student_records.json"
    add_student_record(file_path, "1232", "Aavash Bhattarai ", 30, "A")
    add_student_record(file_path, "6211", "Samyam Aryal", 17, "B")

    student_id = "12345"
    search_result = search_student(file_path, "student_id", student_id)
    if search_result:
        print(
            f"Student with ID {student_id} found. Age: {search_result['age']}, Grade: {search_result['grade']}"
        )
    else:
        print(f"Student with ID {student_id} not found.")