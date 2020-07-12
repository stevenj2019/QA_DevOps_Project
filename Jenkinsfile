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
                sh "echo BUILD_NUMBER=${BUILD_NUMBER} > .env"
                sh "scp docker-compose.yml jenkins@manager:/home/jenkins/docker-compose.yaml"
                sh "scp .env jenkins@manager:/home/jenkins/.env"
                script {
                    sh """ssh -i /home/jenkins/.ssh/id_rsa  manager << EOF
                    env BUILDNUMBER=${BUILD_NUMBER}
                    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml stack
                    exit
                    EOF"""
                }
                //sh "docker stack deploy --compose-file /home/jenkins/docker-compose.yaml stack"
            }
        }
    }
}