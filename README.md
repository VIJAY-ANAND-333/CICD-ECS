# End-to-End CI/CD Pipeline with Jenkins and AWS ECS

Automated deployment of a Flask app to AWS ECS with Jenkins CI/CD and Datadog monitoring.

## Overview
- **Jenkins**: Builds and deploys a Dockerized Flask app via a pipeline triggered by a Bitbucket webhook.
- **AWS ECS**: Runs the app in a cluster with an ELB and SSL (ACM).
- **Monitoring**: Datadog tracks logs and metrics via CloudWatch and Lambda integration.
- **Purpose**: Seamless, enterprise-grade app deployment with real-time observability.

## Tech Stack
- Jenkins
- Docker
- AWS (ECS, ECR, ELB, ACM, CloudWatch, Lambda)
- Bitbucket (Webhook)
- Datadog
- Python (Flask)

## Features
- **Webhook Automation**: Code push to Bitbucket triggers Jenkins pipeline.
- **Load-Balanced ECS**: ELB with SSL ensures secure, scalable access.
- **Advanced Monitoring**: Datadog dashboards via CloudWatch-Lambda integration.

## Setup Instructions
### Prerequisites:
- Jenkins server, AWS CLI, Docker installed.
- Bitbucket repo with webhook to Jenkins.
- Datadog account with Lambda integration.
1. **App**:
   - Build: `docker build -t vj-flask-app .`
2. **Jenkins**:
   - Pipeline: `Jenkinsfile` builds, pushes to ECR, updates ECS service.
   - Webhook: Configured in Bitbucket to trigger on push.
3. **ECS**:
   - Cluster, task definition, service with ELB (Fargate).
4. **Monitoring**:
   - Lambda: Sends CloudWatch logs/metrics to Datadog.
5. **Verify**:
   - Check ECS service logs or access the ELB URL.

## Outcome
- Fully automated deployments with zero downtime.
- Real-time monitoring via Datadog for production reliability.

---
Built by Vijay Anand M | [GitHub](https://github.com/VIJAY-ANAND-333) | [Email](mailto:vijayanandm333@gmail.com)
