pipeline {
    agent any
    stages {
        stage("checkout Code") {
            steps {
                git url:'https://github.com/danish-73/jenkins.git', branch:'main'
            }
        }
        stage("Build Docker Image") {
            steps{
                sh'docker build -t myapp .'
            }
        }
        stage("Create Container") {
            steps{
            sh'docker run -d -p 8501:8501 myimage'
            }  
        }
    }
}
