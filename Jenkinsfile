pipeline {
    agent any 
    stages {
        stage('Testing') {
            steps {
                sh "/home/jenkins/.local/bin/pytest API1"
                sh "/home/jenkins/.local/bin/pytest API2"
                sh "/home/jenkins/.local/bin/pytest API3"
                sh "/home/jenkins/.local/bin/pytest Main"
            }
        }
        stage('Build Artifacts'){
            steps {
                sh "docker-compose build"
                sh "docker-compose push"
            }
        }
        stage ('Deploy to Prod')
        steps{
            sh "ansible-playbook -i ansible/inventory ansible/playbook.yaml"
        }

    }
}