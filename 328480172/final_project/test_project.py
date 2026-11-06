from project import get_astronomy_title, get_mars_rover_status, get_live_iss_coords

def test_get_astronomy_title():
    assert isinstance(get_astronomy_title(), str)

def test_get_mars_rover_status():
    assert "Active" in get_mars_rover_status()

def test_get_live_iss_coords():
    assert "Lat" in get_live_iss_coords()
