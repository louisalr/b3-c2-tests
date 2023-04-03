pipeline{
    agent any
    stages{
        // Install python packages *
        stage('Ls file'){
            steps{
                sh 'ls -l'
            }
        }
        stage('Python Requirements'){
            steps{
                sh 'python3 -m venv env'
                sh '. env/bin/activate'
                sh 'cd env/'
                sh 'pip install -r requirements.txt'
            }
        }
        // Run the tests
        stage('Run Pytest'){
            steps{
                sh '. env/bin/activate'
                sh 'cd env && pytest -v'
            }
        }
    }
}
