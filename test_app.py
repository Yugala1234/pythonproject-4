from app import get_weather

def test_get_weather():
    result = get_weather("London")
    assert "London" in result
