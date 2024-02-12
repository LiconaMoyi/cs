use std::collections::HashMap;

fn main() {
  let mut my_gems = HashMap::with_capacity(1);
  my_gems.insert("红宝石", 3);
  println!("{:?}", my_gems);
}