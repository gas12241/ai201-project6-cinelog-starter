# PR Response Doc — CineLog Watchlist Feature

## AI Usage

<!-- Fill in at the end — how you used AI tools during this project -->

One of the first things we are told to do is to ask Claude for help in navigating the codebase. This included a summary of models.py, a function explanation of add_to_collection(), and asking about the test structure found in the test_collection.py tests.

I used Claude to write the test_watchlist.py file as well. It was pretty similar to test_collection, so with that context, it returned a working test.

One thing that I've seen people do but never done myself (mostly because I've seen it done with a keyboard shortcut), is change the name of one symbol, and have it affect all references of it. I asked Claude to tell me how you can do that in VS Code, which helped with the first comment.

Talking about comments, for the first 3 comments, I did ask Claude to check if I was missing anything after implementing it myself. I used it as a way of making sure I wasn't missing anything.

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

NOTE: At the top of the HW assignment, it makes it sound like we won't have to write code for the decision comments. Under Milestone 3, it says: "Comments 4 and 5 aren't code problems — they're design conversations. Both require written arguments, not just code." This makes it sound like I have to do both, so I made a decision AND changed code to make public = False by default.

I notice watchlists default to public=True. We don't have a documented decision on default visibility for user lists. Before I can approve this, I need you to add a note to your PR description explaining your reasoning. I want to make sure we're being intentional here, not just inheriting a default.

**My position:** I think watchlists should default to NOT being public (public = False).
**Reasoning:** I think it's a better bet to make the default with user privacy in mind. An example that came to mind when thinking of this is when Steam changed everything so that users had to opt into sharing things on their profile (I believe this was in response to Facebook leaking data). I think this is nice because if you're curious about the watchlists of friends, you'll end up asking them about it and bringing up the choice of whether or not they want to make it public (which will also remind the user to make theirs public as well if they so choose).In this way, people who are social will end up seeing their friends film watchlist, while those who could care less, don't have their information out in the open.

One little caveat I would add is to make it painstakingly clear to the user that the toggle for private vs public watchlists exist. Relying on word of mouth solely would ba a grave mistake.

**Tradeoff acknowledged:** Some people might not even think to make their watchlist public, and in that case, it could end up not bringing the community together in the way that we would want. That being said, I do believe User Privacy should be the biggest priority between the two.

## Comment 5 — Sort order

I'd prefer watchlists to default to "date added" order rather than alphabetical. Most users want to see what they added recently. I'm open to discussion if you see it differently — but let's make a decision and document it.

**My position:** Unless I am reading this incorrectly, I agree that watchlists should be oredered by "date added" with the most recent additions being the first ones to show up.
**Reasoning:** When I think about movies that I want to watch, if I have been reminded about it and add it to my watchlist, I usually have the itch to watch them sooner rather than later. Because of this, I think it makes the most sense to return the movies that were most recently added, first. I also think that if you return movies in order alphabetically, if you have many movies in your recommended, it might cause the watchlist to have the same or similar returnings in order over and over again if you don't add any movies that break the top X movies alphabetically.

I also want to address that you could argue this is more of a personal take rather than one based on how the code works and what the project might stand for. The reviewers point for sort order was based on pesonal opinion, so I think it would be fair to use my personal opinion as well.

For reasons against this sort of sort, it would be that not everyone enjoys seeing movies added most recently. I think the best case scenario would be to have something to toggle between multiple sorting styles, but I'm not sure how reasonable that is to do.

The other reason you wouldn't want the most recent movies first, is that people would forget about the movies you've added a while ago, and they would continue to sink lower down the list.

**Engagement with reviewer's point:** I agree wholeheartedly with the reviewer. If I get reminded of a movie, and I add it to my watchlist, I would like to see it to get it out of the watchlist. Waiting too long will cause me to lose interest in the film.

## Comment 6 — Rebase

**What conflicted:**
**How I resolved it:**
**How I verified no conflict remains:**

## PR Description

<!-- Written at the end — feature overview, design decisions, manual testing steps -->
