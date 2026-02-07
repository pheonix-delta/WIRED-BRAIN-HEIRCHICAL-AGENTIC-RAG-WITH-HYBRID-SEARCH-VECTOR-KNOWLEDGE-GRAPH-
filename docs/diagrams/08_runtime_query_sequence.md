# 08 Runtime Query Sequence

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant GR as GateRouter
    participant NR as NeuralRouter
    participant HR as HybridRetrieverV2
    participant PG as PostgreSQL
    participant QD as Qdrant
    participant TRM as TRMEngineV2
    participant MF as ModelFusionEngine

    U->>GR: query
    GR->>NR: predict(query)
    alt confidence > 0.6
        NR-->>GR: gate + confidence
    else fallback
        GR->>GR: keyword scoring
        GR-->>GR: fallback gate
    end

    GR->>HR: hybrid_retrieve(query, gate)
    HR->>PG: hierarchical filter + graph walk
    par parallel signals
        HR->>QD: vector search
        HR->>PG: graph traversal
        HR->>HR: quality scoring
    end
    HR-->>TRM: top-k fused context

    loop iterative reasoning
        TRM->>PG: trace storage
    end

    TRM-->>MF: draft answer + chunks
    MF-->>U: final response
```

---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
