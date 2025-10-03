# Create a cleaner architecture diagram for Heinrich system with improved readability
diagram_code = """
flowchart TD
    %% User Interface Layer
    CLI[CLI Interface] 
    API[API Interface]
    
    %% Security
    SEC[Security Module]
    
    %% Orchestration
    AO[Agent Orchestrator]
    
    %% LLM Integration
    LLM[LLM Adapter]
    
    %% TRIZ Pipeline - arranged horizontally for better flow
    PP[Problem Parser]
    CI[Contradiction ID]
    PS[Principle Select]
    EL[Effects Lookup]
    CG[Concept Gen]
    AP[Adaptation Plan]
    RB[Report Builder]
    
    %% Knowledge Base
    KB[Knowledge Base<br/>Parameters &amp; Principles<br/>Matrix &amp; Effects]
    
    %% Documentation
    DOC[Multi-lang Docs]
    
    %% Main Entry Flow
    CLI --> SEC
    API --> SEC
    SEC --> AO
    
    %% Core Processing Flow
    AO --> PP
    PP --> CI
    CI --> PS
    PS --> EL
    EL --> CG
    CG --> AP
    AP --> RB
    
    %% LLM Integration - dotted lines for clarity
    AO -.-> LLM
    PP -.-> LLM
    CI -.-> LLM
    CG -.-> LLM
    AP -.-> LLM
    
    %% Knowledge Access - different style
    CI ===> KB
    PS ===> KB
    EL ===> KB
    CG ===> KB
    
    %% Output Generation
    RB --> DOC
    RB --> AO
    
    %% Return Path
    AO --> SEC
    SEC --> CLI
    SEC --> API
    
    %% Styling for better visibility
    classDef interface fill:#B3E5EC
    classDef security fill:#FFCDD2
    classDef core fill:#A5D6A7
    classDef knowledge fill:#FFEB8A
    classDef llm fill:#9FA8B0
    
    class CLI,API interface
    class SEC security
    class AO,PP,CI,PS,EL,CG,AP,RB core
    class KB,DOC knowledge
    class LLM llm
"""

# Create the cleaner mermaid diagram
png_path, svg_path = create_mermaid_diagram(diagram_code, 'heinrich_architecture_clean.png', 'heinrich_architecture_clean.svg', width=1400, height=900)
print(f"Clean architecture diagram saved to: {png_path} and {svg_path}")