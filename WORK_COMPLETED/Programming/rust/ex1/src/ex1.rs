use std::collections::HashMap;
use std::fmt::{Display, Debug};
use std::ops::AddAssign;

pub struct Bank<T, U> {
	banker: String,
	vault: HashMap<String, T>,
	lock_box: HashMap<String, Vec<U>>,
	min_deposit: T
}

impl<T: PartialOrd + Display + Default + AddAssign, U: Debug> Bank<T, U> {
	pub fn new(banker: String, min_deposit: T) -> Self {
		Self { 
			banker, 
			vault: HashMap::new(), 
			lock_box: HashMap::new(),
			min_deposit
		}
	}
	
	pub fn greeting(&self) {
		println!("hi welcome to my bank my name is {}", self.banker);
	}

	pub fn banker(&self) -> &String {
		&self.banker
	}
	
	pub fn deposit(&mut self, customer: &str, amount: T) {
		if amount > self.min_deposit {
			print!("Thank you, {} for your deposit of {amount}", customer);
			let account = self.vault.entry(customer.to_string()).or_insert(T::default());
			*account += amount;
		} else {
			print!("sorry your deposit doesn't meet our minimum standard");
		}
		println!(" - {}", self.banker);
	}

	pub fn deposit_lock_box(&mut self, customer: &str, item: U) {
		let l_box = self.lock_box.entry(customer.to_string()).or_insert(Vec::new());
		(*l_box).push(item);
		println!("{customer}, your item is now locked away\n - {}", self.banker);
		for (cust, loot) in &self.lock_box {
			println!("in box {:?}", loot);
		}
	}
}
