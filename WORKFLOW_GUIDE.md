# 🧭 FFLIQ Workflow Guide (GitLab + AI Agent Tasking)

## 🚀 Automated Issue and Commit Workflow

- **Create issues without labels** to avoid API errors.
- **Always fetch the issue number after creation** and reference it in all related commits (e.g., `Closes #7`).
- **Close duplicate or outdated issues** to keep the tracker clean.
- **Update CHANGELOG.md** when merging significant changes.
- **Document all lessons learned** in this WORKFLOW_GUIDE.md and PLANNING.md for future contributors and agents.

---

This document defines how contributors (human or AI) should manage project work using GitLab Issues. It ensures consistent task tracking, context-aware coding, and a clean handoff between developers, AI agents (e.g., Windsurf), and reviewers.

---

## 📌 Core Principles

- **Everything starts with an issue**. No PR/MR should exist without a linked issue.
- **All tasks must be discoverable in GitLab Issues** and traceable to either `PLANNING.md` or `REFERENCE.md`.
- **Windsurf and other AI tools should be guided by issue labels, descriptions, and linked context.**

---

## 🗂️ GitLab Issue Structure

### ✅ Titles
Follow a verb-based naming convention:
```
feat: Add waiver wire alert backend service
fix: Prevent null lineup crash
refactor: Separate AI vector store abstraction
```

### 📄 Descriptions
Use this template:
```
### Summary
Concise summary of what this issue is about.

### Type
[ ] Feature
[ ] Bug
[ ] Chore
[ ] Refactor
[ ] Test
[ ] Documentation

### Linked Docs
- PLANNING.md section: [e.g., AI Assistant]
- Reference.md: [#3 Technical Architecture]

### Requirements
- List exact outputs required (files, endpoints, UI elements, tests)
- Acceptance criteria

### Notes for AI Tools
(Optional)
Specific guidance for AI agents like coding conventions, libraries to use/avoid, or formatting expectations.
```

---

## 🏷️ Labeling Conventions

| Label         | Purpose                                 |
|---------------|------------------------------------------|
| `mvp`         | Must-ship in MVP                        |
| `post-mvp`    | Future phase features                   |
| `ai-generated`| Created by an AI assistant              |
| `blocked`     | Waiting on another task or decision     |
| `needs-review`| PR/MR needs human code review           |
| `good first`  | Suitable for new contributors/agents    |
| `backend`     | Backend-specific task                   |
| `frontend`    | Frontend-specific task                  |
| `ai/llm`      | Related to AI/LLM integration            |
| `infra`       | DevOps / CI / Docker / Environment       |

---

## 📎 Best Practices for AI Tools

### 🔁 Session Startup
- **Always read `PLANNING.md` and current issue description.**
- If uncertain about a feature, look for matching sections in `REFERENCE.md`.
- Ask clarifying questions in issue comments if context is unclear.

### 🧱 Code Contribution
- Follow naming, type, and folder structure conventions from `PLANNING.md`
- Annotate files with file paths in comments.
- Add unit tests and follow documented testing practices.
- Update `CHANGELOG.md` if required.

### 📌 Issue Workflow
1. **Assign yourself** to the issue.
2. Move issue to **"In Progress"**.
3. When complete, open a **Merge Request (MR)**.
4. Link the MR to the issue (`Closes #issueID`).
5. Label the MR with `needs-review` and applicable tech tags.
6. Human must approve MR before merge to `main`.

---

## 🗃️ Workflow Files

| File              | Purpose                                          |
|-------------------|--------------------------------------------------|
| `PLANNING.md`     | Task roadmap + architecture + naming conventions |
| `REFERENCE.md`    | Longform strategy and system vision             |
| `CHANGELOG.md`    | Manual changelog (updated on PR merge)         |
| `.windsurfrules`  | Guidelines for Windsurf AI agent                |

---

## 🧠 Notes for Human Devs
- Review and edit AI-generated GitLab issues for completeness.
- Use this format yourself when writing new issues.
- Prioritize `mvp` issues until the MVP is feature-complete.
- Encourage AI tools to add test coverage for all logic.

---

## 📝 Commit Message Format

We follow the Conventional Commits specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

Types include:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code changes that neither fix a bug nor add a feature
- `test`: Adding or correcting tests
- `chore`: Changes to the build process or auxiliary tools

Examples:
```
feat(auth): implement user login functionality
fix(api): correct off-by-one error in points calculation
docs: update installation instructions
```

---

## 🔍 Code Review Guidelines

- All code, whether human or AI-generated, must be reviewed
- Check for:
  - Adherence to the project architecture and conventions
  - Security vulnerabilities and performance issues
  - Test coverage (minimum 80% for critical paths)
  - Documentation completeness
  - Type safety (TypeScript/Python type hints)

---

> 📎 For reference, see: `PLANNING.md > Feature Checklist (MVP)` for current priorities.

This guide should be updated as workflow conventions evolve.
