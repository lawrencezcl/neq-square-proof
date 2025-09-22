// noir/src/main.nr
// Prove that x != y^2 by providing w = (x - y^2)^{-1} as a private witness.
//
// Public inputs: x, y
// Private witness: w
//
// Constraint: (x - y^2) * w == 1
//
// If x == y^2 then no w exists and the circuit is unsatisfiable.
// If x != y^2 choose w = inv(x - y^2) mod field and constraint holds.

fn main(x: Field, y: pub Field, w: Field) {
    let y2 = y * y;
    let diff = x - y2;
    // Enforce multiplicative inverse: diff * w == 1
    assert(diff * w == 1);
}

#[test]
fn test_main() {
    // Test case: x=10, y=3, w=1
    // 10 != 3^2 = 9, so diff = 10 - 9 = 1, and 1 * 1 = 1 (checkmark)
    main(10, 3, 1);
}
