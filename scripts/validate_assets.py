import csv
from pathlib import Path

root = Path(__file__).resolve().parents[1]
players_path = root / 'data' / 'players.csv'
periods_path = root / 'data' / 'team_periods.csv'
prompts_path = root / 'prompts' / 'character_prompts.md'

def read_csv(path):
    with path.open('r', encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

players = read_csv(players_path)
periods = read_csv(periods_path)
prompts = prompts_path.read_text(encoding='utf-8')

top20 = {row['source_team'] for row in players}
assert len(top20) == 20, f'expected 20 teams, got {len(top20)}'
assert len(players) == 98, f'expected 98 listed players from snapshot, got {len(players)}'

names = [row['inspired_name'] for row in players]
assert len(names) == len(set(names)), 'inspired_name values must be unique'
exact_name_matches = [row['real_nickname'] for row in players if row['real_nickname'].lower() == row['inspired_name'].split()[0].lower()]
assert not exact_name_matches, f'inspired names copy real nicknames: {exact_name_matches}'

period_names = {row['inspired_name'] for row in periods}
missing_period = [row['inspired_name'] for row in players if row['inspired_name'] not in period_names]
assert not missing_period, f'missing team periods: {missing_period}'

prompts_lower = prompts.lower()
required_prompt_bits = ['authentic team jersey', '9:16', 'photorealistic esports drama', 'negative prompt']
for bit in required_prompt_bits:
    assert bit in prompts_lower, f'missing prompt phrase: {bit}'

required_player_fields = [
    'original_reference_required',
    'original_reference_image_path',
    'reference_visual_anchor',
    'similarity_target',
    'likeness_comparison_required',
    'generation_channel',
    'revision_note',
]
for field in required_player_fields:
    assert field in players[0], f'missing players.csv field: {field}'

missing_reference_requirements = [
    row['real_nickname']
    for row in players
    if row['original_reference_required'] != 'YES'
    or not row['original_reference_image_path']
    or row['likeness_comparison_required'] != 'YES - place original reference and generated character side by side; pass only if archetype is recognizable and face is not a clone.'
]
assert not missing_reference_requirements, f'missing visual reference requirements: {missing_reference_requirements[:10]}'

non_web_generation = [
    row['real_nickname']
    for row in players
    if 'Web ChatGPT' not in row['generation_channel']
]
assert not non_web_generation, f'non-Web ChatGPT generation channel rows: {non_web_generation[:10]}'

visual_requirements_path = root / 'data' / 'visual_reference_requirements.csv'
visual_requirements = read_csv(visual_requirements_path)
assert len(visual_requirements) == len(players), 'visual_reference_requirements.csv must cover every player'

zywoo = next(row for row in players if row['real_nickname'] == 'ZywOo')
for bit in ['chubbier', 'glasses', 'curly']:
    assert bit in zywoo['reference_visual_anchor'], f'ZywOo visual anchor missing {bit}'

sample_players = [row for row in players if row['image_status'].startswith('sample') or row['image_status'].startswith('generated')]
assert len(sample_players) == 20, f'expected 20 sample-priority players, got {len(sample_players)}'

generated_root = root / 'assets' / 'generated'
generated = list(generated_root.glob('*/*/*.png')) + list(generated_root.glob('*/*/*.jpg')) + list(generated_root.glob('*/*/*.webp'))
print(f'players={len(players)} teams={len(top20)} periods={len(periods)} sample_priority={len(sample_players)} generated_images={len(generated)}')
if generated:
    teams_with_images = {p.parts[-3] for p in generated}
    print('teams_with_images=' + ','.join(sorted(teams_with_images)))
