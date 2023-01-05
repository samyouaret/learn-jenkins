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

            stage('Build'){
                steps {
                    pip install -r requirements.txt
                }
            }

            stage ('Test'){
                steps {
                    python3 app.py --name="Jenkins"
                }
            }

            stage ('deploy'){
                steps{
                    echo 'Deploying'
                }
            }
        }
}