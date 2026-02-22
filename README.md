# Perioperative Clinical Data Automation & Analysis

## Overview

This repository contains automated data processing pipelines designed for retrospective anesthesiology research. The scripts utilize Python and Pandas to ingest raw Electronic Medical Record (EMR) data, apply clinical exclusion criteria, and instantly generate publication-ready demographic summaries (Table 1).

## Dataset: VitalDB

The current pipeline is built to interface directly with the **VitalDB API**, a high-fidelity perioperative open dataset containing over 6,300 noncardiac surgical cases.

## Workflow & Methodology

Instead of manually auditing charts in Excel, this pipeline automates the data wrangling process to ensure reproducible and error-free research:

1. **Automated Ingestion:** Directly queries and loads massive clinical datasets into memory.
2. **Cohort Filtering:** Applies string-matching algorithms to isolate specific surgical cohorts (e.g., `Cholecystectomy` or `Gastrectomy`), accounting for variations in EMR documentation.
3. **Data Cleaning:** Automatically identifies and drops missing/invalid records (e.g., missing preoperative labs or baseline vitals) to establish a clean study cohort.
4. **Feature Engineering:** Uses lambda functions to create new clinical categories from continuous variables (e.g., classifying patients as `Obese` vs `Non-Obese` based on a BMI threshold of 30.0).
5. **Statistical Aggregation:** Automatically groups the cohort and calculates mean demographic values, outputting a cleanly formatted `Table 1` CSV file.

## Objective

The goal of this project is to demonstrate the ability to handle massive, messy hospital datasets and streamline the exact data-cleaning bottlenecks that slow down retrospective clinical studies.
