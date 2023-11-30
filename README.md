
# Khaanvani - A Chatbot
------------------------------------------------------------------------------
[![SAST Bandit](https://img.shields.io/badge/SAST-Bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![DAST: Wapiti](https://img.shields.io/badge/DAST-Wapiti-red.svg)
![Functional Testing: Pytest](https://img.shields.io/badge/:Functional_Testing-Pytest-blue.svg)
![Dynamic Testing: Code_Coverage](https://img.shields.io/badge/:Dynamic_Testing-Code_Coverage-green.svg)
![IAC: Terraform](https://img.shields.io/badge/:IAC-Terraform-purple.svg)

This repository hosts a Chatbot project that serves as an intelligent virtual assistant capable of responding to text queries related to various Acts, Rules, and Regulations applicable to the Mining industry. It's designed to make the information retrieval process more efficient and user-friendly for people in the mining sector.
## Features

- 24/7 availability
- Text queries
- Ease of use


## Tech Stack

- Python

- LangChain

- Natural Language Processing (NLP)

- Pinecone

## Tools:

-Bandit for code vulnerability checking

-Wapiti for dynamic checking

-Pytest for testing

-Terraform for iac tool

## Demo
Visit our site at [khaanvaani.streamlit.app](https://khaanvaani.streamlit.app/)



## Our flowchart: Dev Repo
```mermaid
    gitGraph
       commit id: "."
       branch B1
       checkout B1
       commit id: "Commit Changes"
       checkout main
       checkout B1
       checkout main
       checkout B1
       commit id:"Bandit Passed"
       commit id:"Wapiti Passed"
       checkout main
       merge B1 id: "Merge " tag: "Changes Committed" type: REVERSE
       commit id: "Push to Test"
       checkout main

```

## Our flowchart: Test Repo
```mermaid
    gitGraph
       commit id: "."
       branch B2
       checkout B2
       commit id: "Commit Changes"
       checkout main
       checkout B2
       checkout main
       checkout B2
       commit id:"Selenium Tests Passed"
       commit id:"Code Coverage Tests Passed"
       checkout main
       merge B2 id: "Merge " tag: "Changes Committed" type: REVERSE
       commit id: "Push to Prod"
       checkout main
    
```
## Future

Regional languages

Voice search

Legal Representative

1 in chat

2 in call

