pipeline {
        agent {
            node {
                label 'python-docker-agent'
            }
        }
        triggers{
            pollSCM('*/5 * * * *')
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