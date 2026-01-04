#!/usr/bin/env python3
"""
SOTN Wiki Stub Generator

Parses source code definitions and generates wiki stub pages.
Uses simple string templating with {placeholder} syntax.
"""

import os
import re
import glob
from pathlib import Path
from dataclasses import dataclass
from typing import Optional

SOTN_ROOT = Path(__file__).parent.parent.parent.parent
WIKI_ROOT = Path(__file__).parent.parent
DOCS_ROOT = WIKI_ROOT / "docs"
TEMPLATES_ROOT = DOCS_ROOT / "_templates"

GITHUB_BASE = "https://github.com/Xeeynamo/sotn-decomp/blob/master"

STAGE_NAMES = {
    "NO0": ("Marble Gallery", "normal"),
    "NO1": ("Outer Wall", "normal"),
    "LIB": ("Long Library", "normal"),
    "CAT": ("Catacombs", "normal"),
    "NO2": ("Olrox's Quarters", "normal"),
    "CHI": ("Abandoned Mine", "normal"),
    "DAI": ("Royal Chapel", "normal"),
    "NP3": ("Castle Entrance", "normal"),
    "CEN": ("Castle Center", "normal"),
    "NO4": ("Underground Caverns", "normal"),
    "ARE": ("Colosseum", "normal"),
    "TOP": ("Castle Keep", "normal"),
    "NZ0": ("Alchemy Laboratory", "normal"),
    "NZ1": ("Clock Tower", "normal"),
    "WRP": ("Warp Rooms", "normal"),
    "ST0": ("Final Stage: Bloodlines", "normal"),
    "BO0": ("Boss: Slogra & Gaibon", "boss"),
    "BO1": ("Boss: Doppleganger10", "boss"),
    "BO2": ("Boss: Minotaur & Werewolf", "boss"),
    "BO3": ("Boss: Scylla", "boss"),
    "BO4": ("Boss: Granfaloon", "boss"),
    "BO5": ("Boss: Hippogryph", "boss"),
    "BO6": ("Boss: Richter", "boss"),
    "BO7": ("Boss: Cerberus", "boss"),
    "RNO0": ("Black Marble Gallery", "reverse"),
    "RNO1": ("Reverse Outer Wall", "reverse"),
    "RLIB": ("Forbidden Library", "reverse"),
    "RCAT": ("Floating Catacombs", "reverse"),
    "RNO2": ("Death Wing's Lair", "reverse"),
    "RCHI": ("Cave", "reverse"),
    "RDAI": ("Anti-Chapel", "reverse"),
    "RNP3": ("Reverse Castle Entrance", "reverse"),
    "RCEN": ("Reverse Castle Center", "reverse"),
    "RNO4": ("Reverse Caverns", "reverse"),
    "RARE": ("Reverse Colosseum", "reverse"),
    "RTOP": ("Reverse Castle Keep", "reverse"),
    "RNZ0": ("Necromancy Laboratory", "reverse"),
    "RNZ1": ("Reverse Clock Tower", "reverse"),
    "RBO0": ("Boss: Trio", "boss"),
    "RBO1": ("Boss: Beelzebub", "boss"),
    "RBO2": ("Boss: Death", "boss"),
    "RBO3": ("Boss: Medusa", "boss"),
    "RBO4": ("Boss: Creature", "boss"),
    "RBO5": ("Boss: Doppleganger40", "boss"),
    "RBO6": ("Boss: Shaft/Dracula", "boss"),
    "RBO7": ("Boss: Akmodan II", "boss"),
    "RBO8": ("Boss: Galamoth", "boss"),
}

ITEM_CATEGORIES = {
    (0x00, 0x04): ("shields", "Shield"),
    (0x05, 0x10): ("shields", "Shield"),
    (0x11, 0x1C): ("weapons", "Sword"),
    (0x1D, 0x46): ("consumables", "Consumable"),
    (0x47, 0x52): ("weapons", "Throwable"),
    (0x53, 0xA8): ("weapons", "Weapon"),
}

BODY_CATEGORIES = {
    (0x00, 0x19): ("armor", "Armor"),
    (0x1A, 0x2F): ("armor", "Helm"),
    (0x30, 0x38): ("accessories", "Cape"),
    (0x39, 0x59): ("accessories", "Accessory"),
}


@dataclass
class StubData:
    name: str
    slug: str
    category: str
    subcategory: str
    code_id: Optional[str] = None
    hex_id: Optional[str] = None
    source_file: Optional[str] = None
    stage_code: Optional[str] = None
    castle_type: Optional[str] = None


