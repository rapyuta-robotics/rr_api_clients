# API Client Generation Repo

This repo can be used to automatically generate client libraries for backend services that has a OpenAPI specification.

## Supported Languages for Client Libraries

[x] Python
[ ] Javascript (Typescript, redux) - planned

## How to trigger workflow

To trigger a workflow from another repository, the following curl command or similar http request must be made.

```bash
curl -L \
    -X POST \
    -H "Accept: application/vnd.github+json" \
    -H "Authorization: Bearer $CLIENT_REPO_REMOTE_TRIGGER_TOKEN" \
    -H "X-GitHub-Api-Version: 2022-11-28" \
    https://api.github.com/repos/rapyuta-robotics/rr_api_clients/actions/workflows/build.yaml/dispatches \
    -d '{"ref": "devel","inputs":{"docker-image-name":"quay.io/rapyuta/io_amr_gwm",
    "client-name":"gwm","version":"devel","service-port":"8000",
    "openapi-path":"api/schema/","docker-command":"poetry run gunicorn"}}'
```

`CLIENT_REPO_REMOTE_TRIGGER_TOKEN` - A robot or a user personal token that allows for cross repo actions.

As for the actual data sent in the request.

`ref` - The branch, tag or commit that you want to use in the `rr_api_clients` repo.
`input` - The input passed to the client generation workflow.
`input.docker-image-name` - The Docker image name to be used for generating the client. In this example, it's set to `quay.io/rapyuta/io_amr_gwm`.
`input.client-name` - The name of the client to be generated. In this example, it's set to `gwm`.
`input.version` - The docker tag `version`
`input.service-port` - The port on which the backend service is running. In this example, it's set to `8000`.
`input.openapi-path` - The path to the OpenAPI specification file within the repository. In this example, it's set to `api/schema/`.
`input.docker-command` - **(optional)** The Docker command to make . In this example, it's set to `poetry run gunicorn`.