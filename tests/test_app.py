from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_remove_participant_from_activity():
    original_participants = activities["Chess Club"]["participants"].copy()

    try:
        response = client.delete(
            "/activities/Chess%20Club/participants/michael%40mergington.edu"
        )

        assert response.status_code == 200
        assert "michael@mergington.edu" not in activities["Chess Club"]["participants"]
        assert response.json()["message"] == "Removed michael@mergington.edu from Chess Club"
    finally:
        activities["Chess Club"]["participants"] = original_participants
