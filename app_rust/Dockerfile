FROM rust:1.54 as build

WORKDIR /app

COPY . .

RUN cargo build --release


FROM frolvlad/alpine-glibc:glibc-2.33

WORKDIR /app

RUN adduser --disabled-password app && chown -R app /app

COPY templates templates
COPY --from=build /app/target/release/app_rust .

USER app

EXPOSE 8000

ENV ROCKET_ADDRESS="0.0.0.0"

CMD ["./app_rust"]
