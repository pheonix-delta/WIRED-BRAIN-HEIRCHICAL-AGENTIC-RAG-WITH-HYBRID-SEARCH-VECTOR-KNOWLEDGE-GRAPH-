# 03 Search Reduction


```mermaid
graph LR
    A[693,313 Chunks<br/>100%] -->|Gate Filter| B[~53,000 Chunks<br/>7.6%]
    B -->|Branch Filter| C[~5,000 Chunks<br/>0.7%]
    C -->|Topic Filter| D[~500 Chunks<br/>0.07%]
    D -->|Vector Search| E[20 Chunks<br/>0.003%]
    
    style A fill:#FF6B6B,stroke:#333,stroke-width:2px,color:#fff
    style B fill:#FFA500,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#FFD700,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#90EE90,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#4CAF50,stroke:#333,stroke-width:3px,color:#fff
```


---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
