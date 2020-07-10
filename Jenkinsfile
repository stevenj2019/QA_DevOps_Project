pipeline {
    agent any 
    stages {
        stage('Testing') {
            steps {
                sh "/home/jenkins/.local/bin/pytest API1"
                sh "/home/jenkins/.local/bin/pytest API2"
                sh "/home/jenkins/.local/bin/pytest API3"
                sh "py/home/jenkins/.local/bin/pytest Main"
            }
        }
        stage('build docker images'){
            steps {
                sh "docker-compose build"
            }
        }
        //stage ('docker swarm deploy')
        //steps{
        //    sh ""
        //}

    }
}