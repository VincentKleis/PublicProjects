fn conjunction(list_of_bool[bool;255])->bool{
    let x = true;
    for y in list_of_bool{
        if x == y{
            continue
        } else{
            return false
        }
    }
    return true

}

fn main(){
    let x = conjunction([true, true, false]);
    let y = conjunction([true, true, true]);

    print!("true  true = {}, true conjuction false = {}", y, x)
}