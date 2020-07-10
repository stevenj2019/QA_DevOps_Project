pipeline {
    agent any 
    stages {
        stage('Testing')
        steps {
            sh "pytest API1"
            sh "pytest API2"
            sh "pytest API3"
            sh "pytest Main"
        }
        stage('build docker images')
        steps {
            sh "docker-compose build"
        }
        //stage ('docker swarm deploy')
        //steps{
        //    sh ""
        //}
        
    }
}