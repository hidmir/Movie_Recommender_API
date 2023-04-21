FROM python:3.9

FROM ghcr.io/railwayapp/nixpacks:ubuntu-1678752204@sha256:fba77818e57bebd4e7a02f60d45554354d6ec5a3f7d98b4ee4f6b2a6e720191e

WORKDIR /app

COPY .nixpacks/nixpkgs-293a28df6d7ff3dec1e61e37cc4ee6e6c0fb0847.nix .nixpacks/nixpkgs-293a28df6d7ff3dec1e61e37cc4ee6e6c0fb0847.nix

RUN nix-env -if .nixpacks/nixpkgs-293a28df6d7ff3dec1e61e37cc4ee6e6c0fb0847.nix && nix-collect-garbage -d

RUN printf '\nPATH=/opt/venv/bin:$PATH' >> /root/.profile

COPY . /app/.

RUN --mount=type=cache,id=s/881b65bd-923c-4526-b322-6b598bac1f40-/root/cache/pip,target=/root/.cache/pip python -m venv /opt/venv && . /opt/venv/bin/activate && pip install -r requirements.txt

COPY . /app

ENV PYTHON_ENV=production

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
