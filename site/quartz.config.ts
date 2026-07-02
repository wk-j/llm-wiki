import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 configuration for the LLM Wiki (Second Brain).
 *
 * This file is copied over the default `quartz.config.ts` inside a freshly
 * cloned Quartz checkout by `.github/workflows/deploy.yml`. It is not meant to
 * run from this repository directly — Quartz's own source tree provides the
 * `./quartz/*` modules imported below. See `site/README.md`.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "LLM Wiki",
    pageTitleSuffix: " · Second Brain",
    enableSPA: true,
    enablePopovers: true,
    // No external analytics — this is a personal knowledge base.
    analytics: null,
    locale: "en-US",
    // GitHub Pages project site served under /llm-wiki. Quartz emits relative
    // links, so the subpath in baseUrl is what makes RSS/sitemap/OG URLs correct.
    baseUrl: "wk-j.github.io/llm-wiki",
    ignorePatterns: ["private", "templates", ".obsidian", "**/.DS_Store"],
    // Our pages carry `created` / `updated` in frontmatter; prefer those.
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        // Quartz defaults. Note: these are Latin-only, so Thai text falls back
        // to each device's system Thai font (Thonburi / Leelawadee / Noto).
        header: "Schibsted Grotesk",
        body: "Source Sans Pro",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#faf8f8",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#2b2b2b",
          secondary: "#284b63",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#161618",
          lightgray: "#393639",
          gray: "#646464",
          darkgray: "#d4d4d4",
          dark: "#ebebec",
          secondary: "#7b97aa",
          tertiary: "#84a59d",
          highlight: "rgba(143, 159, 169, 0.15)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      // NOTE: Latex transformer intentionally omitted. The wiki is Thai-primary
      // prose that uses `$` as a literal character; KaTeX would try to parse
      // Thai text inside `$...$` as math and mangle it.
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
