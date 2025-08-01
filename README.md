TaskFlowX
An event-driven workflow automation system built with Angular (TypeScript), FastAPI, Redis, and AWS (DynamoDB, Lambda, SQS) — optimized for real-time task execution, streaming pipelines, and observability.

🔧 Tech Stack
Frontend: Angular 17 (TypeScript), Tailwind CSS, ngx-charts
Backend: FastAPI (Python), PostgreSQL, Redis Pub/Sub
Cloud: AWS DynamoDB, AWS Lambda, AWS SQS
Infra/DevOps: Docker, GitHub Actions
Monitoring: Prometheus, Grafana


✅ Features
🔗 Task & Workflow Management – Create tasks with statuses (pending, running, success, fail) and chain them into workflows.

⚡ Event-Driven Execution – Redis Pub/Sub for real-time task execution.


🛠️ AWS Integrations –

DynamoDB for workflow state storage

Lambda for execution of tasks

SQS for reliable, durable queuing

📊 Streaming Dashboard – Angular frontend with task logs, execution metrics, and failure alerts.

🔐 Auth Ready – JWT-secured API endpoints.

📈 Observability – Real-time metrics, Redis logs, and Prometheus monitoring.



📈 Key Outcomes
✅ Processed 1,200+ events/min with p95 latency <150ms using Redis + AWS queueing.
✅ Delivered a streaming-style UI that visualizes workflows, logs, and metrics in real time.

