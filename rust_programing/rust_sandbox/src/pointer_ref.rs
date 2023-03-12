pub fn run() {
  // Primitive Array
  let _arr1 = [1,2,3];
  let _arr2 = _arr1;

  // Non Primitive

  // Vector
  let vec1 = vec![1,2,3];
  let vec2 = &vec1;

  println!("Values: {:?}", (&vec1, vec2))
}