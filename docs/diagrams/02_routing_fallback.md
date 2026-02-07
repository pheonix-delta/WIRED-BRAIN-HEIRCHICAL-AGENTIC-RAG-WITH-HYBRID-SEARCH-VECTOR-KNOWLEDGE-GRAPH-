# 02 Routing Fallback


```mermaid
flowchart TD
    START([User Query]) --> SETFIT[SetFit Classification<br/>76.67% Success Rate]
    SETFIT --> CHECK1{Confidence<br/>> 0.7?}
    CHECK1 -->|Yes 76.67%| SUCCESS1[✅ Gate Selected<br/>Method: SetFit]
    CHECK1 -->|No 23.33%| KEYWORD[Keyword Matching<br/>18% Success Rate]
    
    KEYWORD --> CHECK2{Confidence<br/>> 0.6?}
    CHECK2 -->|Yes 18%| SUCCESS2[✅ Gate Selected<br/>Method: Keyword]
    CHECK2 -->|No 5.33%| SEMANTIC[Semantic Similarity<br/>5.33% Success Rate]
    
    SEMANTIC --> SUCCESS3[✅ Gate Selected<br/>Method: Semantic]
    
    SUCCESS1 --> FINAL[100% Routing Success]
    SUCCESS2 --> FINAL
    SUCCESS3 --> FINAL
    
    style START fill:#667eea,stroke:#333,stroke-width:3px,color:#fff
    style SUCCESS1 fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style SUCCESS2 fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style SUCCESS3 fill:#4CAF50,stroke:#333,stroke-width:2px,color:#fff
    style FINAL fill:#FF6B6B,stroke:#333,stroke-width:3px,color:#fff
```


---

**Note:** This diagram is rendered automatically by GitHub markdown.
To export as image, use [Mermaid Live Editor](https://mermaid.live)
