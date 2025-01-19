pub fn run(){
    // string type
    let mut hello = String::from("Hello");

    // primitive str type
    let _hello_str = "Hello";

    // Get length
    println!("Length{}", hello.len());

    // Push char
    hello.push('W');

    // Push str
    hello.push_str("orld!");

    // Capacity in bytes
    println!("Capacity: {}", hello.capacity());

    // Check if empty
    println!("Is Empty: {}", hello.is_empty());

    // Contains
    println!("{}", hello);

    //Replace
    println!("Replace: {}", hello.replace("World", "There"));

    // Loop through string by whitespace
    for word in hello.split_whitespace(){
        println!("{}", word);
    }

    // Create string with capacity
    let mut s = String::with_capacity(10);
    s.push('a');
    s.push('b');

    // Assertion testing
    assert_eq!(2, s.len());
    assert_eq!(10, s.capacity());

    println!("{}", s)
}