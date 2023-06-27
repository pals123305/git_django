pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                checkout scm
            }
        }
        
        stage('Setup virtual environment') {
            steps {
                withPythonEnv('python3') {
                    sh 'python -m venv venv'
                }
            }
        }
        
        stage('Activate virtual environment') {
            steps {
                sh 'source venv/bin/activate'
            }
        }
        
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Run tests') {
            steps {
                sh 'python manage.py test'
            }
        }
        
        // Add more stages as needed
        
        stage('Clean up') {
            steps {
                sh 'deactivate' // Deactivate the virtual environment
            }
        }
    }
}
