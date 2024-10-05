<br>

## The Amazon ECS (Elastic Container Service) settings.

* [Cluster](#amazon-ecs-cluster)
* [Logs](#logs)
* [Task Definition](#amazon-ecs-task-definition)

<br>

### Amazon ECS Cluster

A [cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html) for a group of tasks and services.[^cluster]

<br>

### Logs

Create a [CloudWatch Log Group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) for the `raw` project's task definition.

<br>

### Amazon ECS Task Definition

For an in depth understanding of task definitions study [Amazon ECS Task Definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html), and for a programmatic _task definition registration_ option study [register-task-definition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/register-task-definition.html)[^task] 

Beware:[^errors]
* --container-definitions node of a task definition template
  * 'cpu': Is optional for Fargate launch types
  * 'memory': *ditto*
* --cpu node
  * For the correct settings study [Task Size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)
* --memory node
  * Again, for the correct settings study [Task Size](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)

<br>
<br>

<br>
<br>

<br>
<br>

<br>
<br>

[^errors]: [Troubleshoot Amazon ECS task definition invalid CPU or memory errors](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-cpu-memory-error.html)
[^cluster]: [Cluster & Amazon Command Line Interface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html)
[^task]: [Task & Amazon Command Line Interface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html)
