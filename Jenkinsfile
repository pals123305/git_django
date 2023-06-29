pipeline {
    agent any
    
    stages {
        stage('Clone repository') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }
        stage('Install virtualenv') {
            steps {
                echo '************installing environment***************...'
                sh 'pip install virtualenv'
            }
        }
        
        stage('Setup virtual environment') {
            steps {
                    echo '************create environment***************...'
                    sh 'virtualenv venv'
            }
        }
        
        stage('Activate virtual environment') {
            steps {
                echo '************activate environment***************...'
                sh '. venv/bin/activate'
            }
        }
        
        stage('Install dependencies') {
            steps {
                echo '************installing dependency***************...'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Python version') {
            steps {
                echo '************print version***************...'
                sh 'python3 --version'
            }
        }
       stage('Run Ansible playbook') {
            steps {
                script {
                    echo '************run scripts***************...'
                    sh 'ansible-playbook -i inventories/inventory.ini create_file.yaml'
                }
            }
        }
    }
}
