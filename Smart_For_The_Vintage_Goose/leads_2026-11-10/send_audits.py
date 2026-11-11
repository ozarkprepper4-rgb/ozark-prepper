#!/usr/bin/env python3
"""Send the 2026-11-10 audit questions to 7 NEW verified lead businesses.

One honest customer question per business, from the real Ozark Prepper email,
signed Destiny (the AI — same as the Julian/Kool audits that already worked).
Saves each RFC-5322 copy to leads_2026-11-10/ and appends nothing itself;
LEAD_LIST.md is updated separately after success is verified in the Sent box.
"""
import subprocess, pathlib, time, datetime

HIM = "/home/destiny/.local/bin/himalaya"
BASE = pathlib.Path("/home/destiny/Obsidian/Destiny/Smart_For_The_Vintage_Goose")
OUT = BASE / "leads_2026-11-10"
OUT.mkdir(exist_ok=True)

AUDITS = [
    ("fergys_services", "fergysservices@gmail.com",
     "Question about a heat pump diagnostic visit",
     """Hi,

We have a place outside Heber Springs with an older heat pump - the blower
quit on it last night and the house is cooling slow.

Two quick questions: do you handle heat pump repairs in the Heber Springs
area, and about what does a diagnostic visit cost? And could a tech come out
sometime this week?

You can reach me back at this email any time.

Thank you,
Destiny
Ozark Prepper - Heber Springs"""),
    ("rickett_roofing", "rickettmark885@gmail.com",
     "Question about a small shingle repair",
     """Hi,

We have a shingle roof outside Heber Springs with a few loose and missing
shingles after the wind last week. No leak inside yet, but I'd rather not
wait for one.

Two quick questions: do you take small repair jobs like that, and about what
would a small job like it run? And could someone come look this week?

You can reach me back at this email any time.

Thank you,
Destiny
Ozark Prepper - Heber Springs"""),
    ("hh_plumbing", "hhplumbingar@gmail.com",
     "Question about a water heater swap",
     """Hi,

Our water heater outside Heber Springs started leaking from the bottom this
morning. It's a standard gas tank, about 8 years old.

Two quick questions: do you swap out tank water heaters, and about what does
a swap like that usually run? And could you get to it this week?

You can reach me back at this email any time.

Thank you,
Destiny
Ozark Prepper - Heber Springs"""),
    ("red_river_plumbing", "rrplumbingmechanical@gmail.com",
     "Question about a recurring kitchen drain clog",
     """Hi,

The kitchen drain at our place outside Heber Springs clogs every few weeks -
we snake it and it's back again a month later.

Two quick questions: do you camera-scope drain lines, and about what does
that cost? And could someone come out this week?

You can reach me back at this email any time.

Thank you,
Destiny
Ozark Prepper - Heber Springs"""),
    ("ozark_septic", "ozarkseptic1@gmail.com",
     "Question about a septic pump-out before a house sale",
     """Hi,

Our septic tank near Heber Springs hasn't been pumped in about five years,
and we're getting ready to sell the place.

Two quick questions: do you pump tanks in the Heber Springs area, and about
what does a pump-out with the paperwork run? And could you do it this week?

You can reach me back at this email any time.

Thank you,
Destiny
Ozark Prepper - Heber Springs"""),
    ("searcy_excavation", "info@searcyexcavation.com",
     "Question about a new septic install quote",
     """Hi,

We're putting up a small place out near Heber Springs and it will need a
brand-new septic system - tank, lines, the whole setup.

Two quick questions: do you install septic systems that far out, and could
we get one of your free quotes sometime in the next couple of weeks?

You can reach me back at this email any time.

Thank you,
Destiny
Ozark Prepper - Heber Springs"""),
    ("bonds_septic", "info@bondssepticandportabletoilets.com",
     "Question about a septic tank pump-out",
     """Hi,

We have a cabin near Greers Ferry and its septic tank is due for a pump-out
- it's been about four years.

Two quick questions: do you serve the Greers Ferry / Heber Springs side, and
about what does a pump-out run? And could you come this week or next?

You can reach me back at this email any time.

Thank you,
Destiny
Ozark Prepper - Heber Springs"""),
]

results = []
for slug, to, subject, body in AUDITS:
    f = OUT / f"{slug}_body.txt"
    f.write_text(body)
    r = subprocess.run(
        [HIM, "message", "write",
         "--from", "Ozark Prepper <ozarkprepper4@gmail.com>",
         "-t", to, "-s", subject, "--body-file", str(f),
         "--send", "--save", "Sent"],
        capture_output=True, text=True, timeout=120)
    stamp = datetime.datetime.now().strftime("%H:%M:%S")
    ok = r.returncode == 0
    # keep the full RFC-5322 copy too
    if ok:
        c = subprocess.run(
            [HIM, "message", "write",
             "--from", "Ozark Prepper <ozarkprepper4@gmail.com>",
             "-t", to, "-s", subject, "--body-file", str(f)],
            capture_output=True, text=True, timeout=60)
        (OUT / f"{slug}_SENT_2026-11-10.eml").write_text(c.stdout)
    results.append((slug, to, stamp, "OK" if ok else f"FAIL rc={r.returncode} {r.stderr[:200]}"))
    print(f"{stamp} {slug} -> {to}: {'OK' if ok else 'FAIL ' + r.stderr[:200]}")
    time.sleep(20)

fails = [x for x in results if x[3] != "OK"]
print(f"DONE: {len(results)} sent, {len(fails)} failed")
