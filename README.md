# CS2 Character Asset Library

This repo is the working asset library for a CS2/CSGO-inspired short-drama character pipeline.

## Current State

- Git repo initialized in `D:\05_漫剧`.
- Roster scope is HLTV Top 20 on 2026-06-01.
- `data/players.csv` covers 98 listed players from the snapshot. MOUZ and FaZe show only four players on the ranking page; no fifth player was fabricated.
- `data/team_periods.csv` contains 154 current/history team-period rows.
- `prompts/character_prompts.md` contains reusable prompt drafts for all listed characters.
- Six early sample images were generated for early queue samples (Alek-C/Donk/Moness/Falleno/Xantor/BlitZed) and are pending final-side-by-side acceptance.

## Important Correction

The first generated samples are not good enough for final use. Faces are too homogeneous, and viewers cannot recognize which real player archetype each fictional role maps to.

Treat `assets/generated/` as deprecated visual drafts only. Do not continue that direction for final character art.

The corrected pipeline is:

1. Put one original player reference image per character in `references/originals/<Team>/<real_nickname>.jpg`.
2. Extract recognizable non-facial-clone anchors: body type, glasses, hair, age impression, facial hair, posture, expression, and role aura.
3. Generate with Web ChatGPT image generation in a new browser window/tab, not the built-in `image_gen` tool.
4. Save output under `assets/generated/<Team>/<InspiredName>/current.png` only after side-by-side comparison passes.
5. Record comparison status in `data/visual_reference_requirements.csv`.

## Current Web Rebuild Status (June 2026)

- Current in-app browser check still reaches the ChatGPT onboarding/login flow (`开始使用 | ChatGPT`) with no visible chat composer.
- Re-authentication/login is needed in this same tab before queue generation can continue.
- Current queue head is Alek-C (Aleksib), then Donko, Moness, and the rest of the team-priority samples.

Next manual step in the same browser session (if you are logged in):

- Open `prompts/web_batch_queue.md` and run items from top to bottom.

## Example: ZywOo / Zyvo

The previous Zyvo image is rejected because it is too generic and too thin.

New Zyvo requirements:

- Rounder/chubbier body and face impression.
- Glasses.
- Curly or fluffy curly hair.
- Gentle, silent French AWP superstar aura.
- Must remain an original fictional face, not a cloned portrait.

## Key Files

- `data/players.csv` - main character table with generation channel and visual anchors.
- `data/team_periods.csv` - current and historical team jersey periods.
- `data/visual_reference_requirements.csv` - original reference image checklist and similarity targets.
- `prompts/character_prompts.md` - prompt base, now requiring reference-aware generation.
- `docs/next_ai_handoff.md` - detailed handoff for the next AI session.
- `docs/web_chatgpt_generation.md` - how to use Web ChatGPT without affecting existing browser work.
- `docs/sources.md` - sources and rights notes.

## Verification

Run:

```powershell
python scripts\validate_assets.py
```

The validator checks roster coverage, uniqueness, prompt requirements, sample-priority count, and the visual-reference schema.
