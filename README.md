# RAG Document Workflow

## Overview
This project simulates a retrieval-augmented generation workflow by ingesting text, splitting it into chunks, retrieving relevant context, and generating grounded responses in a structured format.

## Features
- Document ingestion from text file
- Chunking into smaller sections
- Keyword-based retrieval
- Grounded response generation
- Structured JSON output

## Tech Stack
Python, JSON, RAG concepts

## Architecture
Document Input → Chunking → Retrieval → Response Generation

## What I implemented
- Read document content from file
- Split long content into smaller searchable chunks
- Retrieved the most relevant chunk for a query
- Returned a structured response with query, context, and answer

## How to run
1. Clone the repository
2. Run `python app.py`

## Sample Output
See `output_example.json`

## Status
Improved RAG prototype with document ingestion and structured output
