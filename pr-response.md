# PR Response Doc — CineLog Watchlist Feature

## AI Usage

<!-- Fill in at the end — how you used AI tools during this project -->

One of the first things we are told to do is to ask Claude for help in navigating the codebase. This included a summary of models.py, a function explanation of add_to_collection(), and asking about the test structure found in the test_collection.py tests.

## Comment 1 — Rename

Rename save_to_watchlist() to add_to_watchlist() in services/watchlist_service.py and update all call sites (there is one in routes/watchlist/watchlist.py). Use your editor's find-all-references or a project-wide search to confirm you haven't missed any.

**What I did:** I used VS Code's "Rename Symbol" feature to change `save_to_watchlist()` to `add_to_watchlist()`.
**How I verified:** After changing the name, I then used "Find All References" to make sure that the number of calls to the new method name was the same as the old method. I also double checked with Claude just to be safe, since it's my first time using the feature.

## Comment 2 — Deduplication

Add deduplication logic to add_to_watchlist() in services/watchlist_service.py. Look at how add_to_collection() in services/collection_service.py handles this — follow the same pattern.

**What I did:** Added a conditional in the add_to_watchlist() method found in the watchlist_service.py file that checks if the film is one the User has already added to their watchlist.
**How I verified:** I followed the same pattern as add_to_collection() does, including adding a custom Exception class to the file. I did double check using Claude to see if the code works the same.

## Comment 3 — Missing test

Create a new file tests/test_watchlist.py. Read tests/test_collection.py and find test_add_to_collection_nonexistent_film_raises — write the equivalent test for add_to_watchlist() following the same fixture and assertion structure.

**What I did:** Created a test file for watchlist, and wrote a test named `test_add_to_watchlist_nonexistent_film_raises` which was similar to `test_add_to_collection_nonexistent_film_raises` in the test_collection.py file.
**How I verified:** I ran the test suite, first by only running the test that I just added. When that passed, I ran the whole test suite to make sure nothing broke.

## Comment 4 — Default visibility

**My position:**
**Reasoning:**
**Tradeoff acknowledged:**

## Comment 5 — Sort order

**My position:**
**Reasoning:**
**Engagement with reviewer's point:**

## Comment 6 — Rebase

**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description

<!-- Written at the end — feature overview, design decisions, manual testing steps -->
