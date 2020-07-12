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
                sh "echo BUILD_NUMBER=${BUILD_NUMBER}\n > .env"
                sh "echo PROD_SKEY=${PROD_SKEY}\n > .env"
                sh "echo PROD_DB_URI=${PROD_DB_URT}\n > .env"
                sh "scp docker-compose.yml jenkins@manager:/home/jenkins/docker-compose.yaml"
                sh "scp .env jenkins@manager:/home/jenkins/.env"
                script {
                    sh """ssh -i /home/jenkins/.ssh/id_rsa  manager << EOF
                    env BUILD_NUMBER=${BUILD_NUMBER}
                    export BUILD_NUMBER=${BUILD_NUMBER}
                    export PROD_KEY=${PROD_SKEY}
                    export PROD_DB_URI=${PROD_DB_URI}
                    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml stack
                    exit
                    EOF"""
                }
                //sh "docker stack deploy --compose-file /home/jenkins/docker-compose.yaml stack"
            }
        }
    }
}