---
name: repo-review
description: Review local code changes or a pull request when explicitly requested; report evidence-backed defects without modifying code unless separately authorized.
---

# Repository Review

Use this skill when the user asks to review code changes, pull requests, or recent commits.

## Workflow

1. Inspect `git status` and `git diff`.
2. Read the changed files and nearby context.
3. Prioritize bugs, regressions, security risks, and missing tests.
4. Run the smallest relevant verification command when possible.
5. Report findings first, then questions, summary, and tests.

## Output Format

- Findings
- Questions
- Summary
- Tests

## Verification

Every finding should cite a concrete file path and line number.

