# FunImpute Project Structure

This document describes the clean, organized structure of the enterprise-grade imputation analysis service.

## 📁 Project Overview

```
funimpute/
├── 📄 .gitignore                          # Git ignore patterns
├── 📄 README.md                           # Main project documentation
├── 📄 pyproject.toml                      # Python package configuration
├── 📄 requirements.txt                    # Python dependencies
├── 📄 config.yml                          # Default configuration
├── 📄 PROJECT_STRUCTURE.md               # This file
│
├── 📁 funimpute/                          # Main package source code
│   ├── 📄 __init__.py                     # Package initialization
│   ├── 📄 models.py                       # Core data models and enums
│   ├── 📄 enterprise_models.py            # Enterprise metadata models
│   ├── 📄 schema_validator.py             # JSON Schema validation
│   ├── 📄 enterprise_loader.py            # Enterprise metadata loader
│   ├── 📄 io.py                          # I/O operations and metadata loading
│   ├── 📄 analyzer.py                     # Main analysis orchestration
│   ├── 📄 outliers.py                     # Outlier detection algorithms
│   ├── 📄 mechanism.py                    # Missingness mechanism analysis
│   ├── 📄 proposal.py                     # Imputation method proposals
│   ├── 📄 exceptions.py                   # Exception handling rules
│   ├── 📄 metrics.py                      # Prometheus metrics collection
│   └── 📄 cli.py                         # Command-line interface
│
├── 📁 schemas/                            # JSON Schema definitions
│   └── 📄 imputation_metadata_schema.json # Enterprise metadata schema
│
├── 📁 examples/                           # Example files and usage
│   └── 📄 sample_enterprise_metadata.json # Sample enterprise metadata
│
├── 📁 tests/                              # Unit and integration tests
│   ├── 📄 __init__.py
│   ├── 📄 test_models.py                  # Core model tests
│   ├── 📄 test_exceptions.py              # Exception handling tests
│   ├── 📄 test_enterprise_metadata.py     # Enterprise metadata tests
│   └── 📄 conftest.py                     # Test configuration
│
├── 📁 data/                               # Sample data files
│   ├── 📄 metadata.csv                    # Sample legacy metadata
│   └── 📄 material_master_data.csv        # Sample dataset
│
├── 📁 output/                             # Analysis output files
│   ├── 📄 imputation_suggestions.csv      # Generated suggestions
│   └── 📄 audit_logs.jsonl               # Detailed audit logs
│
└── 📁 .venv311/                          # Virtual environment (ignored)
```

## 🏗️ Architecture Components

### Core Package (`funimpute/`)

| Module | Purpose | Key Classes/Functions |
|--------|---------|----------------------|
| `models.py` | Core data models and enums | `ColumnMetadata`, `AnalysisConfig`, `ImputationSuggestion` |
| `enterprise_models.py` | Enterprise metadata models | `EnterpriseMetadata`, `EnterpriseColumnMetadata` |
| `schema_validator.py` | JSON Schema validation | `SchemaValidator`, `validate_metadata_file` |
| `enterprise_loader.py` | Enterprise metadata loading | `EnterpriseMetadataLoader`, `MetadataCache` |
| `io.py` | I/O operations | `load_metadata`, `load_configuration` |
| `analyzer.py` | Main orchestration | `ImputationAnalyzer` |
| `outliers.py` | Outlier detection | `detect_outliers_iqr`, `analyze_outliers` |
| `mechanism.py` | Missingness analysis | `analyze_mechanism` |
| `proposal.py` | Imputation proposals | `propose_method` |
| `exceptions.py` | Exception handling | `apply_exception_handling` |
| `metrics.py` | Prometheus metrics | `MetricsCollector` |
| `cli.py` | Command-line interface | `main` (Click-based CLI) |

### Configuration & Schema

- **`config.yml`**: Default configuration with all parameters
- **`schemas/`**: JSON Schema definitions for enterprise metadata validation
- **`examples/`**: Sample files demonstrating usage

### Data Organization

- **`data/`**: Sample input data and metadata files
- **`output/`**: Generated analysis results and audit logs
- **`tests/`**: Comprehensive test suite

## 🚀 Usage

### Installation
```bash
pip install -e .
```

### Command Line Usage
```bash
# Basic analysis with auto-detection
impute-analyze -m data/metadata.csv -d data/material_master_data.csv

# Enterprise JSON metadata
impute-analyze -m examples/sample_enterprise_metadata.json -d data/material_master_data.csv -f json

# With custom configuration
impute-analyze -m data/metadata.csv -d data/material_master_data.csv -c config.yml
```

### Python API Usage
```python
from funimpute import ImputationAnalyzer, load_metadata, load_configuration

# Load configuration and metadata
config = load_configuration("config.yml")
metadata = load_metadata("data/metadata.csv")

# Run analysis
with ImputationAnalyzer(config) as analyzer:
    results = analyzer.analyze_dataset("data/metadata.csv", "data/material_master_data.csv")
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test modules
pytest tests/test_enterprise_metadata.py -v
pytest tests/test_exceptions.py -v
```

## 📊 Monitoring

- **Prometheus metrics**: Available on port 8001 (configurable)
- **Audit logs**: Detailed JSON-lines format in `output/audit_logs.jsonl`
- **Suggestions output**: CSV format in `output/imputation_suggestions.csv`

## 🔧 Configuration

Configuration can be provided via:
1. YAML file (`config.yml`)
2. Environment variables (prefixed with `FUNIMPUTE_`)
3. Command-line arguments (highest priority)

## 🏢 Enterprise Features

- **Formal JSON Schema**: Comprehensive metadata validation
- **Governance Support**: Data classification, PII handling, compliance tags
- **Business Rules**: Custom validation and imputation rules
- **Lineage Tracking**: Data source and transformation history
- **Quality Thresholds**: Configurable data quality monitoring
- **Caching**: Metadata caching for performance
- **Backward Compatibility**: Full support for legacy CSV metadata

## 🗑️ Cleaned Up Files

The following files were removed during cleanup:
- `simplified_imputation_analyzer.py` (replaced by modular package)
- `test_enterprise_integration.py` (temporary integration test)
- `.idea/` (IDE configuration)
- `.pytest_cache/` (test cache)
- `.metadata_cache/` (runtime cache)

## 📝 Notes

- The project is fully Pydantic v2 compatible
- All imports are properly organized and functional
- Enterprise metadata integration is complete and tested
- Legacy CSV metadata support is maintained
- The package is production-ready with comprehensive error handling and monitoring
