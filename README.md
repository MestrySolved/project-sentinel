# Project Sentinel: The Future of Infrastructure is Agentic 🚀

**Infrastructure as Code just got an upgrade to Infrastructure as Agents.** Project Sentinel is an autonomous, multi-agent "Crew" designed to solve the two biggest headaches in cloud engineering: **Manual Toil** and **Budget Drift.** By orchestrating **Google Gemini**, **Claude 3.5**, and **E2B sandboxed runtimes**, this system allows users to provision complex GCP resources using natural language while maintaining 100% budget compliance—autonomously.

---

## 🏗️ System Architecture

```mermaid
graph TD
    A[User Request: 'Create GKE Cluster'] --> B{Planner: Gemini}
    B -- Checks Budget & Spec --> C[Approved Tech Spec]
    B -- Over Budget --> Z[Request Denied]
    
    C --> D[Coder: Claude]
    D -- Generates HCL Code --> E[E2B Sandbox]
    
    subgraph Execution_Sandbox
    E -- Runs 'Terraform Plan' --> F{Success?}
    F -- No: Errors Found --> D
    F -- Yes: Validated --> G[Infracost Audit]
    end
    
    G --> H[Final Approval]
    H --> I[Push to GitHub PR]
    H --> J[Store State in GCS]
