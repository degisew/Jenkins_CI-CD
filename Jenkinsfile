pipeline {
    agent any
    triggers {
        pollSCM('* * * * *')  // Poll every minute
    }
    stages {
        stage("Clone Repo") {
            steps {
                // Clone the GitHub repository
                git url: 'https://github.com/degisew/Jenkins_CI-CD.git', branch: 'main'
            }
        }
        stage("Install Dependencies") {
            steps {
                script {
                    // Create a virtual environment
                    sh 'python3 -m venv ~/.virtualenvs/jenkins'
                    
                    // Activate the virtual environment and install dependencies
                    sh '. ~/.virtualenvs/jenkins/bin/activate && pip install -r requirements.txt'
                }
            }
        }
        stage("Run Tests") {
            steps {
                script {
                    // Run tests
                    sh '. ~/.virtualenvs/jenkins/bin/activate && pytest tests/'
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Pipeline succeeded.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
