from pathlib import Path
from datetime import datetime, timezone
import json, urllib.request, subprocess, fcntl

OZ = Path("/home/destiny/Obsidian/Ozark Prepper")
SA = OZ / "Sub-Agents"
LOG = OZ / "Victoria_Operational_Log.md"
TRACK = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/.victoria_team_index.txt")
CANVA_TOOL = Path("/home/destiny/Obsidian/Destiny/Three_Brain_Architecture/skills/canva_bridge/canva_tool.js")

EBOOKS = [
    OZ / "ebook_diy_5-gallon_water_filter.md",
    OZ / "ebook_how_to_preserve_eggs_for_a_year_without_refrigeration.md",
    OZ / "ebook_starting_preps_on_a_tight_budget.md",
    OZ / "ebook_the_arkansas_woodsmans_field_manual.md",
    OZ / "ebook_the_simplest_backup_solar_setup_for_beginners.md",
]

AGENTS = [
    ("Audrey", SA / "Audrey_Research",
     "Audit the existing Ozark Prepper ebooks for accuracy, usefulness, missing information, weak sections, outdated material, and opportunities to make each product worth its price. Work on existing products before proposing new ebooks. Produce concrete research and upgrade instructions for the next book that needs improvement."),

    ("Bridget", SA / "Bridget_Creative",
     "Upgrade the writing of an existing Ozark Prepper ebook. Improve weak explanations, organization, readability, practical value, chapter flow, checklists, examples, and beginner usefulness. Focus on making the existing paid ebooks feel like professional products worth buying. Preserve good material instead of replacing it blindly."),

    ("Chloe", SA / "Chloe_SEO",
     "Upgrade the product positioning for an existing Ozark Prepper ebook. Create a strong title or subtitle if needed, SEO title, product description, meta description, keywords, landing-page copy, and benefit-focused sales copy that accurately reflects the improved book. No fake claims."),

    ("Daphne", SA / "Daphne_Publishing",
     "Manage the production quality of an existing Ozark Prepper ebook. Check what is needed for a professional final PDF and EPUB, including cover, table of contents, readable formatting, images, diagrams, captions, page consistency, links, and final publishing package. Do not publish unfinished work or delete the current version."),

    ("Evelyn", SA / "Evelyn_Web",
     "Improve the existing Ozark Prepper website and ebook product presentation. Review the homepage and product pages so the four paid ebooks and one free ebook look professional, trustworthy, easy to understand, visually strong, and easy to buy or download. Use existing payment links and do not break working sales links."),

    ("Fiona", SA / "Fiona_Design",
     "Redesign the visual presentation of an existing Ozark Prepper ebook. Create a professional cover direction plus useful interior visual ideas such as diagrams, checklists, illustrations, comparison graphics, chapter graphics, or infographics. Use Canva to produce high-quality visuals suitable for the finished ebook and website."),

    ("Bella", OZ / "Bella",
     "Create professional faceless video and visual promotion for an improved Ozark Prepper ebook. Produce a useful video concept, shot list, thumbnail direction, and description that accurately represents the product and sends viewers to the correct ebook."),

    ("Maggie", SA / "Maggie_Marketing",
     "Create professional free marketing for an improved existing Ozark Prepper ebook using legal, honest promotion. Prepare strong Facebook, Reddit, Quora, and other appropriate promotional content plus a Canva social graphic. No spam, fake accounts, fake testimonials, or fake sales."),

    ("Hannah", SA / "Hannah_Community",
     "Support the improved Ozark Prepper ebooks with useful community content. Create natural answers to likely customer questions, helpful replies, FAQ ideas, and feedback themes that can improve the ebook and product page. Do not invent customer reviews.")
]

