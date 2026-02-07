# 09 DB Population And Indexes

```mermaid
flowchart TD
    A[Labeled JSONL or TOON] --> B[Stage 6: DB Population]

    B --> C[Embedding Model
BAAI/bge-small-en-v1.5]
    C --> D[Vector Inserts
Qdrant Collection]

    B --> E[PostgreSQL Schema]
    E --> F[knowledge_chunks
content + gate_path + coords]
    E --> G[prerequisite_edges
chunk graph]

    F --> H[GIN: gate_path, concepts]
    F --> I[B-Tree: gate_id, quality]
    F --> J[pgvector: ivfflat index]

    B --> K[Graph Export
NetworkX -> Cytoscape JSON]

    style A fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#43e97b,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#f6d365,stroke:#333,stroke-width:2px,color:#fff
    style K fill:#ff6b6b,stroke:#333,stroke-width:2px,color:#fff
```

---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
