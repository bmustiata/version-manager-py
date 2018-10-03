properties([
    pipelineTriggers([
        upstream(
            threshold: 'SUCCESS',
            upstreamProjects: '/build-system/germaniumhq-python-build-system'
        )
    ])
])

germaniumPyExePipeline(
    binaries: [
        "Lin 64": [
            exe: "/src/dist/version-manager",
            dockerTag: "version_manager",
            dockerPublish: true,
            dockerToolContainer: true
        ]
    ]
)

