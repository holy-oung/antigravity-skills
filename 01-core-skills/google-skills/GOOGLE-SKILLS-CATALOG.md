# 🗺️ Google 공식 Agent Skills 전체 137개 카탈로그 (google/skills)

> **보관소 위치**: `01-core-skills/google-skills/skills/`  
> **라이선스 & 출처**: Google 공식 저장소 (Apache-2.0, 스타 19.8k, `google/skills`)  
> **핵심 특징**: Google Cloud(118종), Google Ads(14종), GA4, Gemini 등 구글 서비스 공식 연동 플레이북.  
> **주의사항**: Google Cloud 스킬만 118개에 달하므로, 평상시에는 0토큰으로 보관소에 두고 필요할 때 특정 프로젝트로 골라 담아 사용하세요.

---

## 📦 Google Ads (14종)

| 스킬명 | 주요 기능 및 설명 요약 |
| :--- | :--- |
| `data-manager-api-audience-ingestion` | Guides developers through managing (adding, removing, and clearing) audience members for Google products using the Data Manager... |
| `data-manager-api-event-ingestion` | Guides developers through implementing event and conversion ingestion to Google products using the Data Manager API /v1/events/... |
| `data-manager-api-setup` | Guides developers through client library installation and authentication setup steps for the Data Manager API. Use this skill w... |
| `google-ads-api-account-diagnostics` | Diagnoses Google Ads account performance issues such as conversion loss (value or volume), low lead flow/volume, and lost impre... |
| `google-ads-api-mcp-setup` | Guides developers through downloading, configuring, and installing the official open-source Google Ads MCP Server. Use this ski... |
| `google-ads-api-quickstart` | Guides developers through Google Ads API quickstart: credential setup, choosing from 6 client libraries/REST, configuring envir... |
| `google-mobile-ads-android-migrate-to-next-gen` | Migrates Android applications from the old, legacy Google Mobile |
| `google-mobile-ads-banner` | Provides instructions to implement, integrate, or configure Google Mobile Ads (GMA) banner ads in Android, iOS, or Unity mobile... |
| `google-mobile-ads-get-started` | Provides instructions for integrating the Google Mobile Ads (GMA) SDK. Use this skill when the user wants to get started with, ... |
| `google-mobile-ads-interstitial` | Provides instructions for implementing, integrating, or configuring Google Mobile Ads (GMA) SDK interstitial ads in Android, iO... |
| `google-mobile-ads-rewarded` | Provides instructions for implementing, integrating, or configuring Google Mobile Ads (GMA) SDK rewarded ads in Android, iOS, o... |
| `google-mobile-ads-validate` | Validates a project's Google Mobile Ads (GMA) SDK integration for iOS, Android, or Unity projects. Use when conducting a full p... |
| `ima-dai-sdk` | Integrates the Google Interactive Media Ads (IMA) Dynamic Ad Insertion (DAI) SDK into websites, web apps, mobile apps, or TV ap... |
| `ima-sdk-client-side` | Supports Interactive Media Ads (IMA) SDK. Use this skill for client-side ad insertion when you are requesting video ads for web... |

---

## 📦 Google Analytics / GA4 (2종)

| 스킬명 | 주요 기능 및 설명 요약 |
| :--- | :--- |
| `google-analytics-admin-api-basics` | Manages Google Analytics account and property settings, enables the Analytics Admin API via the Cloud CLI, lists accounts and p... |
| `google-analytics-data-api-basics` | Manages Google Analytics reporting data, enables the Analytics Data API via the Cloud CLI, and creates reports using the Google... |

---

## 📦 Google Cloud / GCP (118종)

