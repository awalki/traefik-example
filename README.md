# Traefik Example

Usage example for Traefik with TSL and Cloudflare

## How to set up

1. Get a Cloudflare token
2. Fill in the token in `traefik/.env`
3. Run `docker compose up -d --build` in the `traefik` directory
4. Run `docker compose up -d --build` in the `service` directory

## Make sure that you have a dns record that points to the IP of the traefik container

> A: *.example.com 172.16.58.3 (Cloudflare)

Also, change the domain in `traefik/traefik.toml` and `service/docker-compose.yml` to your domain

