stage('Build version-manager') {
    node {
        deleteDir()
        checkout scm

        docker.build('version_manager').inside {
            deleteDir()
            checkout scm

            sh """
                /src/dist/version-manager
            """
        }
    }
}
