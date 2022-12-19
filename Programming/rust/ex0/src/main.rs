// use std::io::{Write, BufReader, BufRead, ErrorKind};
// use rand::Rng;
// use std::fs::File;
// use std::cmp::Ordering;
// use std::io;

mod ex0;

fn main() {
    fahrenheit_to_converter(52, true);
    fahrenheit_to_converter(0, false);
    test_dice_role();
    test_multi_strings();
}

fn fahrenheit_to_converter(temperature: i32, f2c: bool) {
    let result = ex0::fahrenheit_celsius_converter(temperature, f2c);
    
    println!("conversion : {}", result);
}

fn test_dice_role() {
    let result = ex0::dice_roll(2);

    println!("result = {}", result);
}

fn test_multi_strings() {
    let result = ex0::multi_strings("../".to_owned());

    println!("result = {:?}", result);
}