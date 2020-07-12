pipeline {
    agent any 
    String command = 'export BUILD_NUMBER = ' + System.getenv("BUILD_NUMBER")
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
                sh "scp docker-compose.yml jenkins@manager:/home/jenkins/docker-compose.yaml"
                script {
                    sh """ssh -i /home/jenkins/.ssh/id_rsa -o SendEnv=${BUILD_NUMBER} manager << EOF
                    ${command}
                    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml stack
                    exit
                    EOF"""
                }
                //sh "docker stack deploy --compose-file /home/jenkins/docker-compose.yaml stack"
            }
        }
    }
}