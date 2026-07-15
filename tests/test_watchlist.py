"""
tests/test_watchlist.py — CineLog

Tests for the watchlist service. Follows the same fixture and assertion
patterns established in tests/test_collection.py.
"""

import pytest
from app import create_app, db
from models import User, Film, WatchlistEntry
from services.collection_service import FilmNotFoundError
from services.watchlist_service import add_to_watchlist, get_watchlist


@pytest.fixture
def app():
    """Create an isolated test app with an in-memory database."""
    app = create_app(config={
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def sample_user(app):
    """A user to use in tests."""
    with app.app_context():
        user = User(username="testuser", email="test@example.com")
        db.session.add(user)
        db.session.commit()
        return user.id


@pytest.fixture
def sample_film(app):
    """A film to use in tests."""
    with app.app_context():
        film = Film(title="Paddington 2", year=2017, genre="Comedy")
        db.session.add(film)
        db.session.commit()
        return film.id


@pytest.fixture
def client(app):
    """A test client for hitting the watchlist routes over HTTP."""
    return app.test_client()


# ── Nonexistent film ─────────────────────────────────────────────────────────

def test_add_to_watchlist_nonexistent_film_raises(app, sample_user):
    """
    Adding a film_id that doesn't exist in the database should raise
    FilmNotFoundError, not a database integrity error.
    """
    with app.app_context():
        fake_film_id = "00000000-0000-0000-0000-000000000000"

        with pytest.raises(FilmNotFoundError):
            add_to_watchlist(user_id=sample_user, film_id=fake_film_id)


# ── get_watchlist sort order ─────────────────────────────────────────────────

def test_get_watchlist_returns_newest_first(app, sample_user):
    """
    get_watchlist() should return films sorted by date_added descending
    (most recently added first).
    """
    with app.app_context():
        from datetime import datetime, timezone, timedelta

        film_a = Film(title="Alien", year=1979, genre="Horror")
        film_b = Film(title="Blade Runner", year=1982, genre="Sci-Fi")
        db.session.add_all([film_a, film_b])
        db.session.commit()

        earlier = datetime.now(timezone.utc) - timedelta(days=5)
        later = datetime.now(timezone.utc)

        entry_a = WatchlistEntry(user_id=sample_user, film_id=film_a.id, date_added=earlier)
        entry_b = WatchlistEntry(user_id=sample_user, film_id=film_b.id, date_added=later)
        db.session.add_all([entry_a, entry_b])
        db.session.commit()

        watchlist = get_watchlist(sample_user)
        titles = [f["title"] for f in watchlist]

        # Blade Runner was added later, so it should come first
        assert titles[0] == "Blade Runner"
        assert titles[1] == "Alien"


# ── Route-level error handling ───────────────────────────────────────────────

def test_add_film_route_duplicate_returns_409(client, sample_user, sample_film):
    """
    POST /watchlist/<user_id>/add should return a clean 409 (not a raw 500)
    when the film is already on the user's watchlist.
    """
    client.post(f"/watchlist/{sample_user}/add", json={"film_id": sample_film})

    response = client.post(f"/watchlist/{sample_user}/add", json={"film_id": sample_film})

    assert response.status_code == 409
    assert "error" in response.get_json()


def test_add_film_route_nonexistent_film_returns_404(client, sample_user):
    """
    POST /watchlist/<user_id>/add should return a clean 404 (not a raw 500)
    when film_id doesn't exist.
    """
    fake_film_id = "00000000-0000-0000-0000-000000000000"

    response = client.post(f"/watchlist/{sample_user}/add", json={"film_id": fake_film_id})

    assert response.status_code == 404
    assert "error" in response.get_json()
