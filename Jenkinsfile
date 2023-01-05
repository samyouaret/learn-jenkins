pipeline {
        agent {
            label 'my-agent'
        }

        stages {

            stage('build'){
                steps {
                    echo 'Building'
                }
            }

            stage ('test'){
                steps{
                    echo 'Testing'
                }
            }

            stage ('deploy'){
                steps{
                    echo 'Deploying'
                }
            }
        }
}