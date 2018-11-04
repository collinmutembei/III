pipeline {
  agent {
    docker {
      image 'hello-world'
    }

  }
  stages {
    stage('Tests') {
      steps {
        echo '[🐳] running unit tests'
        sh 'docker run -v /var/run/docker.sock:/var/run/docker.sock hello-world'
      }
    }
  }
}