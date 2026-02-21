# Royal Match Clan Tracker

## Project
Track clan member activity via screenshots, detect inactive players.

## Pipeline
```
Screenshots → OCR → SQLite → Python → index.html → GitHub Pages
```

## OCR Rules

### Game data invariants
- **Level never decreases** between snapshots. If OCR shows a decrease — it's a misread, re-examine the screenshot
- Help counter resets weekly (official: "Helps are counted weekly and reset at the end of every week"). Shows how many lives a player sent to teammates this week. Cannot compare across snapshots unless they're within the same week

### Known OCR pitfalls
- **Animated/decorative fonts**: some player names use stylized fonts where digits/letters are hard to distinguish (e.g. `2` looking like `z`). Always flag uncertain readings to the user
- **Partially visible rows**: screenshots cut off top/bottom entries. Don't guess — ask the user to clarify
- **Duplicate names**: multiple players can have the same name (e.g. "123", "Alex"). Match between snapshots by name + approximate level, not name alone
- **Cyrillic/Latin ambiguity**: game allows mixed scripts in names, `a`/`а`, `c`/`с`, `e`/`е` can be either

## SQLite Schema
- `snapshots(id, date)`
- `members(id, snapshot_id, position, name, help, level)`

## Inactivity Definition
A member is inactive only when BOTH conditions are true:
- Level delta = 0 (no level progression)
- Help = 0 in the latest snapshot (no help given at all)

If a member has 0 level delta but non-zero help — they are NOT inactive.

## File Structure
```
screenshots/          # .gitignored, local only
  YYYY-MM-DD/         # one folder per snapshot date
clan.db               # .gitignored
seed_data.py          # one-time initial data seed
```
