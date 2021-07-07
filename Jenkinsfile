pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('Tests') {
      steps {
        echo '[🐳] running unit tests'
        sh 'docker run hello-world'
      }
    }
  }
}