import os


def check_project():
    model_path = "bed_availability_model.pkl"

    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found")

    model_size = os.path.getsize(model_path)

    if model_size == 0:
        raise ValueError("Model file is empty")

    return {
        "status": "success",
        "model": model_path,
        "model_size": model_size
    }


if __name__ == "__main__":
    result = check_project()
    print("Project build check successful!")
    print(result)
