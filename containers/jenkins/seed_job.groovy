def create_pipeline_job = { pipeline -> 
	pipelineJob(pipeline.name) {
	  definition {
		cpsScm {
		  scm {
			git {
			  remote { url(pipeline.repo) }
			  branches('master')
			  scriptPath('Jenkinsfile')
			  extensions { } 
			}
		  }
		}
	  }
	}
}

pipelines = [
	[
		'name': 'razorchess',
		'repo':'https://github.com/tlewis11/razorchess.git'
	],
]

pipelines.each{ pipeline ->
	create_pipeline_job pipeline
}
