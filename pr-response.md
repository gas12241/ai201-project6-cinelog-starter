# PR Response Doc — CineLog Watchlist Feature

## AI Usage

<!-- Fill in at the end — how you used AI tools during this project -->

One of the first things we are told to do is to ask Claude for help in navigating the codebase. This included a summary of models.py, a function explanation of add_to_collection(), and asking about the test structure found in the test_collection.py tests.

## Comment 1 — Rename

save_to_watchlist() should follow the project's naming convention. Compare with add_to_collection() — the pattern here is verb_to_noun. Please rename to add_to_watchlist() and update all call sites.

**What I did:** I used VS Code's "Rename Symbol" feature to change `save_to_watchlist()` to `add_to_watchlist()`.
**How I verified:** After changing the name, I then used "Find All References" to make sure that the number of calls to the new method name was the same as the old method. I also double checked with Claude just to be safe, since it's my first time using the feature.

## Comment 2 — Deduplication

**What I did:**
**How I verified:**

## Comment 3 — Missing test

**What I did:**
**How I verified:**

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
