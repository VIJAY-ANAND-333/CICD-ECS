pipeline {
    agent any

    environment {
        AWS_ACCOUNT_ID = ''
        AWS_REGION = 'us-east-1'
        ECR_REPO = 'jenkins'
        CLUSTER_NAME = 'jenkins'
        SERVICE_NAME = 'jenkins'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'jenkins',
                credentialsId: '',
                url: ''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${ECR_REPO}:latest .'
            }
        }

        stage('Push to ECR') {
            steps {
                sh '''
                aws ecr get-login-password --region ${AWS_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com
                docker tag ${ECR_REPO}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
                docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}:latest
                '''
            }
        }

        stage('Deploy to ECS') {
            steps {
                sh '''
                aws ecs update-service --cluster ${CLUSTER_NAME} --service ${SERVICE_NAME} --force-new-deployment --region ${AWS_REGION}
                '''
            }
        }
    }
}