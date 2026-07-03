# Cost Analysis Report

## Objective

The objective of this project is to build a Retrieval-Augmented Generation (RAG) system that delivers accurate responses while keeping infrastructure and inference costs low.

---

## Embedding Model

**Model:** all-MiniLM-L6-v2

### Why this model?

* Lightweight (~90 MB)
* Fast inference
* Good semantic similarity performance
* Free to use
* Suitable for CPU execution

---

## Vector Database

**Database:** ChromaDB

### Advantages

* Open-source
* No hosting cost
* Persistent local storage
* Easy integration with Python
* Good performance for small and medium datasets

### Limitations

* Not designed for large distributed systems
* Limited enterprise features

---

## LLM

**Provider:** Groq

### Advantages

* Very fast inference
* Free developer tier
* Simple API integration
* Low latency

---

## Approximate Cost Comparison

| Component       | Current Solution        | Enterprise Alternative        |
| --------------- | ----------------------- | ----------------------------- |
| Embeddings      | all-MiniLM-L6-v2 (Free) | OpenAI text-embedding-3-large |
| Vector Database | ChromaDB (Free)         | Pinecone / Weaviate           |
| LLM             | Groq Free Tier          | OpenAI GPT-4o / Claude        |
| Hosting         | Local Machine           | Cloud GPU Instance            |

---

## Estimated Monthly Cost

| Solution                    | Approximate Cost |
| --------------------------- | ---------------: |
| Current Project             |               $0 |
| Managed Vector DB + OpenAI  |         $30–150+ |
| Enterprise Production Setup |      $200+/month |

---

## Trade-offs

### Benefits

* Zero infrastructure cost
* Fast retrieval
* Low latency
* Easy local deployment
* Open-source components

### Drawbacks

* Limited scalability
* No automatic backups
* Single-machine deployment
* Manual maintenance

---

## Conclusion

The implemented RAG system achieves a good balance between retrieval quality, response speed, and operational cost. For prototype and small-scale deployments, the chosen architecture offers excellent performance while keeping infrastructure expenses close to zero. Enterprise deployments may benefit from managed vector databases and commercial LLM APIs for improved scalability and reliability.
