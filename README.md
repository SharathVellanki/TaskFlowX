# TaskFlowX

An event-driven workflow automation system built with Angular, FastAPI, Redis, and AWS — optimized for real-time task execution, streaming pipelines, and observability.

## Table of Contents
- [Introduction](#introduction)
- [Background](#background)
- [Objective](#objective)
- [Approach](#approach)
- [Significance](#significance)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Key Outcomes](#key-outcomes)

---

## Introduction
TaskFlowX is a distributed workflow automation platform enabling the creation, chaining, and execution of tasks in real time. It supports both local and cloud execution, with built-in observability and a streaming dashboard for logs and metrics.

---

## Background
Modern automation requires low latency, scalability, and transparency. TaskFlowX uses Redis Pub/Sub, AWS services, and an Angular-based dashboard to achieve sub-150ms latency while processing thousands of events per minute.

---

## Objective
The primary goal is to deliver a reliable, event-driven automation system that integrates with cloud services, supports real-time monitoring, and scales for high-throughput workflows.

---

## Approach
- Event-driven execution using Redis Pub/Sub  
- AWS integrations: DynamoDB for state storage, Lambda for execution, SQS for durable queueing  
- Angular dashboard for real-time workflow visualization and alerts  
- JWT-secured FastAPI backend  

---

## Significance
TaskFlowX powers high-throughput pipelines, enabling real-time decision-making and reducing operational delays through instant visibility into task and workflow states.

---

## Features
- Task & workflow management with status tracking  
- Event-driven execution with Redis Pub/Sub  
- AWS-based persistence and serverless task execution  
- Real-time dashboard for logs, metrics, and alerts  
- Observability with Prometheus and Grafana  

---

## Tech Stack
**Frontend:** Angular 17 (TypeScript), Tailwind CSS, ngx-charts  
**Backend:** FastAPI (Python), PostgreSQL, Redis Pub/Sub  
**Cloud:** AWS DynamoDB, AWS Lambda, AWS SQS  
**Monitoring:** Prometheus, Grafana  
**Infra/CI:** Docker, GitHub Actions  

---

## Key Outcomes
- Processed 1,200+ events/min with p95 latency under 150ms  
- Delivered a streaming-style UI visualizing workflows, logs, and metrics in real time
