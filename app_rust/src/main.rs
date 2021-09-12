#[macro_use]
extern crate rocket;

use chrono::{TimeZone, Utc};
use chrono_tz::Europe::Moscow;
use std::net::SocketAddr;
use rocket_dyn_templates::Template;
use std::collections::HashMap;

#[get("/")]
fn index(remote_addr: SocketAddr) -> Template {
    println!("Requst from {}", remote_addr);
    let utc = Utc::now().naive_utc();
    let moscow_time = Moscow
        .from_utc_datetime(&utc)
        .format("%H:%M:%S")
        .to_string();

    let mut context = HashMap::new();
    context.insert("time", moscow_time);

    Template::render("index", &context)
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .mount("/", routes![index])
        .attach(Template::fairing())
}
