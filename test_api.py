#!/usr/bin/env python3
"""Test FunImpute API directly"""

import pandas as pd
import sys
import os

# Add funimputer to path
sys.path.insert(0, '/')

import funimpute
from funimpute.models import ColumnMetadata

def test_simple_api():
    print("=== Testing Simple API ===")
    
    # Test file-based API
    try:
        suggestions = funimpute.analyze_imputation_requirements(
            'test_metadata.csv', 
            'test_data.csv'
        )
        print(f"✓ File API: {len(suggestions)} suggestions generated")
        for s in suggestions[:2]:  # Show first 2
            print(f"  {s.column_name}: {s.proposed_method} (confidence: {s.confidence_score:.3f})")
    
    except Exception as e:
        print(f"✗ File API failed: {e}")
    
    # Test DataFrame API
    try:
        data = pd.DataFrame({
            'user_id': [1, 2, 3, 4, 5],
            'age': [25, None, 35, 42, None], 
            'income': [50000, 60000, None, 80000, 45000],
            'category': ['A', 'B', None, 'A', 'C']
        })
        
        metadata = [
            ColumnMetadata('user_id', 'integer', unique_flag=True),
            ColumnMetadata('age', 'integer', min_value=0, max_value=120),
            ColumnMetadata('income', 'float', business_rule='Correlates with age'),
            ColumnMetadata('category', 'categorical')
        ]
        
        suggestions = funimpute.analyze_dataframe(data, metadata)
        print(f"✓ DataFrame API: {len(suggestions)} suggestions generated")
        
        # Show missing data analysis
        for s in suggestions:
            if s.missing_count > 0:
                print(f"  {s.column_name}: {s.missing_count} missing -> {s.proposed_method}")
    
    except Exception as e:
        print(f"✗ DataFrame API failed: {e}")

def test_class_api():
    print("\n=== Testing Class API ===")
    
    try:
        analyzer = funimpute.SimpleImputationAnalyzer()
        suggestions = analyzer.analyze('test_metadata.csv', 'test_data.csv')
        print(f"✓ Class API: {len(suggestions)} suggestions generated")
        
        # Show confidence distribution
        confidences = [s.confidence_score for s in suggestions]
        avg_confidence = sum(confidences) / len(confidences)
        print(f"  Average confidence: {avg_confidence:.3f}")
    
    except Exception as e:
        print(f"✗ Class API failed: {e}")

def test_error_handling():
    print("\n=== Testing Error Handling ===")
    
    # Test missing file
    try:
        suggestions = funimpute.analyze_imputation_requirements(
            'nonexistent.csv', 
            'test_data.csv'
        )
        print("✗ Should have failed with missing file")
    except FileNotFoundError:
        print("✓ Correctly handles missing metadata file")
    except Exception as e:
        print(f"? Unexpected error: {e}")
    
    # Test empty metadata
    try:
        suggestions = funimpute.analyze_dataframe(
            pd.DataFrame({'col1': [1, 2, 3]}), 
            []
        )
        print("✓ Handles empty metadata gracefully")
    except Exception as e:
        print(f"✓ Correctly rejects empty metadata: {type(e).__name__}")

if __name__ == "__main__":
    print("Testing FunImpute Implementation...")
    print(f"FunImpute version: {funimpute.__version__}")
    print(f"Author: {funimpute.__author__}")
    
    test_simple_api()
    test_class_api() 
    test_error_handling()
    
    print("\n=== Test Complete ===")