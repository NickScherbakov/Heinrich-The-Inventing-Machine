# TRIZ Basics

## Introduction to TRIZ

TRIZ (Theory of Inventive Problem Solving) is a systematic methodology for innovation and creative problem solving, developed by Genrich Altshuller starting in 1946.

## Core Concepts

### What is TRIZ?

TRIZ is based on the premise that:
1. **Patterns exist** in how technical problems are solved across industries
2. **Contradictions** are at the heart of difficult problems  
3. **Innovation levels** can be classified and predicted
4. **Evolution patterns** describe how technical systems develop

### The TRIZ Approach

Unlike traditional brainstorming or trial-and-error, TRIZ provides:

- **Systematic methods** for identifying and resolving contradictions
- **Knowledge database** of proven solution patterns
- **Predictable pathways** for technical system evolution
- **Structured algorithms** (ARIZ) for complex problems

## Key TRIZ Tools

### 1. 39 Engineering Parameters

Standard characteristics used to describe technical systems:

- Weight, Speed, Strength, Temperature, etc.
- Maps real-world problems to standard framework
- Enables systematic contradiction analysis

### 2. 40 Inventive Principles

Fundamental patterns for resolving contradictions:

1. Segmentation - Divide object into parts
2. Taking Out - Extract problematic element
3. Local Quality - Vary characteristics by location
4. ... (and 37 more)

Each principle includes sub-principles and examples.

### 3. Contradiction Matrix

39×39 matrix that maps:
- **Improving parameter** (what you want to improve)
- **Worsening parameter** (what gets worse)
- **Recommended principles** (how to solve it)

Example:
- Want: Increase **Speed** (Parameter 9)
- But: Increases **Energy Use** (Parameter 19)
- Solutions: Principles 2, 6, 19, 35

### 4. Technical Contradictions

When improving one parameter worsens another:
- "Make it faster" → "Uses more energy"
- "Make it stronger" → "Becomes heavier"

### 5. Physical Contradictions

When a parameter must have opposite properties:
- Surface must be "rough AND smooth"
- Material must be "hot AND cold"

Resolution strategies:
- **Separation in time**: Hot when needed, cold otherwise
- **Separation in space**: Rough on top, smooth on bottom
- **Separation in scale**: Rough micro, smooth macro

## TRIZ in Heinrich

Heinrich implements TRIZ through a 7-module pipeline:

1. **Problem Parser**: Extract technical system, desired improvement, harmful effect
2. **Contradiction Identifier**: Map to 39 parameters, identify contradictions
3. **Principle Selector**: Use contradiction matrix to select relevant principles
4. **Effects Lookup**: Find applicable scientific effects and phenomena
5. **Concept Generator**: Generate solution concepts based on principles
6. **Adaptation Planner**: Adapt solutions to specific context
7. **Report Builder**: Create structured, traceable solution report

## Example: TRIZ Problem Solving

**Problem**: "Car must be faster without using more fuel"

**Step 1 - Problem Parsing**:
- Technical system: Automotive propulsion
- Desired improvement: Speed
- Harmful effect: Increased fuel consumption

**Step 2 - Contradiction Identification**:
- Improving parameter: Speed (9)
- Worsening parameter: Energy consumption (19)
- Type: Technical contradiction

**Step 3 - Principle Selection** (from matrix):
- Principle 2: Taking Out (Separate conflicting properties)
- Principle 15: Dynamics (Variable characteristics)
- Principle 35: Parameter Changes (Different states)

**Step 4 - Solution Concepts**:
1. **Hybrid powertrain** (Principle 2): Electric for efficiency, gas for speed
2. **Variable compression engine** (Principle 15): Adjust compression ratio dynamically
3. **Active aerodynamics** (Principle 35): Change body shape at different speeds

## Learning More

- **TRIZ Glossary**: See [i18n/glossary_en.yaml](../../i18n/glossary_en.yaml)
- **40 Principles**: See [40_principles.yaml](../../40_principles.yaml)
- **39 Parameters**: See [39_parameters.yaml](../../39_parameters.yaml)
- **Heinrich Architecture**: See [architecture.md](architecture.md)

## Resources

- **Altshuller Foundation**: Original TRIZ resources
- **Oxford TRIZ**: Academic research and case studies
- **TRIZ Journal**: Contemporary applications

---

*"The best way to predict the future is to invent it systematically."* - TRIZ Philosophy
