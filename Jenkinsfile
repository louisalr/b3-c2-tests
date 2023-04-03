pipeline{
    agent any
    stages{
        // Install python packages *
        stage('Python Requirements'){
            steps{
                sh 'python3 -m venv env'
                sh '. env/Scripts/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        // Run the tests
        stage('Run Pytest'){
            steps{
                sh '. env/Scripts/activate'
                sh 'cd env && pytest -v'
            }
        }
    }
}
