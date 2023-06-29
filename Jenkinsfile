pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }
        stage('Install virtualenv') {
            steps {
                sh 'pip install virtualenv'
            }
        }
        
        stage('Setup virtual environment') {
            steps {
                    sh 'virtualenv venv'
            }
        }
        
        stage('Activate virtual environment') {
            steps {
                sh '. venv/bin/activate'
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Python version') {
            steps {
                sh 'python3 --version'
            }
        }
       
    }
}
