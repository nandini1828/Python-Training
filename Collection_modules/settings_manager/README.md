# Settings Manager

## What this project does
This project uses `ChainMap` to combine multiple configuration layers into one effective settings view.

## Key concepts used
- `ChainMap` looks through several dictionaries in order.
- The first matching key wins, so user settings override environment settings, which override defaults.

## Main features
- View the effective settings after combining all layers.
- Update a setting in the user configuration.
- Remove a user setting.
- View each configuration level individually.
- Reset user settings.

## Why this is useful
ChainMap is helpful when applications need default values, environment-specific overrides, and personalized user preferences all at once.
