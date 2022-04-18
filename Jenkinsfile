pipeline {
  agent any

  stages {
    stage('Cloning the project from GitHub') {
      steps {
        git branch: 'main',
        url: 'https://github.com/d-ungureanu/devops106_ItJobsWatch.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          docker.build 'devops106/ItJobsWatch'
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        script {
          docker.withRegistry('', '	docker_hub_credentials')
        }
      }
    }
  }
}
