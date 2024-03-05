# SEO Notebook Prompt Compressor

## Run Locally
    python -m uvicorn app:app

## Build & Deploy Container
### Build docker container
    docker build -t "prompt-compressor" .

### Tag Artifact Repository Container
    docker tag prompt-compressor northamerica-northeast2-docker.pkg.dev/prompt-compressor/prompt-compressor-ar/prompt-compressor

### Push to Artifact Repository
    docker push northamerica-northeast2-docker.pkg.dev/prompt-compressor/prompt-compressor-ar/prompt-compressor