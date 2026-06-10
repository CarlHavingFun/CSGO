# Next AI Handoff

## What Was Done

Initialized a CS2 character asset repository for `D:\05_漫剧` and prepared the first structured data pass.

Created:

- `data/players.csv` with 98 HLTV Top 20 listed players.
- `data/team_periods.csv` with 154 team-period records.
- `data/visual_reference_requirements.csv` for original-player reference images and similarity targets.
- `prompts/character_prompts.md` with per-character prompt drafts.
- `assets/generated/` with six early built-in `image_gen` samples.
- `docs/sources.md` and `docs/roster_gaps.md`.

## User Feedback That Must Drive The Next Pass

The first images failed the intended creative direction:

- Faces are too homogeneous.
- Characters do not clearly map back to the original player archetypes.
- The generation process did not use original player visual references.
- ZywOo/Zyvo specifically must be rounder/chubbier, wear glasses, and have curly hair.

Do not treat the six current images as final quality. They are visual drafts to show what not to continue.

## New Required Direction

Use Web ChatGPT image generation, not built-in `image_gen`, for final character images.

Browser safety requirement:

- Prefer using one fresh ChatGPT tab in the current in-app browser session.
- Do not reuse or disturb any other running ChatGPT/image-generation page the user has open.
- Keep each generation conversation clearly named or separated if the UI supports it.

Image-generation requirement:

- Each character needs one original player reference image first.
- Place references at `references/originals/<Team>/<real_nickname>.jpg`.
- Generate the fictional character from the reference-aware prompt.
- Compare original vs generated side by side.
- Pass condition: the audience can infer the archetype from body type, hair, glasses, age impression, facial hair, posture, expression, and role aura.
- Safety condition: do not clone the exact real face or claim it is the real player.

## Immediate Next Tasks

1. Finish the Web ChatGPT login/MFA flow in an isolated tab, then continue the same session without reopening.
2. Collect original player reference images for the 20 sample-priority characters first:
   `ZywOo`, `Aleksib`, `donk`, `m0NESY`, `FalleN`, `XANTARES`, `arT`, `torzsi`, `bLitz`, `Snax`, `Jame`, `HooXi`, `lauNX`, `SunPayus`, `frozen`, `npl`, `AW`, `biguzera`, `insani`, `dgt`, `YEKINDAR` (and their 20th mapped sample, if not already added).
3. Start with ZywOo/Zyvo and regenerate only that one until the visual anchor passes:
   chubbier/rounder, glasses, curly hair, gentle silent French AWP aura.
3. Save side-by-side comparison in `assets/comparisons/Vitality/Zyvo/current_comparison.png`.
4. Save accepted generation in `assets/generated/Vitality/Zyvo/current.png`, replacing the deprecated draft only after acceptance.
5. Update `data/visual_reference_requirements.csv` comparison status from `missing_original_reference` to `passed` or `needs_revision`.

## Current Run Result (2026-06-10)

- New browser tab for `https://chatgpt.com/` was previously used for a focused Zyvo rebuild and produced `assets/generated/Vitality/Zyvo/current.png`.
- `data/players.csv` was updated to `generated_current` for Zyvo.
- In this continuation check, the in-app browser tab shows the ChatGPT onboarding/login flow with only auth-entry buttons (`使用 Google 账户继续`, `使用 Apple 账户继续`, `使用电话号码继续`, `继续`) and no visible composer/contenteditable field.
- No generation can continue until that tab is in a logged-in chat state.
- Note: avoid clicking the microphone/voice action (`启动语音功能`)—it can capture UI focus and break deterministic submit. Use direct composer submission (Send button first, Enter as fallback).

## Immediate Next Operational Step

- Authenticate the current `iab` browser session once in this tab (keep it open), then resume from `prompts/web_batch_queue.md` at `Alek-C` (Aleksib) and continue downward.
- Queue head remains `Alek-C`, followed by `Donko`, `Moness`, `Falleno`, and the rest of the sample-priority list.

## Do Not Do

- Do not continue generating generic esports faces.
- Do not use built-in `image_gen` for final character images.
- Do not overwrite existing user browser work.
- Do not fabricate missing fifth players for MOUZ/FaZe without a checked source.
- Do not treat real team jersey output as public-safe; it is still trademark/sponsor-risky.
