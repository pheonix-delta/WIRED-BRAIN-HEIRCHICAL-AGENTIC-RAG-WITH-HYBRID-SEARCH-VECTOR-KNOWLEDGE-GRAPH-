# 06 Knowledge Graph


```mermaid
graph LR
    subgraph "Entities: 172,683"
        LQR[LQR Controller]
        RE[Riccati Equation]
        SS[State Space]
        LA[Linear Algebra]
        OC[Optimal Control]
    end
    
    subgraph "Relationships: 688,642"
        LQR -->|USES| RE
        LQR -->|REQUIRES| SS
        LQR -->|REQUIRES| LA
        LQR -->|IS_A| OC
        RE -->|REQUIRES| LA
        SS -->|REQUIRES| LA
    end
    
    subgraph "Chunks: 693,313"
        C1[Chunk: LQR Design]
        C2[Chunk: Riccati Solution]
        C3[Chunk: State Space Rep]
    end
    
    LQR -.->|MENTIONED_IN| C1
    RE -.->|MENTIONED_IN| C2
    SS -.->|MENTIONED_IN| C3
    
    style LQR fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style C1 fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
```


---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
