# AI Usage Report

This document describes how AI tooling was used during the development of the Lagovia Train Tracker, as required by the challenge brief.

---

## Tools Used

| Tool    | Purpose                                  |
|---------|------------------------------------------|
| ChatGPT | Generating boilerplate code and scaffolding |

---

## What I Used AI For

AI assistance was limited to **boilerplate and scaffolding** — the repetitive, structural parts of the codebase that do not require domain-specific thinking:

- Initial FastAPI project layout (`main.py` entry point, router setup)
- React component file structure and `useState` / `useEffect` skeleton
- `requirements.txt` and `package.json` starting points
- Vite config and basic `App.jsx` shell

---

## What I Wrote Myself

All logic and decisions that required understanding the problem were written without AI assistance:

- The departure filtering logic (UTC time comparison, 15-minute window)
- Station substring matching and case-insensitive search
- The in-memory station cache design and its trade-offs
- iRail API integration (`irail.py`): understanding the response shape, extracting the right fields, stripping the `BE.NMBS.` prefix from train numbers
- Error handling strategy (input validation, upstream failure responses)
- The response schema design and documentation
- Frontend grouping of departures by station

---

## What I Rewrote or Rejected

- The initial AI-generated fetch logic used `requests` (synchronous). I replaced it with `httpx` to stay consistent with FastAPI's async model.
- The AI-generated component did not group results by station. I restructured `DeparturesTable.jsx` to group rows by station name, which is a stated requirement.
- Some generated error handling was too generic (bare `except Exception`). I replaced it with specific error types and meaningful response messages.

---

## Chat Links

No shareable public chat links are available for this project. Conversations were conducted in a private ChatGPT session.

---

## Summary

AI was a productivity tool for the parts of the project that don't require engineering judgment — file structure, imports, and initial shells. Every decision about architecture, data flow, filtering logic, and API design was made independently. I am able to explain and modify any part of the codebase.
