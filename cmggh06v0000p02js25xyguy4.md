---
title: "Discover Run Kit: Your Versatile REPL and Command Line Tool for 25+ Languages"
seoTitle: "Explore Run Kit: Multi-Language REPL Tool"
seoDescription: "Run Kit facilitates coding in 25+ languages with a consistent CLI and REPL. Built in Rust for efficient, cross-platform development"
datePublished: Tue Oct 07 2025 11:22:28 GMT+0000 (Coordinated Universal Time)
cuid: cmggh06v0000p02js25xyguy4
slug: discover-run-kit-your-versatile-repl-and-command-line-tool-for-25-languages
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1759836109839/abc955b8-271c-41ba-aa68-f2e61fcc03a2.png
tags: opensource, cli, rust, rust-programming

---


#  Website & Docs

🔗 [Website](https://run.esubalew.et/) • [Docs Overview](https://run.esubalew.et/docs/overview)

> **Run** is a universal code runner built in **Rust** for developers who use multiple programming languages.
> It gives you one simple CLI, smart REPLs, and ready-to-use examples for 25+ languages.

---

##  Explore

* **Website** → [https://run.esubalew.et](https://run.esubalew.et)
* **Docs Overview** → [https://run.esubalew.et/docs/overview](https://run.esubalew.et/docs/overview)

Check out these links for full documentation, examples, and feature guides.

---

#  Overview — Universal Multi-Language Runner

**Run** lets you execute and experiment with code in 25+ programming languages using one consistent CLI.

##  What is `run`?

Run is a **universal code runner** and **smart REPL** built with Rust.
It unifies compilers and interpreters into a single command-line tool — no more switching between environments or remembering different commands.

Whether you're:

* A **beginner** learning your first language,
* A **student** testing quick code snippets,
* A **developer** prototyping across multiple languages,
* Or a **teacher** explaining programming concepts —

**Run** makes coding faster and easier.

---

##  Why Run Exists

Setting up each language separately can be painful — installing compilers, dealing with paths, remembering flags, and fighting with version conflicts.

Run fixes that by giving you:

* **One CLI** for all languages
* **No setup hassles**
* **Consistent commands**
* **Less cognitive load**

You just write code — Run takes care of the rest.

---

## 🦀 Why Rust?

Run is written in **Rust** for:

* ⚡ **Speed** — starts and runs instantly
* 🧱 **Reliability** — safe and crash-free by design
* 🖥️ **Cross-platform** — works on macOS, Linux, and Windows
* 🧠 **Modern tooling** — built and distributed easily with Cargo

---

##  Quickstart

```bash
# Check version
run --version

# Run inline code
run --lang python --code "print('Hello, world!')"

# Detect language from file
run examples/go/hello/main.go

# Start REPL
run

# Pipe stdin into Node.js
echo '{"name":"Ada"}' | run js --code "const data = JSON.parse(require('fs').readFileSync(0,'utf8')); console.log(`Hi ${data.name}`)"
```

---

##  Installation

All builds are available on [GitHub Releases](https://github.com/Esubaalew/run/releases).
Choose the one that fits your system.

###  Using Cargo

```bash
cargo install run-kit
```

Or build from source:

```bash
git clone https://github.com/Esubaalew/run.git
cd run
cargo install --path .
```

###  Using Homebrew (macOS)

```bash
brew install --formula https://github.com/Esubaalew/run/releases/latest/download/homebrew-run.rb
```

###  Windows (Scoop)

```powershell
scoop install https://github.com/Esubaalew/run/releases/latest/download/run-scoop.json
```

###  Install Script (macOS/Linux)

```bash
curl -fsSLO https://raw.githubusercontent.com/Esubaalew/run/master/scripts/install.sh
chmod +x install.sh
./install.sh --add-path
```

###  Verify

```bash
run --version
```

Output:

```
run 0.1.1
```

---

##  How It Works

`run` uses real compilers and interpreters under the hood.
Each language has its own small “engine” that:

1. Detects if the toolchain exists
2. Prepares a workspace
3. Runs your code
4. Keeps session state in the REPL

This makes it lightweight and easy to extend with new languages.

---

##  Supported Languages (25+)

**Scripting:** Python, JavaScript, Ruby, Bash, PHP, Perl, Lua
**Compiled:** Rust, Go, C, C++, Java, C#, Swift, Kotlin, Zig, Nim
**Functional / Typed:** Haskell, TypeScript, Elixir, Julia
**Specialized:** R, Dart, Crystal

You can use short aliases too:

```
py, js, ts, rs, go, cpp, cs, rb, sh, php, hs, ex, jl, dart, kt
```

---

##  Summary

Run is for developers who:

* Jump between multiple languages
* Want consistent behavior everywhere
* Prefer one fast, safe, and smart CLI tool

👉 [Visit the website](https://run.esubalew.et) or
📘 [Read the docs](https://run.esubalew.et/docs/overview)
