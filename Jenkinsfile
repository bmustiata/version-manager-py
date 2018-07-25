properties([
    pipelineTriggers([
        upstream(
            threshold: 'SUCCESS',
            upstreamProjects: '/build-system/germaniumhq-python-build-system'
        )
    ])
])

stage('Build version-manager') {
    node {
        ansiColor('xterm') {

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
}

stage('Publish docker image') {
    node {
        dpush 'version_manager'
    }
}
