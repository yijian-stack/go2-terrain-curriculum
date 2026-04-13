# Experiment Plan

## Baseline

- Robot: Unitree Go2
- Policy type: command-conditioned locomotion
- Control objective: track target linear/angular velocity while staying upright
- Benchmark split: flat, rough, stairs

## Core ablations

- no curriculum vs progressive curriculum
- dense reward only vs reward with slip and torque penalties
- wide command range vs staged command range

## Evaluation metrics

- success rate
- time-to-finish
- command tracking error
- stability score
- torque penalty
- slip penalty

## Why this matters

Interviewers often care less about absolute reward and more about whether you can explain why one policy is better. This plan makes those comparisons first-class.

