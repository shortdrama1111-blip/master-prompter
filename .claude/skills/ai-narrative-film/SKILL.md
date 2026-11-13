---
name: ai-narrative-film
description: Use when building a multi-scene narrative AI film or ad with locked characters across scenes — writing shot prompts, keeping faces/wardrobe/props consistent between generations, locking environments and colour grade, choosing shot lengths, and diagnosing failed generations (duplicated characters, identity drift, studio clothing leaking in from character sheets, wrong colour grade). Trigger on requests to write a video prompt for a scene, continue a scene-by-scene film, fix a generation that came out wrong, or plan shots for a story.
---

# AI Narrative Film — prompt and continuity system

Rules for producing multi-scene narrative films with image/video models where the same characters must appear across many separate generations.

## Order of work

1. Lock the story: scene table with durations and dialogue. It does not change once generation starts.
2. Generate character references.
3. Generate environment references — every angle that will be used.
4. Generate references for key props.
5. Generate shot by shot.
6. Edit.

After 10–15 shots, do a rough edit before generating more. The edit reveals what prompts cannot: dead shots, pacing problems, and which new shots are actually needed.

## Prompt style

Long "cinematic" prompts with stacked lock-lists produce AI-looking output. Use photographic language.

Replace:
- "cinematic, ultra-realistic, 8K" → `Unretouched 35mm film photograph, Kodak Vision3 500T, visible grain`
- "beautiful lighting" → `flat diffused light, no sun, low contrast, lifted blacks`
- "perfect skin" → `visible pores, chapped lips, broken capillaries, uneven tone`
- "looking at camera" → `not looking at camera, eyes somewhere past it`
- "centered composition" → `slightly off-centre, handheld with small natural drift`

The four things that remove the most AI look: named film stock + grain; subject not looking at camera; off-centre handheld framing; concretely described skin flaws.

## Negative prompts

Image models have no true negative prompt. State everything critical **positively** first, then repeat it in negatives as a safety net.

Character count must be stated three times — at the top, inside the action, and in negatives:
```
Exactly three people appear in this shot and no one else: [list]
...
Only three people are ever on screen.
...
NEGATIVE: No fourth person. No duplicated character. No background crew.
```
Once is not enough. This is the fix for duplicated characters.

## Character sheets

A multi-panel sheet with studio clothing is often read as two things at once: the face for the scene, and the sheet's own outfit as a separate extra figure in frame.

Always:
```
@[Image N] = [CHARACTER] — use for his FACE ONLY. Ignore the clothing in this
reference completely. Do not create a second character wearing the clothing from
this reference. Ignore the panel grid, the grey background and any text.
```
Then describe the scene's wardrobe in its own section.

If the sheet contains text: `Ignore the colour swatches and all written text. Do not reproduce any text.`

Safer alternative: use a previously generated frame of that character in that world as the reference — one face, right wardrobe, right grade.

## References vs. description

When an image reference exists for something, **delete its verbal description**. Text and image fight each other and the result drifts.

Exception: when the reference shows the thing differently from what the scene needs, describe it in words and explicitly tell the model to ignore that part of the reference.

## Environment lock

Generate the main environment in every angle before any scene: exterior frontal, 3/4 profile, interior/working space, rear. These become fixed references in every prompt.

For scale: camera low, near the base, frame cropped — not the whole object in frame. Small human figures inside the frame prove size better than any adjective.

Environment sheets: 1:1 or 4:3, not 16:9, plus `no text, no labels`.

## Colour grade

Lock what you got, not what you wrote. If the output differs from the prompt and looks good, the new grade becomes the standard — rewrite the light block to match what is on screen, or new scenes will not cut together.

The light block must be **word-for-word identical** in every prompt:
```
LIGHT
[time of day + weather]. [sky]. Flat diffused light, no sun, no golden light,
no warm tones, low contrast, lifted blacks. No hard shadows.
```

## Shot length

- One action → 4s
- Two actions → 8s
- Three beats (0-4 / 4-7 / 7-10) → split into separate shots

