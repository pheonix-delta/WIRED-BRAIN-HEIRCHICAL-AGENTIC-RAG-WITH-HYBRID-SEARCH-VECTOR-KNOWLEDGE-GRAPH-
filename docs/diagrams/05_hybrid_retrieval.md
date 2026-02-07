# 05 Hybrid Retrieval


```mermaid
graph TD
    Q[User Query + Gate] --> F[Filtered Chunks<br/>~500 in gate]
    
    F --> V[Vector Search<br/>Qdrant HNSW<br/>Cosine Similarity]
    F --> G[Graph Traversal<br/>PostgreSQL<br/>Entity Relations]
    F --> QS[Quality Scoring<br/>0.878 avg]
    
    V --> V1[50 Candidates<br/>Weight: 0.5]
    G --> G1[30 Related<br/>Weight: 0.3]
    QS --> Q1[All Scored<br/>Weight: 0.2]
    
    V1 --> FR[Fusion Ranking<br/>Score = 0.5v + 0.3g + 0.2q]
    G1 --> FR
    Q1 --> FR
    
    FR --> TOP[Top 20 Results<br/>98ms Total]
    
    style Q fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style FR fill:#FF6B6B,stroke:#333,stroke-width:2px,color:#fff
    style TOP fill:#4CAF50,stroke:#333,stroke-width:3px,color:#fff
```


---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
