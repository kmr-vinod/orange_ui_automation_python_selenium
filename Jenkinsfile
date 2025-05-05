pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
//     ansiColor('xterm') // Enable colors in terminal
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent none
//   stages {  // Define the individual processes, or stages, of your CI pipeline
//     stage('Checkout') { // Checkout (git clone ...) the projects repository
//       steps {
//         script {
//             git branch: "main", credentialsId: 'b17d92b0-951b-4177-aa88-8627765ea6de', url: "git@github.com:kmr-vinod/orange_ui_automation_python_selenium.git"
//             }
//       }
//     }
    stage('Setup') { // Install any dependencies you need to perform testing
      steps {
        script {
          sh """
          pip install -r requirements.txt
          """
        }
      }
    }
    stage('Linting') { // Run pylint against your code
      steps {
        script {
          sh """
          pylint **/*.py
          """
        }
      }
    }
    stage('Run tests') { // Run pylint against your code
      steps {
        script {
          sh """
          behave Tests/Features/
          """
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
