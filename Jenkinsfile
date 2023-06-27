/* Jenkinsfile (Declarative Pipeline) */
/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    tools {
        // Define the Python installation
        python 'Python3.9' // Replace with the name of your Python installation in Jenkins
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/pals123305/git_django.git'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python manage.py test'
            }
        }
        
        stage('Build and Deploy') {
            steps {
                sh 'python manage.py collectstatic --noinput'
                sh 'python manage.py migrate'
                sh 'python manage.py runserver'
            }
        }
    }
}
