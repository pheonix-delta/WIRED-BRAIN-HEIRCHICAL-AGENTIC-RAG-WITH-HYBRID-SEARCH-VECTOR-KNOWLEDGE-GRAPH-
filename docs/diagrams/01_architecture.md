# 01 Architecture


```mermaid
graph TB
    subgraph "User Interface"
        Q[User Query]
    end
    
    subgraph "Stage 1: Intent Routing"
        Q --> R[SetFit Router]
        R --> S1{Confidence > 0.7?}
        S1 -->|Yes| G[Gate Selected]
        S1 -->|No| K[Keyword Matching]
        K --> S2{Confidence > 0.6?}
        S2 -->|Yes| G
        S2 -->|No| SE[Semantic Similarity]
        SE --> G
    end
    
    subgraph "Stage 2: Hierarchical Filtering"
        G --> HF[Hierarchical Filter]
        HF --> G1[Gate: 693K → 53K]
        G1 --> B1[Branch: 53K → 5K]
        B1 --> T1[Topic: 5K → 500]
        T1 --> L1[Level: 500 chunks]
    end
    
    subgraph "Stage 3: Hybrid Retrieval"
        L1 --> VS[Vector Search<br/>Qdrant HNSW]
        L1 --> GT[Graph Traversal<br/>PostgreSQL]
        L1 --> QS[Quality Scoring]
        VS --> FR[Fusion Ranking<br/>0.5v + 0.3g + 0.2q]
        GT --> FR
        QS --> FR
    end
    
    subgraph "Output"
        FR --> TOP[Top 20 Results]
    end
    
    style Q fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style TOP fill:#FF6B6B,stroke:#333,stroke-width:2px,color:#fff
```


---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
