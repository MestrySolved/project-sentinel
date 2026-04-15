# Project Sentinel: The Future of Infrastructure is Agentic 🚀

**Infrastructure as Code just got an upgrade to Infrastructure as Agents.** Project Sentinel is an autonomous, multi-agent "Crew" designed to solve the two biggest headaches in cloud engineering: **Manual Toil** and **Budget Drift.** By orchestrating **Google Gemini**, **Claude 3.5**, and **E2B sandboxed runtimes**, this system allows users to provision complex GCP resources using natural language while maintaining 100% budget compliance—autonomously.

---

## 🏗️ System Architecture

```mermaid
graph TD
    %% Input and Analysis Phase
    A --> B{Architect: Gemini}
    B -- Ingests Requirements & Log Data --> C
    B -- Defines Data Storage Strategy --> GCS_Logs
    
    %% Generation Phase
    C --> D
    D -- Generates HCL: IAM, Svc Acct, GKE, Namespaces --> E
    
    %% Validation & Version Control
    subgraph Execution_Sandbox
    E -- Runs 'Terraform Init & Plan' --> F{Validation?}
    F -- Errors Found --> D
    F -- Success --> GH
    end
    
    %% Provisioning Phase
    GH -- Push Code & Open PR --> GPR
    GPR -- Human Approval Gate --> TA
    
    %% GCP Resource Layer
    subgraph Google_Cloud_Platform [Google Cloud Platform]
    TA --> IAM
    IAM --> GKE[GKE Cluster & Namespaces]
    TA --> ST
    end
    
    %% CI/CD and Monitoring Layer
    GKE --> CF[Codefresh Pipeline]
    CF -- Blue-Green Deployment --> PROD
    
    PROD --> MON{Monitoring Agent}
    MON -- Fetches Status API --> GRAF
    GRAF -- Alert/Health Output --> A
