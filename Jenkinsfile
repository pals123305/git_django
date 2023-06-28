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
                sh '/var/lib/jenkins/.local/bin/virtualenv venv'
            }
        }
        
        stage('Setup virtual environment') {
            steps {
                    sh 'virtualenv venv'
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
