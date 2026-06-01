# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

`restart-aws-labs` is a documentation-only repository storing lab notes and screenshots for the AWS Restart Bootcamp. There are no build tools, tests, or scripts — all content is Markdown with embedded images.

## Content language

All lab content is written in **Spanish**.

## File format and conventions

Lab notes use standard GitHub-compatible Markdown:

- Images are embedded with standard Markdown syntax: `![](imgs/Pasted%20image%20YYYYMMDDHHMMSS.png)`
- Filenames are URL-encoded (spaces become `%20`) so links render on GitHub and standard Markdown viewers
- Do not use Obsidian wikilink syntax (`![[...]]`) — links must stay GitHub-compatible

## Structure

Each lab lives under `LABS/labs-{number}/`:

```
LABS/
  labs-11/
    LAB-11-DESARROLLO.md   # lab write-up
    imgs/                  # screenshots pasted from Obsidian
```

New labs follow this same pattern: `LABS/labs-{N}/LAB-{N}-DESARROLLO.md` with a sibling `imgs/` directory.

## .gitignore rules

The `.gitignore` ignores all `*.md` files except `LABS/**/LAB-*.md`. This means only lab write-ups matching that pattern are tracked; other Markdown files (notes, drafts, README edits) are excluded automatically.

## Workflow notes

Screenshots are captured and pasted directly in Obsidian, which auto-names them `Pasted image YYYYMMDDHHMMSS.png` and places them in `imgs/`. Do not rename these files; reference them in Markdown with URL-encoded spaces (`%20`).
