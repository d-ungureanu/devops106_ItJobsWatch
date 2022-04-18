pipeline {
  agent any

  stages {
    stage('Cloning the project from GitHub') {
      steps {
        git branch: 'jenkins',
        url: 'https://github.com/d-ungureanu/devops106_ItJobsWatch.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          docker.build 'devops106/itjobswatch'
        }
      }
    }
  }
}