Short shots are safer for identity: the longer the shot, the more time the model has to drift from the reference face. A 10s scene split into three 4s shots gives steadier identity, more edit material and cheaper retries.

Dialogue: roughly 10 seconds for three short sentences with pauses. Budget a breath before and a pause after.

## Multi-character shots

Three faces in one frame is the highest drift risk.
- Keep framing wider when several characters are present
- Never put all of them in close-up at once — close-ups are separate shots
- When two characters are only needed as presence, shoot them **from behind**: backs carry no identity, so all risk falls on one face, which can then be as tight as you like

Mandatory block:
```
Separate people, each matching his own reference face. Never blend the faces.
Never move a beard, hairstyle or garment from one to another. Do not age or
de-age anyone. Do not duplicate any character.
```

## Prop continuity

The object that ties scenes together needs its own reference image from the start. Without one it drifts within 2–3 scenes and the narrative link breaks unnoticed.

When it changes between generations, make the version from the scene where it **first appears** the standard — that is the scene where the viewer learns it — and regenerate the rest.

## Cuts

Match cut on an object is the strongest way to show passage of time: two shots with the same framing, same camera height, same object, only the hands/character changed. Use the **last frame of shot A** as the starting image for shot B.

Always cut on movement, never on a pause.

Shot / reverse shot: A left of frame looking right, B right of frame looking left. In the reverse angle **everything behind the camera disappears** — if A had the sea behind, B has the land behind. Reusing the same background in the reverse angle is the most common error and destroys the geography.

## Breaking the rules on purpose

If the film has a visual rule (frontal faces, steady camera), break it exactly where the story breaks. Failure and chaos call for profile, backs, obscured faces, unstable camera. The contrast is what gives weight to returning to the rule at the end.

## Performance direction

Describe physical behaviour, not emotion.
- "he is sad" → `his jaw tightens once and releases, he breathes out through his nose`
- "emotional" → `his eyes go glassy but no tear falls — he does not let it`
- "happy" → `the corner of his mouth lifts very slightly`

Always add:
```
No sobbing. No tears running. No trembling lip. No raised voice.
No theatrical grief. No wide gestures.
```

Small details that lift a shot: a mouth that opens slightly and closes without a sound; one small nod; a held breath before the first word.

Happy endings: no triumphal music, no wide smiles. Joy reads truer when it is held back.

## Words that must never enter a prompt

The prompt describes only what is seen and heard. Never write `That is the whole shot.`, `This is the most important scene.`, `Nothing else happens.`, or any meta-comment about the shot's purpose — the model processes them as content and produces artifacts.

Every line is either camera, action, light, or reference.

## Prompt structure

```
1. Character count (positively, at the top)
2. REFERENCES (each one's exact role + what to ignore)
3. Anti-blend block
4. WARDROBE (only where the reference does not cover it)
5. Film stock + camera + lens + movement
6. FRAMING (position in frame, face angle, eyeline direction)
7. SCENE (environment, what is in focus, what is not)
8. ACTION over N seconds
9. LIGHT (identical block across the whole film)
10. SKIN (concrete flaws)
11. NEGATIVE (repetition of the critical items)
12. AUDIO
```

## QC after every generation

Check: character count; whether the sheet's studio outfit appeared as a separate figure; identity drift toward a generic actor; prop shape/thickness/colour; colour grade against the other scenes; text leaking in from a sheet; face angle (profile where frontal was asked); over-acted expression.

Two or more failures → regenerate with a targeted fix rather than letting it into the edit.

## Short proven rules

- Steady camera must be stated hard: `the camera does not move for the entire shot`, or the model adds movement.
- Drones must shake to read as real: `drone fighting the wind, unstable`. Smooth movement looks like a render.
- Shots with no characters are free of risk — environments, objects, aerials: generate them with no identity block.
- One shot = one problem. If a generation fails at two things at once, split it into two shots.
- Repeating a rule in two places of the prompt works better than one long description in one place.
- A generated frame is the best reference. When a shot comes out right, it becomes the reference for similar shots that follow.
