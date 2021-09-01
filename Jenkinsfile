pipeline {
    agent {
        docker {
            image 'python:3.9.6-alpine3.14'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'cd app_python && pip install -r requirements.txt -r dev-requirements.txt'
            }
        }
        stage('Lint') {
            steps {
                sh 'pylint --rcfile app_python/.pylintrc app_python/'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
    }
}