import os


def test_model_file_exists():
    """Check that the trained model artifact is present."""
    assert os.path.exists("bed_availability_model.pkl")


def test_model_file_not_empty():
    """Check that the model artifact is not empty."""
    assert os.path.getsize("bed_availability_model.pkl") > 0
