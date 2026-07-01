# Recent Files Manager

## What this project does
This project uses `OrderedDict` to keep a list of recently opened files in a fixed order.

## Key concepts used
- `OrderedDict` preserves insertion order.
- `move_to_end()` moves a file to the newest position when it is opened again.
- `popitem(last=False)` removes the oldest file when the history grows past 10 items.

## Main features
- Open a file and add it to the recent history.
- View the recent file list.
- Remove a file from the history.
- Clear the entire history.

## Why this is useful
This pattern is useful in editors and file managers that need to remember recent activity while keeping the history manageable.