def _ask(prompt):
    payload = {"model": "qwen2.5:14b", "prompt": prompt, "stream": False, "options": {"num_predict": 900, "temperature": 0.3}}
    req = urllib.request.Request("http://127.0.0.1:11434/api/generate", data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    lock_path = Path("/tmp/destiny_model_busy.lock")
    with lock_path.open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        lock.write("victoria_team:qwen")
        lock.flush()
        with urllib.request.urlopen(req, timeout=900) as r:
            return json.loads(r.read().decode()).get("response", "").strip()


def _bridget_build_ebook(ebook_path, ebook_text):
    upgraded_dir = OZ / "upgraded_ebooks"
    upgraded_dir.mkdir(parents=True, exist_ok=True)
    upgraded_path = upgraded_dir / ebook_path.name

    plan_prompt = (
        "You are Bridget under Victoria, CEO of Ozark Prepper. "
        "Create a professional expansion plan for this REAL ebook: " + ebook_path.name + ". "
        "The finished ebook must be substantially more useful than the current source, practical, "
        "well organized, beginner friendly, and worth buying. Preserve good existing information. "
        "Do not invent statistics, prices, medical claims, or unsupported facts. "
        "Return ONLY a numbered list of 6 to 10 chapter titles with a short description for each.\n\n"
        "CURRENT SOURCE:\n" + ebook_text[:24000]
    )

    existing = upgraded_path.read_text(encoding="utf-8") if upgraded_path.exists() else ""

    if "## Production Plan" in existing and "<!-- Bridget upgrade in progress -->" in existing:
        print("BRIDGET: Resuming existing ebook upgrade...", flush=True)
        plan_section = existing.split("## Production Plan", 1)[1]
        if "\n\n---\n\n## Chapter " in plan_section:
            plan = plan_section.split("\n\n---\n\n## Chapter ", 1)[0].strip()
        else:
            plan = plan_section.strip()
    else:
        print("BRIDGET: Building ebook production plan...", flush=True)
        plan = _ask(plan_prompt)
        print("BRIDGET: Production plan finished and saving...", flush=True)
        upgraded_path.write_text(
            "# " + ebook_path.stem.replace("_", " ").title() +
            "\n\n<!-- Bridget upgrade in progress -->\n\n"
            "## Production Plan\n\n" + plan.strip() + "\n",
            encoding="utf-8"
        )
        existing = upgraded_path.read_text(encoding="utf-8")

    chapters = []
    for line in plan.splitlines():
        stripped = line.strip()
        if stripped and stripped[0].isdigit() and (". " in stripped or ") " in stripped):
            title = stripped.split(". ", 1)[-1].split(") ", 1)[-1]
            title = title.split(" - ", 1)[0].split(" — ", 1)[0].strip()
            if title:
                chapters.append(title)

    if not chapters:
        chapters = [
            "Getting Started",
            "What You Need",
            "Step-by-Step Method",
            "Common Mistakes and Safety",
            "Practical Checklist",
            "Putting the Plan Into Action",
        ]

    chapters = chapters[:10]

    for number, title in enumerate(chapters, 1):
        existing = upgraded_path.read_text(encoding="utf-8")
        if "## Chapter " + str(number) + ":" in existing:
            print("BRIDGET: Chapter", number, "already saved - skipping", flush=True)
            continue

        chapter_prompt = (
            "You are Bridget under Victoria, CEO of Ozark Prepper. "
            "Write ONE finished chapter for the upgraded ebook " + ebook_path.name + ". "
            "Chapter " + str(number) + ": " + title + ". "
            "Write polished publication-ready Markdown, approximately 400 to 650 words for this section. "
            "Be practical, specific, useful, readable, and beginner friendly. "
            "Use headings, bullets, checklists, examples, and warnings where genuinely useful. "
            "Do not include image placeholders. Do not tell Neil to do production work. "
            "Do not invent statistics, prices, medical claims, or unsupported facts. "
            "Avoid repeating material that belongs in other chapters.\n\n"
            "BOOK PLAN:\n" + plan[:8000] +
            "\n\nORIGINAL SOURCE FOR REFERENCE:\n" + ebook_text[:16000]
        )

        print("BRIDGET: Writing chapter", number, "OF", len(chapters), "-", title, flush=True)
        chapter = _ask(chapter_prompt)

        with upgraded_path.open("a", encoding="utf-8") as f:
            f.write(
                "\n\n---\n\n## Chapter " + str(number) + ": " + title +
                "\n\n" + chapter.strip() + "\n"
            )

        print("BRIDGET SAVED CHAPTER", number, "OF", len(chapters), "-", title, flush=True)

    with upgraded_path.open("a", encoding="utf-8") as f:
        f.write("\n\n<!-- Bridget upgrade complete -->\n")

    return upgraded_path, len(chapters)


def _run_canva(*args):
    result = subprocess.run(
        [
            "bash", "-lc",
            'source "$HOME/.nvm/nvm.sh" && node "$1" "$2" "$3" "$4"',
            "bash", str(CANVA_TOOL),
            args[0] if len(args) > 0 else "",
            args[1] if len(args) > 1 else "",
            args[2] if len(args) > 2 else ""
        ],
        capture_output=True,
        text=True,
        timeout=300
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "Canva bridge failed")
    return json.loads(result.stdout)


def _canva_generate(design_type, prompt):
    outer = _run_canva("generate", design_type, prompt)
    inner = json.loads(outer["content"][0]["text"])
    job = inner["job"]
    designs = job["result"]["generated_designs"]

    return {
        "job_id": job["id"],
        "designs": [
            {
                "candidate_id": d["candidate_id"],
                "url": d["url"]
            }
            for d in designs
        ]
    }


def _canva_accept(job_id, candidate_id):
    outer = _run_canva("accept", job_id, candidate_id)
    inner = json.loads(outer["content"][0]["text"])
    return inner["design_summary"]


def _canva_export(design_id, format_type="png"):
    outer = _run_canva("export", design_id, format_type)
    inner = json.loads(outer["content"][0]["text"])
    return inner["job"]


def run():
    i = 0
    if TRACK.exists():
        try:
            i = int(TRACK.read_text().strip())
        except Exception:
            i = 0
    name, folder, job = AGENTS[i % len(AGENTS)]

    ebook_index = (i // len(AGENTS)) % len(EBOOKS)
    ebook_path = EBOOKS[ebook_index]

    try:
        ebook_text = ebook_path.read_text(encoding="utf-8")
    except Exception as e:
        ebook_text = "SOURCE COULD NOT BE READ: " + str(e)

    folder.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d_%H%M")
    out = folder / (name.lower() + "_work_" + stamp + ".md")

    prompt = (
        "You are " + name + " under Victoria, CEO of Ozark Prepper only. "
        "Your company sells prepper ebooks and must bring in money. "
        "You are working on this REAL existing ebook: " + ebook_path.name + ". "
        "Do the assigned work directly on the provided source. "
        "Do NOT tell Neil or another person to gather, review, choose, or fix things for you. "
        "Do NOT merely explain how the work could be done. Perform the work yourself.\n\n"
        "YOUR ASSIGNMENT:\n" + job +
        "\n\nCURRENT EBOOK SOURCE:\n" + ebook_text[:24000]
    )

    if name == "Bridget":
        upgraded_path, chapter_count = _bridget_build_ebook(ebook_path, ebook_text)
        body = (
            "## Ebook being upgraded\n" + ebook_path.name +
            "\n\n## Upgraded source saved\n" + str(upgraded_path) +
            "\n\n## Bridget result\nCompleted and saved " +
            str(chapter_count) + " ebook chapters."
        )
    else:
        body = _ask(prompt)
        body = "## Ebook being upgraded\n" + ebook_path.name + "\n\n" + body

    canva_jobs = {
        "Fiona": (
            "youtube_thumbnail",
            "Create a professional Ozark Prepper YouTube thumbnail from this design brief. "
            "Rugged, trustworthy, high quality, readable, no clickbait."
        ),
        "Bella": (
            "youtube_thumbnail",
            "Create a professional visual concept for this Ozark Prepper faceless YouTube video. "
            "Make it useful as the video's thumbnail and visual direction."
        ),
        "Evelyn": (
            "infographic",
            "Create a professional Ozark Prepper website graphic or infographic based on this website work. "
            "Make it useful, clean, rugged, trustworthy, and easy to understand."
        ),
        "Maggie": (
            "facebook_post",
            "Create a professional Ozark Prepper Facebook promotional graphic based on this marketing work. "
            "Helpful and trustworthy, not spammy or misleading."
        ),
    }

    if name in canva_jobs:
        design_type, canva_instruction = canva_jobs[name]
        try:
            generated = _canva_generate(
                design_type,
                canva_instruction + "\n\nAgent work:\n" + body
            )

            designs = generated.get("designs", [])

            if designs:
                body += "\n\n## Canva design candidates\n" + "\n".join(
                    "- " + d["url"] for d in designs
                )

                chosen = designs[0]

                saved = _canva_accept(
                    generated["job_id"],
                    chosen["candidate_id"]
                )

                body += (
                    "\n\n## Canva working design"
                    "\n- Design ID: " + saved["id"] +
                    "\n- Edit: " + saved["urls"]["edit_url"] +
                    "\n- View: " + saved["urls"]["view_url"]
                )

                exported = _canva_export(saved["id"], "png")

                urls = exported.get("urls", [])
                if urls:
                    body += "\n- Finished PNG: " + urls[0]

        except Exception as e:
            body += "\n\n## Canva\nCanva generation/finish skipped: " + str(e)

    out.write_text("# " + name + " work " + stamp + "\n\n" + body + "\n", encoding="utf-8")
    TRACK.write_text(str(i + 1))
    old = LOG.read_text(encoding="utf-8") if LOG.exists() else "# Victoria Operational Log\n"
    LOG.write_text(old + "\n## " + stamp + " UTC\n" + name + " wrote " + out.name + "\n", encoding="utf-8")
    return "victoria team: " + name + " wrote " + out.name

if __name__ == "__main__":
    print(run())
