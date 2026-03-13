```markdown
# Product Requirements Document (PRD): Project Sentinel

**Status:** Draft / Version 1.0  
**Target Role:** AI Product Manager / Technical PM

## 1. Problem Statement
Cloud infrastructure management currently suffers from "The DevOps Gap":
* **Manual Bottlenecks:** Engineers spend hours debugging Terraform syntax and checking spreadsheets.
* **Cloud Waste:** 30% of cloud spend is wasted due to over-provisioning and lack of pre-deployment cost controls.

## 2. Product Vision
To provide a "Self-Driving" infrastructure experience where natural language is converted into cost-optimized, validated, and production-ready cloud resources.

## 3. User Stories
| As a... | I want to... | So that... |
| :--- | :--- | :--- |
| Developer | Request a GKE cluster via chat | I don't have to learn complex HCL syntax. |
| FinOps Manager | Set a $50/mo limit on new resources | I can prevent surprise cloud bills. |
| DevOps Lead | Have AI self-correct its own errors | My team stops spending time on minor syntax debugging. |

## 4. Functional Requirements
* **FR1:** System must parse natural language and identify the required GCP resource type.
* **FR2:** System must perform an `infracost` audit before executing `terraform apply`.
* **FR3:** System must retry code generation at least 3 times if validation fails (Self-Healing).
* **FR4:** All state files must be stored in a secure GCS bucket, not locally.

## 5. Success Metrics (KPIs)
* **Reduction in MTTP (Mean Time to Provision):** Target < 5 minutes (vs. 45 mins manual).
* **Budget Compliance:** 100% of deployed resources must be within the user-defined cost limit.
* **Error Rate:** < 5% failure rate on first-attempt "Apply" after AI self-correction.
