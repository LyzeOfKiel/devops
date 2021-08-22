FROM rust:1.54 as build

WORKDIR /app

COPY . .

RUN cargo install --path .


FROM frolvlad/alpine-glibc:glibc-2.33

WORKDIR /app

COPY templates templates
COPY --from=build /usr/local/cargo/bin/app_rust .

ENV ROCKET_ADDRESS="0.0.0.0"

CMD ["./app_rust"]
