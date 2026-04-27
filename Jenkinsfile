pipeline {
    agent any

    stages {

        stage('Clone Code') {
            steps {
                git 'https://github.com/your-username/event-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t event-app .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest || true'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}