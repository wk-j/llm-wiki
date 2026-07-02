# Website (Quartz → GitHub Pages)

The wiki in `../wiki/` is rendered to a static site with
[Quartz v4](https://quartz.jzhao.xyz) and published to GitHub Pages at
<https://wk-j.github.io/llm-wiki/>.

## How it works

The site is **not** vendored into this repo. `.github/workflows/deploy.yml`:

1. Checks out this repo.
2. Fetches a pinned Quartz commit (`QUARTZ_REF` in the workflow) into `quartz/`.
3. Copies `wiki/*` into Quartz's `content/` and `site/quartz.config.ts` over
   Quartz's default config.
4. Runs `npm ci && npx quartz build`.
5. Uploads `quartz/public/` and deploys it to Pages.

So the only site files tracked here are `site/quartz.config.ts` (branding,
`baseUrl`, plugin choices) and the workflow. Content stays in `wiki/`.

## What the config changes vs. Quartz defaults

- `pageTitle` / `pageTitleSuffix` → **LLM Wiki · Second Brain**
- `baseUrl` → `wk-j.github.io/llm-wiki` (project page subpath)
- `analytics` → `null` (no external tracking)
- Drops the **Latex** transformer — the wiki is Thai prose that uses `$` as a
  literal character; KaTeX would parse Thai inside `$...$` as math.

## One-time GitHub setup

Repo **Settings → Pages → Build and deployment → Source = GitHub Actions**.
After that, every push to `master` touching `wiki/**` or `site/**` redeploys.

## Building locally

```sh
git clone --branch v4 https://github.com/jackyzha0/quartz.git /tmp/quartz
cd /tmp/quartz
rm -rf content && mkdir content
cp -R /path/to/llm-wiki/wiki/. content/
cp /path/to/llm-wiki/site/quartz.config.ts quartz.config.ts
npm ci
npx quartz build --serve   # http://localhost:8080
```

> Node 22 LTS is recommended. Very new Node (26+) can deadlock Quartz's bundled
> esbuild; if so, `npm i esbuild@0.25.10` in the Quartz checkout works around it.
