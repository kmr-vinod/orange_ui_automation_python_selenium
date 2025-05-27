pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent any
  triggers {
    githubPush()
  }
  stages {  // Define the individual processes, or stages, of your CI pipeline
    stage('Init') {
        steps {
            echo 'Initiating...'
        }

    }
    stage('Checkout') { // Checkout (git clone ...) the projects repository
      steps {
            checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'vinod-SSH', url: 'git@github.com:kmr-vinod/orange_ui_automation_python_selenium.git']])
      }
    }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
            powershell 'python.exe -m pip install --upgrade pip'
            powershell 'pip install -r requirements.txt'
        }
      }
    }
//     stage('Linting') { // Run pylint against your code
//       steps {
//         script {
//           powershell 'pylint **/*.py'
//         }
//       }
//     }
    stage('Run tests') { // Run pylint against your code
      steps {
        script {
            powershell 'behave Tests/Features'
        }
      }
    }
}

  post {
    failure {
      script {
           echo "Failed"
    }
  }
}
}
