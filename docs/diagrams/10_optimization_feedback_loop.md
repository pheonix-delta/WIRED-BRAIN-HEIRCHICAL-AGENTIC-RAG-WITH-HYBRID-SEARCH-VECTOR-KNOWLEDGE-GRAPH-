# 10 Optimization Feedback Loop

```mermaid
flowchart LR
    A[Routing + Retrieval] --> B[Offline Evaluation]
    B --> C[Metrics: NDCG@20, Latency, Quality]
    C --> D[Adjust Weights
fusion + thresholds]
    D --> E[Update Heuristics
skip_vector, graph_walk]
    E --> F[Re-run Benchmarks]
    F --> B

    style A fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style C fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff
    style D fill:#f6d365,stroke:#333,stroke-width:2px,color:#fff
    style F fill:#ff6b6b,stroke:#333,stroke-width:2px,color:#fff
```

---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
