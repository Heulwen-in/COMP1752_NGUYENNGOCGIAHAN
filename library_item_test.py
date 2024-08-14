from library_item import LibraryItem
import pytest

def test_default_rating():
    key = LibraryItem("Tom and Jerry", "Fred Quimby", 0)
    assert key.name == "Tom and Jerry"
    assert key.director == "Fred Quimby"
    assert key.rating == 0
    assert key.play_count == 0
    
def test_video_details():
    key = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
    assert key.name == "Tom and Jerry"
    assert key.director == "Fred Quimby"
    assert key.rating == 4
    assert key.play_count == 0

def test_info():
    key = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
    assert key.info() == "Tom and Jerry - Fred Quimby (4) - Played 0 times"
    
def test_play_count():
    key = LibraryItem("Tom and Jerry", "Fred Quimby", 4)
    assert key.play_count == 0
    key.play()
    assert key.play_count == 1
    key.play()
    assert key.play_count == 2
    assert key.info() == "Tom and Jerry - Fred Quimby (4) - Played 2 times"
    
def test_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem("Tom and Jerry", "Fred Quimby", -1)
        
def test_invalid_rating_type():
    with pytest.raises(TypeError):
        LibraryItem("Tom and Jerry", "Fred Quimby", "four")