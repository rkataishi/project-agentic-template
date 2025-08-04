# Product Requirements Document (PRD) Template

Use this template to define product scope clearly and generate actionable tasks with Task Master. Keep sections concise and scoped for implementation.

## 1. Overview
- Title:
- Owner:
- Date:
- Version:
- Status: Draft / Review / Approved

## 2. Problem Statement
- What problem are we solving?
- Who is affected and how?

## 3. Goals (What success looks like)
- G1:
- G2:
- G3:

## 4. Non-Goals (Out of scope)
- NG1:
- NG2:

## 5. Stakeholders
- Product:
- Engineering:
- Design:
- QA:
- Others:

## 6. User Personas / Target Audience
- Persona A: brief description, needs
- Persona B: brief description, needs

## 7. Assumptions
- A1:
- A2:

## 8. Requirements
### 8.1 Functional Requirements
- FR-1: As a <role>, I can <action> so that <outcome>.
- FR-2:
- FR-3:

### 8.2 Non-Functional Requirements
- NFR-1: Performance (e.g., P95 < 250ms for endpoint X)
- NFR-2: Security/Compliance (e.g., OAuth2, audit logs)
- NFR-3: Reliability/Availability (e.g., SLOs)

### 8.3 API/Interface Requirements (if applicable)
- Endpoint(s), request/response schema, error codes
- UI views/components and states
- CLI/Job contracts

## 9. Constraints
- Tech stack constraints (libraries, languages, frameworks)
- Platform constraints (mobile/web/desktop)
- Legal/compliance constraints

## 10. Dependencies
- Internal systems/services
- External vendors/APIs
- Feature flags/rollout

## 11. Milestones and Timeline
- M1: Scope finalized (date)
- M2: Prototype/Spike (date)
- M3: MVP (date)
- M4: GA (date)

## 12. Acceptance Criteria
- AC-1:
- AC-2:
- AC-3:
- Definition of Done: code, tests, docs, monitoring, alerts

## 13. Risks and Mitigations
- R-1: Risk ... — Mitigation ...
- R-2: Risk ... — Mitigation ...

## 14. Open Questions
- Q-1:
- Q-2:

## 15. Rollout Plan
- Launch strategy
- Feature flags/gradual rollout
- Rollback plan

## 16. Metrics & Success Indicators
- Activation/Usage metrics
- Quality metrics (bug rate, error budget)
- Business metrics (conversion, retention)

## 17. Appendix
- Links to ADRs, designs, diagrams, spikes
- Glossary

---

How to use with Task Master:
1) Fill this template and save as `docs/prd/current_prd.md`.
2) Parse into tasks:
   - CLI:
     - `npm install -g task-master-ai` (or use `npx task-master-ai ...`)
     - `task-master parse-prd docs/prd/current_prd.md -o .taskmaster/tasks/tasks.json -n 8 -f`
   - MCP (Roo Code): Use the `parse_prd` tool with:
     - input: `docs/prd/current_prd.md`
     - output: `.taskmaster/tasks/tasks.json`
     - numTasks: e.g., `8`
     - force: `true`
3) Then run:
   - `task-master analyze-complexity -r`
   - `task-master expand --all -r`
   - `task-master generate`