| 스킬명 | 주요 기능 및 설명 요약 |
| :--- | :--- |
| `agent-platform-alert-configuration` | Configures best-practice alerting policies for AI agents using OpenTelemetry (OTel) metrics, generating output as Terraform (.t... |
| `agent-platform-deploy` | Deploy open models or custom weights from Model Garden to Agent Platform endpoints, check the status of an in-progress deployme... |
| `agent-platform-endpoint-management` | Manages Agent Platform serving endpoints. Use when you need to create, list, describe, update, or delete serving endpoints for ... |
| `agent-platform-eval-flywheel` | Measures and improves the quality of AI models and agents on Google Cloud using the Eval Quality Flywheel methodology. Use when... |
| `agent-platform-inference` | Connects to and performs inference with Google Cloud Agent Platform GenAI models, including First-Party Gemini models and Third... |
| `agent-platform-migrate-from-ai-studio` | Guides agents and users through migrating from Gemini API in Google AI Studio to Gemini Enterprise Agent Platform (formerly Ver... |
| `agent-platform-model-registry` | Agent Platform Model Registry Management. Use when you need to upload, list, describe, update, or delete machine learning model... |
| `agent-platform-prompt-management` | Manages and orchestrates prompts in Agent Platform. Use when you need to create, list, retrieve, version, or delete managed pro... |
| `agent-platform-rag-engine-management` | Manage and query Agent Platform RAG Engine Corpora and retrieve grounded contexts using the Google GenAI SDK. Use when listing ... |
| `agent-platform-skill-registry` | Interact with the Gemini Enterprise Agent Platform Skill Registry to create and search for available skills. Use this skill to ... |
| `agent-platform-troubleshooting` | Troubleshoots Google Cloud Gemini Enterprise Agent Platform issues (Agent Gateway, Registry, Identity, Policies, Model Armor, I... |
| `agent-platform-tuning` | Agent Platform Model Tuning. Use when you need to fine-tune open models or Gemini models using Agent Platform infrastructure. D... |
| `agent-platform-tuning-management` | Manages GenAI tuning jobs in Agent Platform. Use this to list, get, or cancel ongoing model tuning jobs. Don't use for fine-tun... |
| `alloydb-basics` | Manages clusters, instances, and backups for AlloyDB for PostgreSQL, and integrates with AlloyDB Model Context Protocol (MCP) t... |
| `application-design-center-design-deploy` | Processes GCP infrastructure design and deployment workflows within Application Design Center (ADC). Use when: - Designing GCP ... |
| `bigquery-ai-ml` | Leverages BigQuery's built-in machine learning and GenAI capabilities for advanced data analytics. Use when you need to write S... |
| `bigquery-basics` | Manages datasets, tables, and jobs in BigQuery. Use when you need to interact with BigQuery, run SQL queries, manage BigQuery r... |
| `bigquery-bigframes` | Generates Python code using BigQuery DataFrames (BigFrames), the pandas/scikit-learn-style API over BigQuery. Use when writing ... |
| `bigtable-basics` | Assists in provisioning instances/tables, designing performant schemas, and querying data in Bigtable. Use when designing Bigta... |
| `cloud-build-basics` | Teaches the fundamentals of Google Cloud Build (GCB). Covers core concepts, API enablement, console navigation to the Build His... |
| `cloud-databases-onboarding` | Guides users through discovering their database requirements, recommends a Google Cloud database based on a recommendation matr... |
| `cloud-logging-configuration-basics` | Configure single-project Google Cloud Logging: regional log buckets, log sinks, log views, restricting or hiding sensitive logs... |
| `cloud-logging-cross-project-configuration` | Configure and troubleshoot Google Cloud cross-project centralized logging and read-time aggregation. Use when: - Setting up log... |
| `cloud-logging-query-generation` | Generates Logging Query Language (LQL) queries for Google Cloud Logging from natural language. Use this skill when you need to ... |
| `cloud-monitoring-chart-generation` | Generates Google Cloud Monitoring Server-Driven UI (SDUI) Widget and XyChart Protocol Buffer textprotos from resolved PromQL or... |
| `cloud-monitoring-list-time-series-request` | Generates valid Cloud Monitoring ListTimeSeries requests and aggregation specifications from metric descriptors and resource pa... |
| `cloud-monitoring-metric-selection` | Retrieve, query, and identify relevant Google Cloud Monitoring metric descriptors for a GCP service or resource (such as Comput... |
| `cloud-monitoring-promql-query` | Generates valid PromQL queries from Cloud Monitoring metric descriptors and resource parameters. Use when asked to create, gene... |
| `cloud-run-alert-configuration` | Configures best-practice, high-signal alerting policies for Google Cloud Run resources (services, jobs, and worker pools) based... |
| `cloud-run-basics` | Manages Cloud Run services, jobs, and worker pools. Use when you need to deploy applications responding to HTTP requests (servi... |
| `cloud-sql-basics` | This file generates or explains Cloud SQL resources. Use this file when the user asks to create a Cloud SQL instance or databas... |
| `datalineage-bigquery-asset-impact-analysis` | Analyzes the downstream impact (blast radius) when a BigQuery table or view is broken, stale, or modified. Identifies all downs... |
| `datalineage-summary` | Summarizes Google Cloud Data Lineage graphs to help users debug data quality issues and understand data provenance for BQ/GCS. ... |
| `dbt-sf-to-bq-translator` | Translates Snowflake dbt SQL models to Standardized BigQuery SQL. Handles SQL compilation, Jinja macro placeholder masking, Big... |
| `detection-engineering-coverage-evaluation` | Automates the end-to-end detection engineering workflow in Google SecOps using MCP tools. Use when fetching threat intelligence... |
| `developer-device-platform-basics` | Provides guidance and instructions on managing remote devices on Developer Device Platform (DDP). Use when reserving remote And... |
| `developing-genkit-dart` | Generates code and provides documentation for the Genkit Dart SDK. Use when the user asks to build AI agents in Dart, use Genki... |
| `developing-genkit-go` | Develop AI-powered applications using Genkit in Go. Use when the user asks to build AI features, agents, flows, or tools in Go ... |
| `developing-genkit-js` | Develop AI-powered applications using Genkit in Node.js/TypeScript. Use when the user asks about Genkit, AI agents, flows, or t... |
| `developing-genkit-python` | Develop AI-powered applications using Genkit in Python. Use when the user asks about Genkit, AI agents, flows, or tools in Pyth... |
| `firebase-basics` | Provides foundational Firebase CLI setup, CLI installation, version checks (`firebase-tools@latest --version`), CLI login (incl... |
| `gcloud` | Provides safety-critical validation, guardrails, and data reduction for gcloud CLI operations across Google Cloud Platform (GCP... |
| `gemini-agents-api` | Manages custom Agent resources on Gemini Enterprise Agent Platform. Use when the user wants to programmatically create, configu... |
| `gemini-api` | Use when the user asks about using Gemini in an enterprise environment or explicitly mentions Vertex AI, Google Cloud, or Agent... |
| `gemini-interactions-api` | Guides the usage of Gemini Interactions API on Gemini Enterprise Agent Platform. Use when the user wants to use the stateful, s... |
| `gemini-live-api` | Generates a Gemini LiveAPI client service class in the user's chosen programming language. Use when the user wants to build, sc... |
| `gke-ai-troubleshooting-handle-disruption-gpu-tpu` | Diagnoses, predicts, and mitigates node disruptions during Compute Engine host maintenance and hardware or software maintenance... |
| `gke-ai-troubleshooting-jobset-interruption` | Diagnoses GKE JobSet interruptions, restarts, and preemptions for AI/ML training workloads autonomously. Use when troubleshooti... |
| `gke-ai-troubleshooting-tpu-dynamic-slices-monitoring` | Monitors, troubleshoots, and manages GKE TPU Dynamic Slices custom resources. Use when checking TPU slice lifecycle states, tro... |
| `gke-ai-troubleshooting-tpu-metrics-monitoring` | Monitors and troubleshoots GKE TPU workloads, nodes, and node pools using GKE system metrics and PromQL. Use when monitoring Te... |
| `gke-ai-troubleshooting-tpu-vbar-oom` | Diagnoses and prevents vbar_control_agent segfaults, out-of-memory (OOM) errors, and TPU device initialization failures on TPU ... |
| `gke-alert-configuration` | Configures alerting policies in Terraform for Google Kubernetes Engine (GKE) clusters, workloads, and services using PromQL and... |
| `gke-app-onboarding` | Manages GKE application onboarding, covering containerization, deployment manifests, and migration. Use when onboarding or depl... |
| `gke-backup-dr` | Configures Backup for GKE: the BackupRestore cluster addon, BackupPlan and RestorePlan resources, restore workflows, and CMEK-e... |
| `gke-basics` | Manages core GKE cluster provisioning, credentials, Autopilot vs Standard selection, and workload deployment. Use when creating... |
| `gke-batch-hpc` | Runs batch and HPC workloads on GKE, utilizing job queues and parallel processing. Use when running GKE batch jobs, configuring... |
| `gke-cluster-autoscaler` | Trigger on mention of GKE cluster autoscaler, node autoscaling, node pool auto-creation / node auto-provisioning. Provides guid... |
| `gke-cluster-creation` | Plans and executes GKE cluster creation, provisioning, and production readiness audits using pre-defined templates (Autopilot, ... |
| `gke-compute-classes` | Configures, optimizes, and troubleshoots GKE ComputeClasses. Use when configuring Spot VMs with on-demand fallback, targeting s... |
| `gke-cost-analysis` | Answer natural language questions and perform analysis on GKE cluster and workload costs using BigQuery billing exports, cost a... |
| `gke-cost-optimization` | Optimizes GKE costs, rightsizes workloads, and configures Spot VMs, CUDs, cost allocation, and resource quotas. Use when optimi... |
| `gke-custom-golden-image-discovery` | Discovers golden base images for creating GKE custom node images based on technical specifications or context clues. Use when f... |
| `gke-golden-path` | Provides GKE golden path configuration defaults, production readiness checklists, and cluster default patterns. Use when design... |
| `gke-inference` | Deploys and optimizes AI/ML inference workloads on GKE, using GPUs, TPUs, and model servers. Use when deploying GKE inference s... |
| `gke-manifest-generation` | Generates and updates secure, production-ready Kubernetes YAML manifests optimized for GKE Autopilot and GKE Standard clusters.... |
| `gke-multitenancy` | Plans and configures multi-tenancy on GKE. Covers namespace isolation, RBAC planning for teams, resource quotas, LimitRanges, n... |
| `gke-networking` | Plans, configures, and manages core GKE cluster networking. Covers private clusters, VPC-native configurations, DNS, node egres... |
| `gke-node-notready` | Diagnoses GKE nodes reporting NotReady or Unknown status by inspecting node conditions, events, kubelet/containerd logs, and no... |
| `gke-observability` | Configures GKE observability, including Cloud Logging, Cloud Monitoring, and managed Prometheus. Use when configuring GKE monit... |
| `gke-platform-security` | Plans, configures, and hardens platform-level Google Kubernetes Engine (GKE) cluster security. Covers cluster add-ons (Secret M... |
| `gke-productionize` | Orchestrates comprehensive production readiness reviews and assessments for GKE clusters and workloads across scalability, secu... |
| `gke-reliability` | Improves GKE workload reliability, using PDBs, health probes, and topology spread constraints. Use when configuring GKE workloa... |
| `gke-service-networking` | Configures GKE edge networking, traffic routing, load balancing, and private service endpoints. Use when configuring Gateway AP... |
| `gke-storage` | Manages GKE storage, including PVCs, PersistentVolumes, Filestore, and GCS FUSE. Use when configuring GKE storage, creating PVC... |
| `gke-upgrades` | Plans, executes, and validates Google Kubernetes Engine (GKE) cluster upgrades and maintenance operations for both Standard and... |
| `gke-workload-scaling` | Manages scaling for GKE workloads using HPA and VPA. Use when configuring Horizontal Pod Autoscaler (HPA), configuring Vertical... |
| `gke-workload-security` | Audits, configures, and hardens workload-level security controls for Google Kubernetes Engine (GKE) applications and namespaces... |
| `gke-workload-troubleshooting` | Diagnoses GKE workload failures (CrashLoopBackOff, OOMKilled, ImagePullBackOff, Pending, etc.) via logs and events. Use when po... |
| `google-agents-cli-onboarding` | Onboarding entrypoint for agents-cli in Agent Platform. It should be used when the user wants to "create a new agent", "develop... |
| `google-cloud-filestore-auditing` | Audits Google Cloud Filestore instances across projects for disaster recovery readiness (missing or stale backups), security ac... |
| `google-cloud-filestore-autoscale` | Inspects Google Cloud Filestore capacity and utilization, evaluates storage scaling rules, and performs capacity autoscaling (s... |
| `google-cloud-filestore-nfs-browser` | Inspects, searches, and reads files and POSIX metadata on Google Cloud Filestore (NFS) instances without local NFS client packa... |
| `google-cloud-global-frontend-configuration` | Guides agents through a 6-step discovery process to design and deploy Google Cloud global external Application Load Balancers w... |
| `google-cloud-networking-observability` | Investigates Google Cloud networking issues by analyzing logs, metrics, and diagnostics. Use when investigating VPC Flow Logs (... |
| `google-cloud-recipe-auth` | Provides expert guidance on authenticating and authorizing to Google Cloud services and APIs, covering human users, service ide... |
| `google-cloud-recipe-foundation-builder` | Deploys a baseline landing zone foundation for a Google Cloud Organization, establishing security guardrails using Organization... |
| `google-cloud-recipe-onboarding` | Guides a developer's first steps on Google Cloud, covering account creation, billing setup, project management, and deploying a... |
| `google-cloud-scc-query` | Queries and retrieves active security findings, external exposures, toxic combinations, vulnerabilities, threats, and sensitive... |
| `google-cloud-slo-alert-configuration` | Configures PromQL-based Service Level Objective (SLO) alerting policies for Google Cloud resources registered in App Hub or ind... |
| `google-cloud-solution-agentic-ai-bidirectional-streaming` | Guides agents to interactively discover customer requirements for live, bidirectional multi-agent AI systems that process conti... |
| `google-cloud-solution-agentic-ai-borderless-data-lakehouse` | Guides agents to discover requirements and design a governed, secure borderless open data lakehouse with agentic AI integration... |
| `google-cloud-solution-agentic-ai-data-science-workflow` | Designs a tailored multi-product agentic data science architecture on Google Cloud that incorporates opinionated best practices... |
| `google-cloud-solution-agentic-analytics-spark-knowledge-catalog` | Discovers requirements and generates guidance to design and deploy a governed, secure agentic-analytics solution for data that'... |
| `google-cloud-solution-architecture` | Interactively discovers requirements and designs holistic, multi-product system architectures, solution blueprints, and deploym... |
| `google-cloud-solution-build-deploy-agents` | Designs, builds, and deploys AI agents or multi-agent systems on Google Cloud. Provides an interactive workflow to gather requi... |
| `google-cloud-solution-guided-gke-ai-migration` | Guides the migration of existing AI workloads (Cloud Run, Gemini API, Gemini Enterprise Agent Platform) to self-hosted GKE infe... |
| `google-cloud-solution-hybrid-search-alloydb` | Discovers requirements and generates architectural, design, and deployment guidance for dynamic hybrid search systems by combin... |
| `google-cloud-solution-multi-agent-security` | Designs, deploys, and secures Google Cloud Agent Gateway solutions. Use when the user needs to configure multi-agent security, ... |
| `google-cloud-solution-n-tier-serverless-web-app` | Assists in designing and implementing secure n-tier serverless web applications and microservices on Google Cloud. Use when use... |
| `google-cloud-solution-rag-enterprise-search-gke-sqldb` | Discovers requirements, and generates architectural, design, and deployment guidance for a retrieval-augmented generation (RAG)... |
| `google-cloud-storage-basics` | Stores, retrieves, and manages data as objects in Cloud Storage (Google Cloud Storage, or GCS) buckets. Use when you need to in... |
| `google-cloud-storage-bucket-architect` | Creates Cloud Storage (Google Cloud Storage, or GCS) buckets. Analyzes the workload (sensitive data, media hosting, ingestion, ... |
| `google-cloud-storage-fuse` | Mounts Cloud Storage buckets as a POSIX file system with Cloud Storage FUSE (gcsfuse). Use when interacting with gcsfuse: decid... |
| `google-cloud-waf-cost-optimization` | Generates cost optimization guidance for Google Cloud workloads based on the Google Cloud Well-Architected Framework (WAF). Use... |
| `google-cloud-waf-operational-excellence` | Generates operations-focused guidance for Google Cloud workloads based on the design principles and recommendations in the Oper... |
| `google-cloud-waf-performance-optimization` | Generates performance-focused guidance for Google Cloud workloads based on the design principles and recommendations in the Per... |
| `google-cloud-waf-reliability` | Generates guidance for reliability, resilience, availability, redundancy, fault-tolerance, and disaster recovery (DR) for Googl... |
| `google-cloud-waf-security` | Generates security-focused guidance for Google Cloud workloads based on the design principles and recommendations in the Google... |
| `google-cloud-waf-sustainability` | Generates sustainability-focused guidance for Google Cloud workloads based on the design principles and recommendations in the ... |
| `iam-helper-for-policy-management` | Streamlines the creation, modification, and management of IAM allow policies (v1) and deny policies (v2). Manages access contro... |
| `iam-helper-for-policy-simulator` | Safely simulates and applies Google Cloud IAM v1 (Allow) policy changes. Uses the Policy Simulator to replay historical access ... |
| `iam-helper-for-privileged-access-management` | Manages the end-to-end lifecycle of on-demand, temporary access using Privileged Access Manager (PAM). Use when a user asks to ... |
| `iam-helper-for-troubleshooting` | Diagnoses, remediates, and manages Google Cloud Identity and Access Management (IAM) access issues. Supports two distinct opera... |
| `managed-airflow-dag-authoring` | Provides guidance for authoring Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Cove... |
| `managed-airflow-dag-troubleshooting` | Provides guidance for troubleshooting Apache Airflow DAGs (failed DAG runs and task instances) in Managed Service for Apache Ai... |
| `managed-airflow-migrations` | Provides guidance for migrating Apache Airflow DAGs in Managed Service for Apache Airflow (MSAA; formerly Cloud Composer). Cove... |
| `spanner-basics` | Assists in provisioning instances and databases, designing performant schemas, and querying data in Spanner. Use when designing... |
| `workload-manager-basics` | Use this skill to manage Google Cloud Workload Manager evaluations, rules, scanned resources, and validation results by using p... |

---

## 📦 Google Developers (2종)

| 스킬명 | 주요 기능 및 설명 요약 |
| :--- | :--- |
| `finding-google-skills` | Locates and loads the right Google product skill on demand from a remote catalog index, instead of preloading every skill. Use ... |
| `retrieving-developer-knowledge` | Searches, retrieves, and synthesizes official Google developer documentation across Google Cloud, AI/Gemini, Android, Chrome, W... |

---

## 📦 Google Identity & OAuth (1종)

| 스킬명 | 주요 기능 및 설명 요약 |
| :--- | :--- |
| `dpop-adoption` | Implement and debug OAuth 2.0 DPoP (RFC 9449) refresh token sender-constraining for WebCrypto, Node.js ES6, and browser runtime... |

---
