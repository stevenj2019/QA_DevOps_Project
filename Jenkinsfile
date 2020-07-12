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
                sh "scp docker-compose.yml jenkins@manager:/home/jenkins/docker-compose.yaml"
                sh "ssh -i /home/jenkins/.ssh/id_rsa master << EOF
                docker service create --replicas 3 --name main --update-delay 5s sjohnson2019/main:${BUILD_NUMBER}
                docker service create --replicas 2 --name api_1 --update-delay 5s sjohnson2019/api_1:${BUILD_NUMBER}
                docker service create --replicas 2 --name api_2 --update-delay 5s sjohnson2019/api_2:${BUILD_NUMBER}
                docker service create --replicas 2 --name api_3 --update-delay 5s sjohnson2019/api_3:${BUILD_NUMBER}
                EOF"
            }
        }
    }
}