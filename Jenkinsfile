pipline {
agent any
environment {}
triggers{
  pollSCM('* * * * *')  // Optional: Polling as a fallback
}
stages{
  stage("Clone Repo") {
    steps {
      // Clone the GitHub repository
      git url: 'https://github.com/degisew/Jenkins_CI-CD.git', branch: 'main'
    }
  }
  stage("Install Dependencies") {
    steps {
      script {
        python venv ~/.virtualenvs/jenkins
        source ~/.virtualenvs/jenkins/bin/activate
        sh 'pip install -r requirements.txt'
      }
    }
  }
 stage("Run Tests") {
   steps{
    script{
      sh 'pytest tests/'
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