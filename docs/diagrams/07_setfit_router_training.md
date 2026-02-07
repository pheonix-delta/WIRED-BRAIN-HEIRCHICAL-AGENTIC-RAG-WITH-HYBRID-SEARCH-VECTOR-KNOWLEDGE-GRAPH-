# 07 SetFit Router Training

```mermaid
flowchart TD
    A[Raw Queries + Gate Labels] --> B[Label QA + Normalize]
    B --> C[Train/Val Split]
    C --> D[Sentence-Transformer Encoder]
    D --> E[SetFit Contrastive Training]
    E --> F[Calibrate Thresholds
(Primary: 0.6-0.7)]
    F --> G[Export Model
trained_neural_router/]

    G --> H[Runtime: GateRouter.route]
    H --> I{Confidence > 0.6?}
    I -->|Yes| J[Primary Gate + Secondary Gates]
    I -->|No| K[Keyword Scoring Fallback]
    K --> L[Fallback Gate]

    style A fill:#667eea,stroke:#333,stroke-width:2px,color:#fff
    style E fill:#4facfe,stroke:#333,stroke-width:2px,color:#fff
    style G fill:#43e97b,stroke:#333,stroke-width:2px,color:#fff
    style J fill:#4caf50,stroke:#333,stroke-width:2px,color:#fff
    style L fill:#ff6b6b,stroke:#333,stroke-width:2px,color:#fff
```

---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
