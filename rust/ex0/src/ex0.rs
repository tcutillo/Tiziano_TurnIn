use rand::Rng;
use rand::random;
use std::io;

pub fn fahrenheit_celsius_converter(temperature: i32, f2c: bool) -> f32 {
    if f2c == true {
        return (temperature as f32 -32.0) * (5.0 / 9.0)
    } else {
        return (temperature as f32 * (9.0 / 5.0)) + 32.0
    }
}

pub fn dice_roll(sides: u8) -> u8 {
    if sides < 2 {
        return 0;
    }

    let mut rng = rand::thread_rng();
    let result: u8 = rng.gen_range(1..(sides+1)) as u8;
    return result;
}

pub fn multi_strings(s: String) -> [String; 4] {
    let mut s2 = s.clone();
    let mut s3 = s.clone();
    let mut s4 = s.clone();

    s2.push_str("ONE");
    s3.push_str("TWO");
    s4.push_str("THREE");

    let multi_str: [String; 4] = [s, s2, s3, s4];
    return multi_str;
}

pub fn add_vowels(s: &mut String) {
    let mut s2 = String::new();
    for c in s.chars() {
        if c == 'a' || c == 'A' || c == 'i' || c == 'I' || c == 'u' || c == 'U'
            || c == 'e' || c == 'E' || c == 'o' || c == 'O' {
            s2.push(c);
        }
        s2.push(c);
    }
    *s = s2; 
}

pub fn echo_split(whole: String, num: u32) {
    let (first, second);
    if num%2 == 1 {
        (first, second) = whole.split_at(whole.len() / 2);
    } else {
        (first, second) = whole.split_at((whole.len() + 1) / 2);
    }
    for _ in 0..num {
        print!("{}", first);
    }
    print!(" ");
    for _ in 0..num {
        print!("{}", second);
    }
    println!("");
}

pub fn input_number(high: u32) -> Option<u32> {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Failed to read line");
    let input: u32 = match input.trim().parse() {
        Ok(num) => num,
        Err(_) => return None,
    };
    if input >= high {
        return None;
    }
    Some(input)
}

pub enum Card {
    Diamond(String),
    Club(String),
    Heart(String),
    Spade(String)
}
pub fn draw_card() -> Card {
    let suit = random::<u8>() % 4;
    let face = random::<u8>() % 13;
    let face = match face {
        0 => "2".to_owned(),
        1 => "3".to_owned(),
        2 => "4".to_owned(),
        3 => "5".to_owned(),
        4 => "6".to_owned(),
        5 => "7".to_owned(),
        6 => "8".to_owned(),
        7 => "9".to_owned(),
        8 => "10".to_owned(),
        9 => "Jack".to_owned(),
        10 => "Queen".to_owned(),
        11 => "King".to_owned(),
        12 => "Ace".to_owned(),
        _ => "2".to_owned(),
    };
    match suit {
        0 => Card::Diamond(face),
        1 => Card::Club(face),
        2 => Card::Heart(face),
        3 => Card::Spade(face),
        _ => Card::Diamond(face),
    }
}