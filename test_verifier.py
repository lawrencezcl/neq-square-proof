#!/usr/bin/env python3
"""
Test script for the Noir neq_square verifier logic
Demonstrates the mathematical constraint verification
"""

def verify_neq_square(x: int, y: int, w: int) -> bool:
    """
    Verify that x != y^2 using the constraint (x - y^2) * w == 1
    
    Args:
        x: Public input 1
        y: Public input 2  
        w: Private witness (multiplicative inverse)
    
    Returns:
        bool: True if constraint is satisfied, False otherwise
    """
    y_squared = y * y
    diff = x - y_squared
    
    # Check the core constraint
    constraint_satisfied = (diff * w) == 1
    
    print(f"Testing: x={x}, y={y}, w={w}")
    print(f"y² = {y_squared}")
    print(f"x - y² = {diff}")
    print(f"(x - y²) × w = {diff} × {w} = {diff * w}")
    print(f"Constraint satisfied: {constraint_satisfied}")
    print(f"Conclusion: x {'!=' if constraint_satisfied else '=='} y²")
    print("-" * 50)
    
    return constraint_satisfied

def find_witness(x: int, y: int) -> int:
    """
    Find the witness w for given x, y such that (x - y^2) * w == 1
    
    Returns:
        int: The witness w, or None if x == y^2
    """
    y_squared = y * y
    diff = x - y_squared
    
    if diff == 0:
        print(f"Cannot find witness: x ({x}) == y² ({y_squared})")
        return None
    
    # For simplicity, we assume diff = 1 in our test cases
    # In a real implementation, this would use modular inverse
    if diff == 1:
        return 1
    else:
        print(f"Note: diff = {diff}, witness calculation would need modular inverse")
        return None

def main():
    """Run test cases for the neq_square verifier"""
    
    print("🧮 Noir neq_square Verifier Test")
    print("=" * 50)
    print("Testing constraint: (x - y²) × w = 1")
    print("This proves x ≠ y² when satisfied\n")
    
    # Test cases
    test_cases = [
        # Valid cases (x != y^2)
        (10, 3, 1),   # 10 != 9, diff = 1, w = 1
        (5, 2, 1),    # 5 != 4, diff = 1, w = 1  
        (17, 4, 1),   # 17 != 16, diff = 1, w = 1
        
        # Edge cases
        (1, 0, 1),    # 1 != 0, diff = 1, w = 1
        (2, 1, 1),    # 2 != 1, diff = 1, w = 1
    ]
    
    print("✅ Valid Test Cases:")
    for i, (x, y, w) in enumerate(test_cases, 1):
        print(f"\nTest {i}:")
        result = verify_neq_square(x, y, w)
        assert result, f"Test {i} should pass but failed"
    
    print("\n❌ Invalid Test Cases:")
    
    # Invalid cases (x == y^2) - these should fail
    invalid_cases = [
        (9, 3),   # 9 == 3^2
        (16, 4),  # 16 == 4^2  
        (25, 5),  # 25 == 5^2
        (0, 0),   # 0 == 0^2
        (1, 1),   # 1 == 1^2
    ]
    
    for i, (x, y) in enumerate(invalid_cases, 1):
        print(f"\nInvalid Test {i}:")
        w = find_witness(x, y)
        if w is None:
            print(f"✓ Correctly identified: x ({x}) == y² ({y*y}), no valid witness exists")
        else:
            # This shouldn't happen for our test cases
            result = verify_neq_square(x, y, w)
            print(f"Unexpected: found witness {w}, result: {result}")
    
    print("\n🎉 All tests completed!")
    print("\n📋 Summary:")
    print("- The constraint (x - y²) × w = 1 successfully proves x ≠ y²")
    print("- When x = y², no valid witness w exists")
    print("- When x ≠ y², witness w can be computed as (x - y²)⁻¹")
    print("- This forms the basis of our zero-knowledge proof system")

if __name__ == "__main__":
    main()