stage('Build version-manager') {
    node {
        deleteDir()
        checkout scm

        docker.build('version_manager').inside {
            deleteDir()
            checkout scm

            sh """
                /src/dist/version-manager --all
            """

            archiveArtifacts artifacts: "/src/dist/version-manager"
        }

        dockerRm containers: ['version_manager']
        dockerRun image: 'version_manager',
            name: 'version_manager',
            command: 'ls'
    }
}
