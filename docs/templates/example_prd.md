# Example PRD: Task Master Integration Bootstrap

## 1. Overview
- Title: Integrate Task Master PRD Workflow
- Owner: Product/Eng
- Date: 2025-08-04
- Version: 0.1.0
- Status: Approved

## 2. Problem Statement
Contributors lack a clear PRD template and workflow to generate actionable tasks via Task Master, slowing onboarding and planning.

## 3. Goals
- G1: Provide a standard PRD template and an example to copy.
- G2: Document how to parse a PRD into tasks.json using Task Master.
- G3: Ensure the output is actionable for expansion and task file generation.

## 4. Non-Goals
- NG1: Redefine existing development or release processes.
- NG2: Replace ADRs or other templates.

## 5. Stakeholders
- Product: PM team
- Engineering: Dev leads, contributors
- QA: QA lead
- Others: Docs maintainers

## 6. User Personas / Target Audience
- New contributors needing a repeatable path from idea to tasks.
- Maintainers enforcing consistent planning.

## 7. Assumptions
- Task Master CLI or MCP is available and configured.
- Repo will store PRDs in docs/prd.

## 8. Requirements
### 8.1 Functional Requirements
- FR-1: As a maintainer, I can copy the example PRD and quickly adapt it for my project.
- FR-2: As a contributor, I can run a single command to parse the PRD into tasks.json.
- FR-3: As a team, we can expand tasks and generate task markdown files.

### 8.2 Non-Functional Requirements
- NFR-1: Documentation is concise and copy-paste friendly.
- NFR-2: Commands work cross-platform (macOS/Linux; Windows via Git Bash).

### 8.3 API/Interface Requirements
- CLI usage: task-master parse-prd, analyze-complexity, expand, generate.
- MCP usage: parse_prd, analyze_project_complexity, expand_all, generate.

## 9. Constraints
- Must align with Task Master tool/CLI expectations.
- Use markdown for templates and PRD.

## 10. Dependencies
- Task Master CLI (npm) or MCP tools via Roo Code.
- .taskmaster/config.json configured models and provider keys where applicable.

## 11. Milestones and Timeline
- M1: Templates merged (Day 0).
- M2: Docs updated (Day 0).
- M3: First PRD parsed and tasks generated (Day 1).

## 12. Acceptance Criteria
- AC-1: Template and example available under docs/templates.
- AC-2: README and onboarding mention PRD workflow and commands.
- AC-3: Running parse-prd on a filled PRD yields .taskmaster/tasks/tasks.json.

## 13. Risks and Mitigations
- R-1: Missing API keys for AI operations — Mitigation: Document .env and .taskmaster/config.json setup.
- R-2: Overly long PRDs leading to noisy tasks — Mitigation: Keep PRD scoped and focused on goals and acceptance criteria.

## 14. Open Questions
- Q-1: Should we enforce a maximum PRD length for parse-prd?
- Q-2: Where do we store historical PRDs (archive)?

## 15. Rollout Plan
- Provide templates and docs.
- Encourage teams to create docs/prd/current_prd.md from template.

## 16. Metrics & Success Indicators
- Number of teams generating tasks via parse-prd.
- Time from idea to initial task breakdown.

## 17. Appendix
- ADRs: docs/adr/
- Templates: docs/templates/

---

How to use:
1) Copy this file to docs/prd/current_prd.md and customize.
2) Parse into tasks:
   - CLI:
     - npm install -g task-master-ai
     - task-master parse-prd docs/prd/current_prd.md -o .taskmaster/tasks/tasks.json -n 8 -f
   - MCP (Roo Code):
     - parse_prd:
       - input: docs/prd/current_prd.md
       - output: .taskmaster/tasks/tasks.json
       - numTasks: 8
       - force: true
3) Next steps:
   - task-master analyze-complexity -r
   - task-master expand --all -r
   - task-master generate