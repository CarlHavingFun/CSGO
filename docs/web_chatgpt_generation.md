# Web ChatGPT Generation Workflow

Use this workflow for the next image pass.

## Browser Isolation

The user has another image-generation project running in a browser. Do not disturb it.

Required behavior:

- Open a new browser window or a new ChatGPT tab.
- If using browser automation, create a fresh tab and verify it is not the currently active generation page.
- Do not navigate, refresh, close, or type into an existing ChatGPT page unless the user explicitly points to it.

## Per-Character Inputs

Before generating, gather:

- Original player reference image.
- Current inspired name.
- Team jersey period.
- 2-4 recognizable anchors.
- Face-safety note.

Store the original reference image path in `data/visual_reference_requirements.csv`.

## Prompt Template

```text
Create a 9:16 vertical photorealistic CS2 esports drama character still.

Use the attached original player image only as a loose archetype reference for recognizable non-clone traits:
- body type:
- hair:
- glasses/facial hair:
- age impression:
- posture/expression:

Create an original fictional character named <InspiredName>.
The audience should be able to infer the archetype from silhouette, hair, glasses, body type, expression, and esports role aura, but the face must not be a clone of the real person.

Wardrobe: authentic <Team> <Year> esports jersey, including real colors, logo placement, and sponsor layout for internal concept testing.
Scene: CS2 tournament gaming booth, monitor glow, headset, broadcast arena background.
Style: photorealistic esports drama still, cinematic sports documentary, realistic skin texture.
Composition: waist-up portrait, centered slightly right, enough top and side room for CapCut motion crop.

Avoid exact real-player likeness, celebrity face cloning, generic esports model face, anime, cartoon, wax skin, plastic face, unreadable text, watermarks, extra fingers, duplicated headset, 3D game render.
```

## ZywOo / Zyvo Locked Prompt Notes

Zyvo must not be thin or generic.

Use these anchors:

- Rounder/chubbier body and face impression.
- Glasses.
- Curly or fluffy curly hair.
- Gentle, quiet French AWP superstar energy.
- Soft but focused expression.

The output fails if it looks like the current generic thin sample in `assets/generated/Vitality/Zyvo/current.png`.

## Acceptance Check

For each final image:

- Put original reference and generated image side by side.
- Confirm the archetype is readable in 3 seconds.
- Confirm the face is not a direct clone.
- Confirm body/hair/accessory anchors survived.
- Confirm 9:16 vertical composition works for short-drama editing.
