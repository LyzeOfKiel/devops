# HTTP time server

## Run

### Directly on target machine:

```bash
cargo run --release
```

### Or with docker:

```bash
docker build -t app_rust .
docker run -d -p 8000:8000 app_rust
```

## Lint

Using [clippy](https://github.com/rust-lang/rust-clippy):

```bash
cargo clippy -- -D warnings
```
