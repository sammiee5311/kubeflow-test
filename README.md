# kubeflow-test

## How to use it
- Add github secrets
    - `COOKIES`: kubeflow website cookie
    - `NAMESPACE`: kubeflow namespace
    - `URI`: kubeflow uri
    - `DOCKERHUB_TOKEN`: [get dockerhub access token](https://hub.docker.com/settings/security)
    - `DOCKERHUB_USERNAME`: dockerhub username
    - `SLACK_WEBHOOK`: [get slack incoming webhook](https://api.slack.com/apps/)
    - `TARGET`: target directory in pipelines
 
- Change mod bash file
    - git update-index --chmod=+x `file.sh`
