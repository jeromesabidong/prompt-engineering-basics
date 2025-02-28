# Python using OpenAI API

A simple runner of scripts to study OpenAI if you don't want to install python on your local..
.. but you have Docker.

# Course References

- Following along with the course Prompt Engineering at DeepLearning.ai (1-7)
- Understanding and Applying Text Embeddings at DeepLearning.ai (8- )

Creating this as a test environment for the OpenAI API

## Prepare the Environment

1. Copy the `.env` file and input your OpenAI API key
2. Build the docker image

```
docker build -t python-openai .
```

3. Run image on temp mode

```
docker run -it --rm python-openai
```

## Guide

When opening the sample codes, you will see two kinds of comments
`NOTES` and `EDIT`

`NOTES` are general notes about the lesson. Some bits of information can be seen there

`EDIT` is usually paired with `END:EDIT` and is intended to be commented out for the specific `NOTES` section.
When this prevents from spamming the OpenAI API for prompts when the script is run.
