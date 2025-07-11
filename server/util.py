import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        # No .lower() — Keep exact match as per columns.json
        loc_index = __data_columns.index(location)
    except ValueError:
        loc_index = -1  # Location not found

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    # Load columns.json
    try:
        with open("artifacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # Skipping first 3 columns (sqft, bath, bhk)
    except Exception as e:
        raise RuntimeError(f"Error loading columns.json: {e}")

    # Load model
    try:
        with open("artifacts/banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    except Exception as e:
        raise RuntimeError(f"Error loading model pickle file: {e}")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


# For testing only (optional)
if __name__ == '__main__':
    load_saved_artifacts()
    print("Available Locations:", get_location_names())
    print("Test Prediction:", get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