def slugify(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


def titleify(name: str) -> str:
    name = name.replace("_", " ").replace("-", " ")
    name = re.sub(r"^e ", "", name)
    return name.title()


def load_template(template_name: str) -> str:
    template_path = TEMPLATES_ROOT / template_name
    if template_path.exists():
        return template_path.read_text()
    return "# {name}\n\n*Stub page*\n"


def render_template(template: str, data: StubData) -> str:
    replacements = {
        "{name}": data.name,
        "{slug}": data.slug,
        "{category}": data.category,
        "{subcategory}": data.subcategory,
        "{code_id}": data.code_id or "TBD",
        "{hex_id}": data.hex_id or "TBD",
        "{source_file}": data.source_file or "TBD",
        "{source_url}": f"{GITHUB_BASE}/{data.source_file}"
        if data.source_file
        else "#",
        "{stage_code}": data.stage_code or "TBD",
        "{castle_type}": data.castle_type or "normal",
    }
    result = template
    for placeholder, value in replacements.items():
        result = result.replace(placeholder, value)
    return result


def parse_items_h() -> list[StubData]:
    items_path = SOTN_ROOT / "include" / "items.h"
    if not items_path.exists():
        print(f"Warning: {items_path} not found")
        return []

    content = items_path.read_text()
    items = []

    hand_pattern = re.compile(r"ITEM_(\w+)\s*=\s*(0x[0-9A-Fa-f]+|[0-9]+)")
    for match in hand_pattern.finditer(content):
        name = match.group(1)
        hex_val = match.group(2)
        if name in ("EMPTY_HAND", "NUM_HAND_ITEMS"):
            continue

        int_val = int(hex_val, 16) if hex_val.startswith("0x") else int(hex_val)
        category = "weapons"
        subcat = "Weapon"
        for (low, high), (cat, sub) in ITEM_CATEGORIES.items():
            if low <= int_val <= high:
                category = cat
                subcat = sub
                break

        items.append(
            StubData(
                name=titleify(name),
                slug=slugify(name),
                category="items",
                subcategory=category,
                code_id=f"ITEM_{name}",
                hex_id=hex_val,
                source_file="include/items.h",
            )
        )

    return items


def parse_enemies() -> list[StubData]:
    enemies = []
    enemy_files = glob.glob(str(SOTN_ROOT / "src" / "st" / "*" / "e_*.c"))

    seen_names = set()
    for filepath in enemy_files:
        path = Path(filepath)
        stage_code = path.parent.name.upper()
        enemy_name = path.stem

        if enemy_name in seen_names:
            continue
        seen_names.add(enemy_name)

        clean_name = enemy_name.replace("e_", "")
        enemies.append(
            StubData(
                name=titleify(clean_name),
                slug=slugify(clean_name),
                category="enemies",
                subcategory="enemy",
                source_file=f"src/st/{path.parent.name}/{path.name}",
                stage_code=stage_code,
            )
        )

    return enemies


def parse_stages() -> list[StubData]:
    stages = []
    for code, (name, castle_type) in STAGE_NAMES.items():
        if castle_type == "boss":
            category = "bosses"
        else:
            category = "stages"

        stages.append(
            StubData(
                name=name,
                slug=slugify(name),
                category=category,
                subcategory=castle_type,
                stage_code=code,
                castle_type=castle_type,
                source_file=f"src/st/{code.lower()}/"
                if not code.startswith("BO") and not code.startswith("RBO")
                else f"src/boss/{code.lower()}/",
            )
        )

    return stages


def write_stub(data: StubData, template: str, output_dir: Path) -> bool:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f"{data.slug}.md"

    if output_path.exists():
        return False

    content = render_template(template, data)
    output_path.write_text(content)
    return True


def generate_all_stubs(dry_run: bool = False) -> dict[str, int]:
    stats = {"items": 0, "enemies": 0, "stages": 0, "bosses": 0, "skipped": 0}

    item_template = load_template("TEMPLATE_WEAPON.md")
    items = parse_items_h()
    for item in items:
        output_dir = DOCS_ROOT / "items" / item.subcategory
        if dry_run:
            print(f"Would create: {output_dir / item.slug}.md")
            stats["items"] += 1
        elif write_stub(item, item_template, output_dir):
            stats["items"] += 1
        else:
            stats["skipped"] += 1

    enemy_template = load_template("TEMPLATE_ENEMY.md")
    enemies = parse_enemies()
    for enemy in enemies:
        output_dir = DOCS_ROOT / "enemies"
        if dry_run:
            print(f"Would create: {output_dir / enemy.slug}.md")
            stats["enemies"] += 1
        elif write_stub(enemy, enemy_template, output_dir):
            stats["enemies"] += 1
        else:
            stats["skipped"] += 1

    stage_template = load_template("TEMPLATE_STAGE.md")
    boss_template = load_template("TEMPLATE_BOSS.md")
    stages = parse_stages()
    for stage in stages:
        if stage.category == "bosses":
            output_dir = DOCS_ROOT / "bosses"
            template = boss_template
            if dry_run:
                print(f"Would create: {output_dir / stage.slug}.md")
                stats["bosses"] += 1
            elif write_stub(stage, template, output_dir):
                stats["bosses"] += 1
            else:
                stats["skipped"] += 1
        else:
            castle_type = stage.castle_type or "normal"
            output_dir = DOCS_ROOT / "stages" / castle_type
            template = stage_template
            if dry_run:
                print(f"Would create: {output_dir / stage.slug}.md")
                stats["stages"] += 1
            elif write_stub(stage, template, output_dir):
                stats["stages"] += 1
            else:
                stats["skipped"] += 1

    return stats


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate SOTN wiki stub pages")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without writing files",
    )
    parser.add_argument(
        "--category",
        choices=["items", "enemies", "stages", "all"],
        default="all",
        help="Which category to generate",
    )
    args = parser.parse_args()

    print(f"SOTN Wiki Stub Generator")
    print(f"Source root: {SOTN_ROOT}")
    print(f"Wiki root: {WIKI_ROOT}")
    print(f"Dry run: {args.dry_run}")
    print()

    stats = generate_all_stubs(dry_run=args.dry_run)

    print()
    print("Summary:")
    print(f"  Items:   {stats['items']}")
    print(f"  Enemies: {stats['enemies']}")
    print(f"  Stages:  {stats['stages']}")
    print(f"  Bosses:  {stats['bosses']}")
    print(f"  Skipped: {stats['skipped']} (already exist)")
    print(f"  Total:   {sum(stats.values()) - stats['skipped']}")


if __name__ == "__main__":
    main()
