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
        stage('Build Artifacts') {
            steps {
                sh "docker-compose build"
                sh "docker-compose push"
            }
        }
        stage('Deploy to Prod') {
            steps {
                sh "/home/jenkins/.local/bin/ansible-playbook -i ansible/inventory ansible/playbook.yaml"
                sh "scp docker-compose.yml jenkins@35.197.233.181:/home/jenkins/docker-compose.yaml"
                sh "ssh -i /home/jenkins/.ssh/id_rsa master"
                sh "docker stack deploy --compose-file docker-compose.yaml stack"
            }
        }
    }
}