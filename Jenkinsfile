stage('Build version-manager') {
    node {
        deleteDir()
        checkout scm

        docker.image('six8/pyinstaller-alpine').inside {
            deleteDir()
            checkout scm

            sh """
                pyinstaller version-manager.spec
            """

            archiveArtifacts artifacts: 'dist/version-manager'
        }

        docker.build('version_manager').inside {
            sh """
                /src/dist/version-manager
            """
        }
    }
}
