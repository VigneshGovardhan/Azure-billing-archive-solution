# Azure Billing Records Cost Optimization Solution

## Overview

**Goal:** Seamlessly reduce Cosmos DB costs by archiving old billing records (>3 months) to Azure Blob Storage (Cool/Archive tier) while keeping API unchanged.

## Architecture

![Architecture Diagram](architecture-diagram.png)

## Key Features

- Transparent API: fallback to Blob if record not in Cosmos DB.
- Automated archival: Azure Function/Data Factory moves old records.
- No downtime or data loss.

## Setup & Usage

### Archival Script

See [archive_records.py](archive_records.py) for sample archival logic.

### API Wrapper

See [api_layer_shim.py](api_layer_shim.py) for seamless API interception.

### Blob Lifecycle

See [blob_lifecycle_policy.json](blob_lifecycle_policy.json).

## Robustness & Edge Cases

- Handles Cosmos DB and Blob read/write failures with logging and alerts.
- Migration is idempotent, records are marked archived only after safe copy.

## Monitoring

- Integrate with Azure Monitor and setup metrics on both Cosmos DB and Blob Storage.
