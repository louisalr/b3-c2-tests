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
                sh 'cd env && python3 -m tests.test_calculator'
            }
        }
    }
    post {
        failure {
            discordSend description: "Failed Pipeline ${currentBuild.fullDisplayName}",
                        link: env.BUILD_URL
                        title: env.JOB_NAME
                        webhookURL : "https://discord.com/api/webhooks/1092702382858707024/ijtbk1G6fJnK6HttmfYNb-MAlB-74ioPdEvJlacNk1UtvtMVGaIj938Cxt9Xq0X2-ekp"

        }
    }

}
