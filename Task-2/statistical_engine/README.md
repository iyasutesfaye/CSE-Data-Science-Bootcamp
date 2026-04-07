# Statistical Engineering & Simulation

## Overview
This project implements a statistical engine from scratch using pure Python.

## Mathematical Logic
Variance:
- Population: Σ(x - μ)² / n
- Sample: Σ(x - μ)² / (n - 1)

Median:
- Even → average of middle two
- Odd → middle value

## Setup
git clone <repo>
cd statistical_engine
python main.py

## Testing
python -m unittest discover tests

## Acceptance Checklist
- [x] Handles empty data
- [x] Handles mixed data types
- [x] Correct sample vs population variance
- [x] Multimodal mode supported