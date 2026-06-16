# Agent Instructions for Robertsoftware2026

## Key Behavioral Rule

**DO NOT auto-correct code or work shown. DO NOT suggest changes or show "what you should do" unless explicitly asked.**

When taking any action, **explain why you're doing it first**.

---

## Project Overview

This repository contains:
- **OOP/Software/** — Object-oriented programming learning materials, progressively introducing classes, methods, attributes, encapsulation, getters/setters, and inheritance
- **treacherous_beams/** — A text-based game with fighters, wizards, and archers using OOP concepts
- Various testing and experimentation files

---

## Working with This Codebase

### When Code Has Issues
- **Report what you see**, not what it should be
- Example: "I see the line at L45 references a variable that hasn't been defined" — NOT "you need to define X"
- Only fix or suggest fixes if the user asks

### When Making Changes
- Explain the reasoning **before** executing the change
- Example: "I'm going to refactor this function because [reason]. Should I proceed?"
- Wait for confirmation unless the user explicitly asked for the action

### When Explaining Code
- Focus on what the code does, not what's "wrong" with it
- Let the user decide if changes are needed

---

## Project Structure

```
OOP/Software/          # Learning progression of OOP concepts
treacherous_beams/     # Game project using Fighter, Wizard, Archer classes
├── main_game.py
├── monster_generation.py
├── story_code.py
├── village_generation/
└── testing_files/
```

---

## Notes
- This is an educational codebase with intentional learning stages
- Some files may have incomplete implementations (marked with ACTIVITIES comments)
- Testing files explore different approaches to problems
