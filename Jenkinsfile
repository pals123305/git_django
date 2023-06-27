/* Jenkinsfile (Declarative Pipeline) */
/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    tools {
        // Specify the Python installation defined in Jenkins Tools
        python 'Python3.10.6'
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
