#!/usr/bin/env python3
"""Generate self-hosted GitHub stats + top-languages SVG cards.

Writes:
  OUT_DIR/stats.svg
  OUT_DIR/top-langs.svg
No third-party card service is involved, so the cards never go down.
"""
import json
import os
import sys
import urllib.request
from html import escape

USER = os.environ.get("GH_USER", "parvatkhattak")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("OUT_DIR", "assets")
DISPLAY_NAME = os.environ.get("DISPLAY_NAME", "Parvat Khattak")
# Notebook outputs / exported HTML inflate byte counts without reflecting real code
EXCLUDE_LANGS = {"Jupyter Notebook", "HTML"}

# Tokyo Night palette (matches the banner)
BG, BORDER, TITLE, TEXT, ICON, MUTED = "#1a1b27", "#2a2e45", "#70a5fd", "#c0caf5", "#bf91f3", "#565f89"
LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a", "Jupyter Notebook": "#DA5B0B",
    "C++": "#f34b7d", "C": "#555555", "Java": "#b07219", "HTML": "#e34c26", "CSS": "#663399",
    "Shell": "#89e051", "Swift": "#F05138", "PLpgSQL": "#336790", "CMake": "#DA3434", "Makefile": "#427819",
    "Dockerfile": "#384d54", "Kotlin": "#A97BFF", "Go": "#00ADD8", "Rust": "#dea584",
}


def gql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        sys.exit(f"GraphQL error: {data['errors']}")
    return data["data"]


QUERY = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    name
    followers { totalCount }
    contributionsCollection { totalCommitContributions restrictedContributionsCount }
    pullRequests { totalCount }
    issues { totalCount }
    repositoriesContributedTo(contributionTypes: [COMMIT, PULL_REQUEST, ISSUE]) { totalCount }
    repositories(first: 100, after: $cursor, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name color } } }
      }
    }
  }
}
"""


def collect():
    cursor, repos, user = None, [], None
    while True:
        u = gql(QUERY, {"login": USER, "cursor": cursor})["user"]
        user = user or u
        repos += u["repositories"]["nodes"]
        page = u["repositories"]["pageInfo"]
        if not page["hasNextPage"]:
            break
        cursor = page["endCursor"]
    langs = {}
    for repo in repos:
        for e in repo["languages"]["edges"]:
            n = e["node"]["name"]
            if n in EXCLUDE_LANGS:
                continue
            langs.setdefault(n, [0, e["node"]["color"]])
            langs[n][0] += e["size"]
    cc = user["contributionsCollection"]
    return {
        "name": DISPLAY_NAME or user["name"] or USER,
        "stars": sum(r["stargazerCount"] for r in repos),
        "commits": cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        "prs": user["pullRequests"]["totalCount"],
        "issues": user["issues"]["totalCount"],
        "repos": user["repositories"]["totalCount"],
        "contributed": user["repositoriesContributedTo"]["totalCount"],
        "followers": user["followers"]["totalCount"],
    }, langs


# Octicon paths (16x16)
ICONS = {
    "star": "M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z",
    "commit": "M11.93 8.5a4.002 4.002 0 0 1-7.86 0H.75a.75.75 0 0 1 0-1.5h3.32a4.002 4.002 0 0 1 7.86 0h3.32a.75.75 0 0 1 0 1.5Zm-1.43-.75a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z",
    "pr": "M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354Z",
    "issue": "M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z",
    "repo": "M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8Z",
    "contrib": "M2 2.5A2.5 2.5 0 0 1 4.5 0h8.75a.75.75 0 0 1 .75.75v12.5a.75.75 0 0 1-.75.75h-2.5a.75.75 0 0 1 0-1.5h1.75v-2h-8a1 1 0 0 0-.714 1.7.75.75 0 1 1-1.072 1.05A2.495 2.495 0 0 1 2 11.5Zm10.5-1h-8a1 1 0 0 0-1 1v6.708A2.486 2.486 0 0 1 4.5 9h8ZM5 12.25a.25.25 0 0 1 .25-.25h3.5a.25.25 0 0 1 .25.25v3.25a.25.25 0 0 1-.4.2l-1.45-1.087a.249.249 0 0 0-.3 0L5.4 15.7a.25.25 0 0 1-.4-.2Z",
}

FONT = "'Segoe UI', Ubuntu, 'DejaVu Sans', sans-serif"


def stats_svg(s):
    rows = [
        ("star", "Total Stars Earned", s["stars"]),
        ("commit", "Total Commits (this year)", s["commits"]),
        ("pr", "Total PRs", s["prs"]),
        ("issue", "Total Issues", s["issues"]),
        ("repo", "Public Repositories", s["repos"]),
        ("contrib", "Contributed to (this year)", s["contributed"]),
    ]
    h = 210
    body = ""
    for i, (icon, label, value) in enumerate(rows):
        y = 54 + i * 24
        body += (
            f'<g transform="translate(25,{y})">'
            f'<path fill="{ICON}" d="{ICONS[icon]}"/>'
            f'<text x="26" y="12.5" font-family="{FONT}" font-size="13.5" font-weight="500" fill="{TEXT}">{label}:</text>'
            f'<text x="370" y="12.5" text-anchor="end" font-family="{FONT}" font-size="13.5" font-weight="700" fill="{TEXT}">{value:,}</text></g>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="{h}" viewBox="0 0 440 {h}" role="img" aria-label="GitHub stats">'
        f'<rect x="0.5" y="0.5" rx="6" width="439" height="{h - 1}" fill="{BG}" stroke="{BORDER}"/>'
        f'<text x="25" y="34" font-family="{FONT}" font-size="17" font-weight="600" fill="{TITLE}">{escape(s["name"])}\'s GitHub Stats</text>'
        f"{body}</svg>"
    )


def langs_svg(langs, top=8):
    items = sorted(langs.items(), key=lambda kv: kv[1][0], reverse=True)[:top]
    total = sum(v[0] for _, v in items) or 1
    h = 210
    bar, x = "", 25.0
    for name, (size, color) in items:
        w = size / total * 390
        c = color or LANG_COLORS.get(name, MUTED)
        bar += f'<rect x="{x:.2f}" y="52" width="{w:.2f}" height="8" fill="{c}"/>'
        x += w
    legend = ""
    for i, (name, (size, color)) in enumerate(items):
        c = color or LANG_COLORS.get(name, MUTED)
        cx, cy = (0 if i % 2 == 0 else 198), (i // 2) * 28
        pct = f"{size / total * 100:.1f}%"
        legend += (
            f'<g transform="translate({cx},{cy})">'
            f'<circle cx="5" cy="6" r="5" fill="{c}"/>'
            f'<text x="16" y="10" font-family="{FONT}" font-size="12.5" font-weight="500" fill="{TEXT}">{escape(name)}</text>'
            f'<text x="175" y="10" text-anchor="end" font-family="{FONT}" font-size="12.5" font-weight="600" fill="#7aa2f7">{pct}</text></g>'
        )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="{h}" viewBox="0 0 440 {h}" role="img" aria-label="Top languages">'
        f'<rect x="0.5" y="0.5" rx="6" width="439" height="{h - 1}" fill="{BG}" stroke="{BORDER}"/>'
        f'<text x="25" y="34" font-family="{FONT}" font-size="17" font-weight="600" fill="{TITLE}">Most Used Languages</text>'
        f'<rect x="25" y="52" width="390" height="8" rx="4" fill="#24283b"/>'
        f'{bar}'
        f'<g transform="translate(25,84)">{legend}</g></svg>'
    )


def main():
    if not TOKEN:
        sys.exit("GITHUB_TOKEN is required")
    stats, langs = collect()
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "stats.svg"), "w") as f:
        f.write(stats_svg(stats))
    with open(os.path.join(OUT, "top-langs.svg"), "w") as f:
        f.write(langs_svg(langs))
    print(json.dumps(stats), sorted(langs, key=lambda k: -langs[k][0])[:8])


if __name__ == "__main__":
    main()
